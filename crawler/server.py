import json
import os
import subprocess
from pymongo import MongoClient
from datetime import datetime
from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

client = MongoClient('localhost', 27008)
db = client.ru
collection = db.menu


@app.route('/')
def hello():
    return """
        <h1>Go to /cardapio/[day] </h1>
    """


@app.route('/cardapio/download')
def get_today_menu():
    subprocess.check_output(['python', 'scraper.py'])
    return redirect(url_for('hello'))


@app.route('/cardapio/update')
def populate_database():
    subprocess.check_output(['python', 'scraper.py', '-a', '-w'])
    subprocess.check_output(['python', 'populate.py'])
    return redirect(url_for('hello'))


@app.route('/cardapio/week')
def weekMenu():
    today = datetime.today().strftime('%d/%m/%Y')
    cursor = collection.find({'dates': today})
    for record in cursor:
        return jsonify(record['menu'])


@app.route('/cardapio/<day>')
def menu_day(day):
    already_exists = os.path.isfile('./menu.json')
    if already_exists:
        subprocess.check_output(['python', 'scraper.py', '-d', day])
        f = open('menu.json', 'r')
        result = json.load(f)
        print(day)
        print(result)
        return jsonify(result)
    else:
        subprocess.check_output(['python', 'scraper.py', '-a', '-d', day])
        f = open('menu.json', 'r')
        result = json.load(f)
        return jsonify(result)


@app.route('/cardapio/<day>/Desjejum')
def breakfastMenu(day):
    already_exists = os.path.isfile('./desjejumMenu.json')
    if already_exists:
        subprocess.check_output(
            ['python', 'scraper.py', '-d', day, '-r', 'Desjejum'])
        f = open('desjejumMenu.json', 'r')
        result = json.load(f)
        return jsonify(result)
    else:
        subprocess.check_output(
            ['python', 'scraper.py', '-a', '-d', day, '-r', 'Desjejum'])
        f = open('menu.json', 'r')
        result = json.load(f)
        return jsonify(result)


@app.route('/cardapio/<day>/Almoco')
def lunchMenu(day):
    already_exists = os.path.isfile('./almocoMenu.json')
    if already_exists:
        subprocess.check_output(
            ['python', 'scraper.py', '-d', day, '-r', 'Almoco'])
        f = open('almocoMenu.json', 'r')
        result = json.load(f)
        return jsonify(result)
    else:
        subprocess.check_output(
            ['python', 'scraper.py', '-a', '-d', day, '-r', 'Almoco'])
        f = open('almocoMenu.json', 'r')
        result = json.load(f)
        return jsonify(result)


@app.route('/cardapio/<day>/Jantar')
def dinnerMenu(day):
    already_exists = os.path.isfile('./jantarMenu.json')
    if already_exists:
        subprocess.check_output(
            ['python', 'scraper.py', '-d', day, '-r', 'Jantar'])
        f = open('jantarMenu.json', 'r')
        result = json.load(f)
        return jsonify(result)
    else:
        subprocess.check_output(
            ['python', 'scraper.py', '-a', '-d', day, '-r', 'Jantar'])
        f = open('jantarMenu.json', 'r')
        result = json.load(f)
        return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
