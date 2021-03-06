import subprocess
import os
import current_date
import json
from datetime import datetime
from populate import save_menu
from pymongo import MongoClient
from flask import Flask, jsonify, send_file
from scraper import PdfReader

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

DB_URI = os.getenv('DB_URI', 'localhost')
client = MongoClient(DB_URI)
db = client.ru
collection = db.menu

valid_days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]

days = {
    'sunday': 'Domingo',
    'monday': 'Segunda-feira',
    'tuesday': 'Terça-feira',
    'wednesday': 'Quarta-feira',
    'thursday': 'Quinta-feira',
    'friday': 'Sexta-feira',
    'saturday': 'Sábado'
}


def getMenu():
    today = datetime.today().strftime('%d/%m/%Y')
    cursor = collection.find({'dates': today})

    for record in cursor:
        return record['menu']


def isValidDay(day):
    return day in valid_days


@app.route('/cardapio/update')
def populate_database():
    subprocess.call('touch weekMenu.json', shell=True)
    subprocess.check_output(['python', 'scraper.py'])

    save_menu('weekMenu.json')

    return jsonify({'status': 'Success', 'updated': True})


@app.route('/cardapio/week')
def weekMenu():
    return jsonify(getMenu())


@app.route('/cardapio/pdf')
def getPdf(filePath='result.json'):
    with open(filePath) as f:
        menuList = json.load(f)
        pdf_name = ''
        start = current_date.get_first_day_week('/')

        for item in menuList:
            # Adds validation in 'url' field
            # to avoid errors due changes in links text
            if start in item['text'].split(' '):
                pdf_name = item['path'].split('/').pop()

                break

    if pdf_name:
        pdf = PdfReader()
        pdf_path = './downloads/' + pdf_name
        os.mkdir('./static') if 'static' not in os.listdir('./') else None
        pdf.gen_image(pdf_path, './static/', 'pdfImage')

        return send_file('./static/pdfImage.png')
    else:
        return jsonify({
            'status': 'error',
            'description': 'pdf not found'
        }), 404


@app.route('/cardapio/<day>')
def menu_day(day):
    if not isValidDay(day):
        return jsonify({'status': 'error', 'description': 'Wrong day'}), 400

    p = PdfReader()
    menu = p.gen_menu()
    day = days[day.lower()]

    return jsonify(menu[day])


@app.route('/cardapio/<day>/<meal>/')
def menu_specific_meal(day, meal):
    if not isValidDay(day):
        return jsonify({'status': 'error', 'description': 'Wrong day'}), 400

    p = PdfReader()
    menu = p.gen_menu()
    day = days[day.lower()]
    meal = meal.upper()

    return jsonify(menu[day][meal])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5010')
