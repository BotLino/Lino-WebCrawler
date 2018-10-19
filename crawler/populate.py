import datetime
import re
import json
import os
from pymongo import MongoClient

DB_URI = os.getenv('DB_URI', 'localhost')
client = MongoClient(DB_URI)
db = client.ru
collection = db.menu


def getDateRange(filePath):
    """
    Returns the start and end date for a given menu.
    """
    with open(filePath) as f:
        menuList = json.load(f)
        today = datetime.datetime.now()
        regex = re.compile(r'(?P<date>\d{2}/\d{2}/\d{4})')
        dateRange = []
        for item in menuList:
            if 'FGA' in item['text']:
                _day = datetime.datetime.strptime(
                    regex.findall(item['text'])[0],
                    '%d/%m/%Y'
                )
                if today >= _day:
                    dateRange = regex.findall(item['text'])
        return dateRange


def genDatesList(startDate, endDate):
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


def genWeekMenuObj(dateList, weekMenu):
    """
    Creates the object with the attributes to save in teh database.
    """
    weekObj = {}
    weekObj['menu'] = weekMenu
    weekObj['dates'] = dateList
    return weekObj


def saveMenu(filePath, datesPath='result.json'):
    """
    Saves the content of filePath to the database.
    """
    f = open(filePath, 'r')
    weekMeals = json.load(f)
    dates = getDateRange(datesPath)
    dates = genDatesList(*dates)
    obj = genWeekMenuObj(dates, weekMeals)
    collection.replace_one({'dates': dates}, obj, upsert=True)
