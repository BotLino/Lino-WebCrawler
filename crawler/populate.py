import datetime
import re
import json
import os
from pymongo import MongoClient

DB_URI = os.getenv('DB_URI', 'localhost')
client = MongoClient(DB_URI)
db = client.ru
collection = db.menu


def get_date_range(filePath):
    """
    Returns the start and end date for a given menu.
    """
    with open(filePath) as f:
        menu_list = json.load(f)
        today = datetime.datetime.now()
        regex = re.compile(r'(?P<date>\d{2}/\d{2})')
        date_range = []

        for item in menu_list:
            # Adds validation in 'url' field
            # to avoid errors due changes in links text
            if 'FGA' in item['path']:
                _day = datetime.datetime.strptime(
                    regex.findall(item['text'])[0],
                    '%d/%m'
                )

                if today >= _day:
                    date_range = regex.findall(item['text'])

        date_range = [date + '/2018' for date in date_range]

        return date_range


def generate_dates_list(startDate, endDate):
    """
    Creates a list of all dates between a given range.
    """
    allDates = []
    startDate = datetime.datetime.strptime(startDate, '%d/%m/%Y')
    endDate = datetime.datetime.strptime(endDate, '%d/%m/%Y')
    step = datetime.timedelta(days=1)

    while startDate <= endDate:
        allDates.append(startDate.strftime('%d/%m/%Y'))
        startDate += step

    return allDates


def generate_week_menu_objects(dateList, weekMenu):
    """
    Creates the object with the attributes to save in teh database.
    """
    weekObj = {}
    weekObj['menu'] = weekMenu
    weekObj['dates'] = dateList

    return weekObj


def save_menu(filePath, datesPath='result.json'):
    """
    Saves the content of filePath to the database.
    """
    f = open(filePath, 'r')
    weekMeals = json.load(f)
    dates = get_date_range(datesPath)
    dates = generate_dates_list(*dates)
    obj = generate_week_menu_objects(dates, weekMeals)
    collection.replace_one({'dates': dates}, obj, upsert=True)


if __name__ == '__main__':
    save_menu('weekMenu.json')
