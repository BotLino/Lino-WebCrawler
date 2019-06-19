import os
import re
from datetime import datetime, timedelta


def get_menu():
    path = "./downloads"

    today = datetime.today().date()
    today = today + timedelta(days=1)
    today = today.strftime('%d/%m/%Y')
    dt = datetime.strptime(today, '%d/%m/%Y')
    start = dt - timedelta(days=dt.weekday())
    start = start.strftime('%d-%m-%Y')
    fileName = start + ".txt"

    for menuFile in os.listdir(path):
        if fileName == menuFile:
            fileName = path + "/" + fileName
            file = open(fileName, 'r')
            break

    stringzona = ""
    line = ""
    foods = []

    for line in file:
        if line[len(line)-1] == '\n':
            line = line[:len(line)-1] + " "

        stringzona = stringzona + line

    words = stringzona.split(" ")

    for word in words:
        if word != '':
            foods.append(word)

    id_desjejum = foods.index("DESJEJUM") + 8
    id_almoco = foods.index("ALMOÇO") + 8
    id_jantar = foods.index("JANTAR") + 8
    id_end = foods.index("Legenda:")

    menu = {}

    menu["DESJEJUM"] = {
        "Bebidas quentes": [],
        "Vegetariano 1": [],
        "Vegetariano 2": [],
        "Vegetariano 3": [],
        "Achocolatado": [],
        "Pão": [],
        "Complemento 1": [],
        "Complemento 2": [],
        "Comp. Vegetariano": [],
        "Fruta": []
    }
    menu["ALMOÇO"] = {
        "Salada:": [],
        "Molho:": [],
        "Prato Principal:": [],
        "Guarnição:": [],
        "Prato Vegetariano:": [],
        "Acompanhamentos:": [],
        "Sobremesa:": [],
        "Refresco:": []
    }
    menu["JANTAR"] = {
        "Salada:": [],
        "Molho:": [],
        "Sopa:": [],
        "Pão:": [],
        "Prato Principal:": [],
        "Prato Vegetariano:": [],
        "Acompanhamentos:": [],
        "Sobremesa:": [],
        "Refresco:": []
    }

    keys_desjejum = ["Bebidas", "Vegetariano", "Achocolatado", "Pão", "Complemento",
                     "Comp.", "Fruta"]

    keys_almoco = ["Salada:", "Molho:", "Principal:", "Guarnição:",
                   "Vegetariano:", "Acompanhamentos:", "Sobremesa:", "Refresco:"]

    keys_jantar = ["Salada:", "Molho:", "Principal:", "Sopa:", "Pão:",
                   "Vegetariano:", "Acompanhamentos:", "Sobremesa:", "Refresco:"]

    key = ""
    counter_v = 1
    counter_pao = 1
    counter_achocolatado = 1
    counter_c = 1
    it = iter(range(id_desjejum, id_almoco-8))

    for x in it:
        if foods[x] in keys_desjejum:
            if foods[x] == "Bebidas" or foods[x] == "Comp.":
                key = foods[x] + " " + foods[x+1]
                x = next(it)
            elif foods[x] == "Vegetariano":
                key = foods[x] + " " + str(counter_v)
                counter_v = counter_v + 1
            elif foods[x] == "Complemento":
                key = foods[x] + " " + str(counter_c)
                counter_c = counter_c + 1
            elif foods[x] == "Pão":
                if counter_pao == 1:
                    key = foods[x]
                    counter_pao = counter_pao - 1
                else:
                    menu["DESJEJUM"][key].append(foods[x])
            elif foods[x] == "Achocolatado":
                if counter_achocolatado == 1:
                    key = foods[x]
                    counter_achocolatado = counter_achocolatado - 1
                else:
                    menu["DESJEJUM"][key].append(foods[x])
            else:
                key = foods[x]
        else:
            menu["DESJEJUM"][key].append(foods[x])

    it = iter(range(id_almoco, id_jantar-8))
    for x in it:
        if foods[x] in keys_almoco:
            if foods[x] == "Principal:" or foods[x] == "Vegetariano:":
                key = foods[x-1] + " " + foods[x]
            else:
                key = foods[x]
        else:
            if foods[x] != "Prato":
                menu["ALMOÇO"][key].append(foods[x])

    it = iter(range(id_jantar, id_end))
    for x in it:
        if foods[x] in keys_jantar:
            if foods[x] == "Principal:" or foods[x] == "Vegetariano:":
                key = foods[x-1] + " " + foods[x]
            else:
                key = foods[x]
        else:
            if foods[x] != "Prato":
                menu["JANTAR"][key].append(foods[x])

    menu_days = {
        "Segunda-feira": {
            "DESJEJUM": {},
            "ALMOÇO": {},
            "JANTAR": {}
        },
        "Terça-feira": {
            "DESJEJUM": {},
            "ALMOÇO": {},
            "JANTAR": {}
        },
        "Quarta-feira": {
            "DESJEJUM": {},
            "ALMOÇO": {},
            "JANTAR": {}
        },
        "Quinta-feira": {
            "DESJEJUM": {},
            "ALMOÇO": {},
            "JANTAR": {}
        },
        "Sexta-feira": {
            "DESJEJUM": {},
            "ALMOÇO": {},
            "JANTAR": {}
        },
        "Sábado": {
            "DESJEJUM": {},
            "ALMOÇO": {},
            "JANTAR": {}
        },
        "Domingo": {
            "DESJEJUM": {},
            "ALMOÇO": {},
            "JANTAR": {}
        }
    }

    is_title = []
    _is_title = {}
    menu_index = {}
    prohibited_list = ['Vegetariana']

    for element in menu.keys():
        for e in menu[element].keys():
            for i in range(0, len(menu[element][e])):
                if menu[element][e][i].istitle() \
                   and menu[element][e][i-1] != '/' \
                   and menu[element][e][i-1] != 'molho' \
                   and menu[element][e][i][0] != '/' \
                   and menu[element][e][i-1] != 'à' \
                   and menu[element][e][i] not in prohibited_list \
                   and menu[element][e][i-1] != "de" \
                   and menu[element][e][i-1] != 'e':
                    is_title.append(i)
            _is_title[e] = []
            _is_title[e].append(is_title)
            _is_title[e].append(menu[element][e])
            is_title = []

        menu_index[element] = _is_title
        _is_title = {}

    # print(menu_index)
    days = ["Segunda-feira", "Terça-feira", "Quarta-feira",
            "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

    for e in menu_index.keys():
        for key, food in zip(menu_index[e].keys(), menu_index[e].values()):
            for i in range(0, len(food[0])):
                if i+1 == len(food[0]):
                    food_words = food[1][food[0][i]:]
                else:
                    food_words = food[1][food[0][i]:food[0][i+1]]

                complete_word = ""
                counter_words = 0
                for word in food_words:
                    complete_word += word
                    if counter_words != len(food_words)-1:
                        complete_word += " "
                    counter_words += 1
                menu_days[days[i]][e][key] = complete_word
                print(complete_word)
    print(menu_days)

    return menu_days
