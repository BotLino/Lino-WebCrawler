import datetime
import re
import json
from pymongo import MongoClient

client = MongoClient('localhost', 27008)
db = client.ru
collection = db.menu


f = open('weekMenu.json', 'r')
weekMeals = json.load(f)


def getDateRange():
        """
        Returns the fileName according to the current week.
        """
        with open('result.json') as f:
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
    allDates = []
    startDate = datetime.datetime.strptime(startDate, '%d/%m/%Y')
    endDate = datetime.datetime.strptime(endDate, '%d/%m/%Y')
    step = datetime.timedelta(days=1)
    while startDate <= endDate:
        allDates.append(startDate.strftime('%d/%m/%Y'))
        startDate += step
    return allDates


def genWeekMenuObj(dateList, weekMenu):
    weekObj = {}
    weekObj['menu'] = weekMenu
    weekObj['dates'] = dateList
    return weekObj


dates = getDateRange()
dates = genDatesList(*dates)
obj = genWeekMenuObj(dates, weekMeals)
collection.replace_one({'dates': dates}, obj, upsert=True)
