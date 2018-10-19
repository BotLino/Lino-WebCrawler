import subprocess
from populate import saveMenu
from pymongo import MongoClient
from datetime import datetime
from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

client = MongoClient('mongodb://mongo-ru:27017/ru')
db = client.ru
collection = db.menu


def getMenu():
    today = datetime.today().strftime('%d/%m/%Y')
    cursor = collection.find({'dates': today})
    for record in cursor:
        return record['menu']


@app.route('/')
def hello():
    return """
        <h1>Go to /cardapio/[day] </h1>
    """


@app.route('/cardapio/update')
def populate_database():
    subprocess.check_output(['python', 'scraper.py'])
    saveMenu()
    return redirect(url_for('hello'))


@app.route('/cardapio/week')
def weekMenu():
    return jsonify(getMenu())


@app.route('/cardapio/<day>')
def menu_day(day):
    menu = getMenu()
    return jsonify(menu[day])


@app.route('/cardapio/<day>/Desjejum')
def breakfastMenu(day):
    menu = getMenu()
    return jsonify(menu[day]['DESJEJUM'])


@app.route('/cardapio/<day>/Almoco')
def lunchMenu(day):
    menu = getMenu()
    return jsonify(menu[day]['ALMOÇO'])


@app.route('/cardapio/<day>/Jantar')
def dinnerMenu(day):
    menu = getMenu()
    return jsonify(menu[day]['JANTAR'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
