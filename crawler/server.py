import subprocess
import os
from populate import saveMenu
from pymongo import MongoClient
from datetime import datetime
from flask import Flask, jsonify

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


def getMenu():
    today = datetime.today().strftime('%d/%m/%Y')
    cursor = collection.find({'dates': today})
    for record in cursor:
        return record['menu']


def isValidDay(day):
    return day in valid_days


@app.route('/cardapio/update')
def populate_database():
    subprocess.check_output(['python', 'scraper.py'])
    saveMenu('weekMenu.json')
    return jsonify({'status': 'Success', 'updated': True})


@app.route('/cardapio/week')
def weekMenu():
    return jsonify(getMenu())


@app.route('/cardapio/<day>')
def menu_day(day):
    if not isValidDay(day):
        return jsonify({'status': 'error', 'description': 'Wrong day'}), 400
    menu = getMenu()
    return jsonify(menu[day])


@app.route('/cardapio/<day>/Desjejum')
def breakfastMenu(day):
    if not isValidDay(day):
        return jsonify({'status': 'error', 'description': 'Wrong day'}), 400
    menu = getMenu()
    return jsonify(menu[day]['DESJEJUM'])


@app.route('/cardapio/<day>/Almoco')
def lunchMenu(day):
    if not isValidDay(day):
        return jsonify({'status': 'error', 'description': 'Wrong day'}), 400
    menu = getMenu()
    return jsonify(menu[day]['ALMOÇO'])


@app.route('/cardapio/<day>/Jantar')
def dinnerMenu(day):
    if not isValidDay(day):
        return jsonify({'status': 'error', 'description': 'Wrong day'}), 400
    menu = getMenu()
    return jsonify(menu[day]['JANTAR'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
