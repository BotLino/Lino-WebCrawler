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


if __name__ == '__main__':
    app.run(debug=True)
