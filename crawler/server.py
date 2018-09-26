import json
import os
import subprocess
from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def hello():
    return """
        <h1>Go to /cardapio/[day] </h1>
    """

# @app.route('/cardapio')
# def menu():
#     f = open('menu.json', 'r')
#     result = json.load(f)
#     print(result)
#     return jsonify(result)

@app.route('/cardapio/download')
def get_today_menu():
    already_exists = os.path.isfile('./menu.json')
    if already_exists:
        return redirect(url_for('hello'))
    else:
        subprocess.check_output(['python', 'scraper.py'])
        return redirect(url_for('hello'))

@app.route('/cardapio/week')
def weekMenu():
    already_exists = os.path.isfile('./weekMenu.json')
    if already_exists:
        subprocess.check_output(['python','scraper.py','-w'])
        f = open('weekMenu.json','r')
        result = json.load(f)
        return jsonify(result)
    else:
        subprocess.check_output(['python','scraper.py','-a','-w'])
        f = open('weekMenu.json', 'r')
        result = json.load(f)
        return jsonify(result)

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
        subprocess.check_output(['python', 'scraper.py', '-d',day,'-r','Desjejum'])
        f = open('desjejumMenu.json', 'r')
        result = json.load(f)
        return jsonify(result)
    else:
        subprocess.check_output(['python', 'scraper.py', '-a', '-d', day,'-r','Desjejum'])
        f = open('menu.json', 'r')
        result = json.load(f)
        return jsonify(result)

@app.route('/cardapio/<day>/Almoco')
def lunchMenu(day):
    already_exists = os.path.isfile('./almocoMenu.json')
    if already_exists:
        subprocess.check_output(['python', 'scraper.py', '-d',day,'-r','Almoco'])
        f = open('almocoMenu.json', 'r')
        result = json.load(f)
        return jsonify(result)
    else:
        subprocess.check_output(['python', 'scraper.py', '-a', '-d', day,'-r','Almoco'])
        f = open('almocoMenu.json', 'r')
        result = json.load(f)
        return jsonify(result)

@app.route('/cardapio/<day>/Jantar')
def dinnerMenu(day):
    already_exists = os.path.isfile('./jantarMenu.json')
    if already_exists:
        subprocess.check_output(['python', 'scraper.py', '-d',day,'-r','Jantar'])
        f = open('jantarMenu.json', 'r')
        result = json.load(f)
        return jsonify(result)
    else:
        subprocess.check_output(['python', 'scraper.py', '-a', '-d', day,'-r','Jantar'])
        f = open('jantarMenu.json', 'r')
        result = json.load(f)
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
