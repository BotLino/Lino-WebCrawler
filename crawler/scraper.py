import pdfx
import json
import os
import pandas as pd
import re
from datetime import datetime
from tabula import convert_into
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

DOWNLOAD_PATH = './downloads/'
OUTPUT_PATH = './outputs/'
DEFAULT_CAMPUS = 'FGA'
DEFAULT_FILE_NAME = 'FGA0'


class TheCrawler():
    def __init__(self):
        self.process = CrawlerProcess(get_project_settings())

    def runCrawler(self):
        self.process.crawl('RU')
        self.process.start()


class JsonReader():
    def __init__(self):
        with open('result.json') as f:
            self.body = json.load(f)


class PdfReader():
    def __init__(self):
        self.data = JsonReader()

    def downloadMenu(self, campus):
        """
        Parses the pdf file to tsv.
        """
        data = self.data
        fileIndex = 0
        if not os.path.exists(OUTPUT_PATH):
            os.mkdir(OUTPUT_PATH)
        for item in data.body:
            if campus in item['text']:
                pdf = pdfx.PDFx(item['url'])
                pdf.download_pdfs(DOWNLOAD_PATH)
                name = campus + str(fileIndex)
                fileIndex += 1
                fileName = item['url'].split('/')
                fileName = fileName.pop()
                convert_into(
                    f'{DOWNLOAD_PATH}{fileName}',
                    f'{OUTPUT_PATH}{name}.tsv',
                    output_format='tsv')

    def genQuery(self, sheet):
        """
        Get a Data Frame with the RU menu,
        and generates a query dictionary by merging related columns.
        """
        columns = list(sheet.columns.values)
        queryList = {}
        queryList['legenda'] = sheet[columns[0]]
        queryList['Monday'] = sheet[columns[1]] + sheet[columns[2]]
        queryList['Tuesday'] = sheet[columns[3]] + sheet[columns[4]]
        queryList['Wednesday'] = sheet[columns[5]] + sheet[columns[6]]
        queryList['Thursday'] = sheet[columns[7]]
        queryList['Friday'] = sheet[columns[8]] + sheet[columns[9]]
        queryList['Saturday'] = sheet[columns[10]] + sheet[columns[11]]
        queryList['Sunday'] = sheet[columns[12]] + sheet[columns[13]]
        return queryList

    def getTodayFile(self):
        """
        Returns the fileName according to the current week.
        """
        data = self.data
        today = datetime.now()
        regex = re.compile(r'(?P<date>\d{2}/\d{2}/\d{4})')
        fileIndex = 0
        if len(data.body) > 3:
            for item in data.body:
                if 'FGA' in item['text']:
                    _day = datetime.strptime(
                        regex.findall(item['text'])[0],
                        '%d/%m/%Y'
                    )
                    if today >= _day:
                        fileIndex += 1
        if fileIndex > 0:
            fileName = DEFAULT_CAMPUS + str(fileIndex-1)
        else:
            fileName = DEFAULT_FILE_NAME
        return fileName

    def getDayMenu(self, day):
        """
        Return the menu for an specified day.
        """
        fileName = self.getTodayFile()
        filePath = OUTPUT_PATH + fileName + '.tsv'
        sheet = pd.read_table(
            f'{filePath}',
            sep='\t',
            na_filter=False,
            header=1,
            skipfooter=3,
            dayfirst=True,
            parse_dates=True,
            engine='python')
        query = self.genQuery(sheet)
        return(query[day])

    def getWeekMenu(self):
        """
        Generate a json file with all the week meals.
        And returns the week meals.
        """
        weekMeals = {}
        weekMeals['Monday'] = {}
        weekMeals['Tuesday'] = {}
        weekMeals['Wednesday'] = {}
        weekMeals['Thursday'] = {}
        weekMeals['Friday'] = {}

        for i in weekMeals:
            weekMeals[i] = self.genJson(i)
        f = open('weekMenu.json', 'w')
        f.write(json.dumps(weekMeals, indent=4, ensure_ascii=False))
        f.close()
        return weekMeals

    def genJson(self, day):
        """
        Generates the menu and saves the json.
        """
        leg = self.getDayMenu('legenda')
        data = self.getDayMenu(day)
        rows = list(data.index.values)
        menu = {}
        menu['DESJEJUM'] = {}
        menu['ALMOÇO'] = {}
        menu['JANTAR'] = {}
        for item in rows:
            leg[item] = leg[item].replace('.', '')
            if leg[item] == 'DESJEJUM':
                flag = leg[item]
                continue
            elif leg[item] == 'ALMOÇO':
                flag = leg[item]
                continue
            elif leg[item] == 'JANTAR':
                flag = leg[item]
                continue
            elif leg[item] == '':
                leg[item] = 'Pão:'
                menu[flag][leg[item]] = data[item]
            else:
                menu[flag][leg[item]] = data[item]
        return menu


def runAll():
    crawl = TheCrawler()
    crawl.runCrawler()
    p = PdfReader()
    p.downloadMenu(DEFAULT_CAMPUS)
    p.getWeekMenu()


if __name__ == '__main__':
    runAll()
