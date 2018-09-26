import scrapy
import pdfx
import json
import os
import argparse
import pandas as pd
from pprint import pprint
from tabula import convert_into
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

DOWNLOAD_PATH = './downloads/'
OUTPUT_PATH = './outputs/'

class TheCrawler():
    def __init__(self):
        self.process = CrawlerProcess(get_project_settings())

    def runCrawler(self):
        self.process.crawl('RU')
        self.process.start()  # the script will block here until the crawling is finished

class JsonReader():
    def __init__(self):
        with open('result.json') as f:
            self.body = json.load(f)

class PdfReader():
    def __init__(self):
        self.data = JsonReader()
    
    def downloadMenu(self, campus):
        data = self.data
        n = 0
        if not os.path.exists(OUTPUT_PATH):
            os.mkdir(OUTPUT_PATH)
        for item in data.body:
            if campus in item['text']:
                pdf = pdfx.PDFx(item['url'])
                pdf.download_pdfs(DOWNLOAD_PATH)
                name = campus + str(n)
                n += 1
                fileName = item['url'].split('/')
                fileName = fileName.pop()
                convert_into(
                    f'{DOWNLOAD_PATH}{fileName}',
                    f'{OUTPUT_PATH}{name}.tsv',
                    output_format='tsv')

    def genQuerry(self, df):
        cols = list(df.columns.values)
        q = {}
        q['legenda'] = df[cols[0]]
        q['Monday'] = df[cols[1]] + df[cols[2]]
        q['Tuesday'] = df[cols[3]] + df[cols[4]]
        q['Wednesday'] = df[cols[5]] + df[cols[6]]
        q['Thursday'] = df[cols[7]]
        q['Friday'] = df[cols[8]] + df[cols[9]]
        q['Saturday'] = df[cols[10]] + df[cols[11]]
        q['Sunday'] = df[cols[12]] + df[cols[13]]
        return q

    def getDayMenu(self, fileName, day):
        df = pd.read_table(
            f'{OUTPUT_PATH}{fileName}.tsv',
            sep='\t',
            na_filter=False,
            header=1,
            skipfooter=3,
            dayfirst=True,
            parse_dates=True,
            engine='python')
        q = self.genQuerry(df)
        return(q[day])

    def getWeekMenu(self, fileName):
        df = pd.read_table(
            f'{OUTPUT_PATH}{fileName}.tsv',
            sep='\t',
            na_filter=False,
            header=1,
            skipfooter=3,
            dayfirst=True,
            parse_dates=True,
            engine='python')
        q = self.genQuerry(df)

        week = [('Monday','Segunda'),('Tuesday','Terça'),('Wednesday','Quarta'),('Thursday','Quinta'),('Friday','Sexta')]
        obj = {}
        obj['Segunda'] = {}
        obj['Terça'] = {}
        obj['Quarta'] = {}
        obj['Quinta'] = {}
        obj['Sexta'] = {}

        for i,j in week:
            obj[j] = self.genJson(i)
        pprint(obj)
        f = open('weekMenu.json','w')
        f.write(json.dumps(obj, indent=4, ensure_ascii=False))
        f.close()
        
        return obj

    def genMealJson(self, day):
        
        obj = self.genJson(day)
        f = open('desjejumMenu.json','w')
        f.write(json.dumps(obj['DESJEJUM'], indent=4, ensure_ascii=False))
        f.close()
        f = open('almocoMenu.json','w')
        f.write(json.dumps(obj['ALMOÇO'], indent=4, ensure_ascii=False))
        f.close()
        f = open('jantarMenu.json','w')
        f.write(json.dumps(obj['JANTAR'], indent=4, ensure_ascii=False))
        f.close()

    def genJson(self, day):
        leg = self.getDayMenu('FGA0','legenda')
        data = self.getDayMenu('FGA0', day)
        rows = list(data.index.values)
        obj = {}
        obj['DESJEJUM'] = {}
        obj['ALMOÇO'] = {}
        obj['JANTAR'] = {}
        for item in rows:
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
                obj[flag][leg[item]] = data[item]
            else:
                obj[flag][leg[item]] = data[item]
        f = open('menu.json','w')
        f.write(json.dumps(obj, indent=4, ensure_ascii=False))
        f.close()
        return obj 

parser = argparse.ArgumentParser("Scraper")
parser.add_argument('-d','--day', help='Search for a specific week day')
parser.add_argument('-s','--save', help='Download the files and generates new result.json')
parser.add_argument('-a','--all', help='Run the complete pipeline (Requires -d value)', action='store_true')
parser.add_argument('-w','--week', help='Search for a week',action='store_true')
parser.add_argument('-r','--refeicao', help='Search for a meal')

args = parser.parse_args()

if args.all and args.day:
    crawl = TheCrawler()
    crawl.runCrawler()
    p = PdfReader()
    p.downloadMenu('FGA')
    p.genJson(args.day)
elif args.all and args.day and args.refeicao:
    crawl = TheCrawler()
    crawl.runCrawler()
    p = PdfReader()
    p.downloadMenu('FGA')
    if args.refeicao == 'Desjejum':
        p.genMealJson(args.day)
    elif args.refeicao == 'Almoco':
        p.genMealJson(args.day)
    elif args.refeicao == 'Jantar':
        p.genMealJson(args.day)
elif args.all and args.week:
    crawl = TheCrawler()
    crawl.runCrawler()
    p = PdfReader()
    p.downloadMenu('FGA')
    p.getWeekMenu('FGA0')
elif args.all:
    raise ValueError('-a must have -d value')
elif args.day:
    p = PdfReader()
    p.genJson(args.day)
elif args.save:
    crawl = TheCrawler()
    crawl.runCrawler()
    p = PdfReader()
    p.downloadMenu('FGA')
elif args.week:
    p = PdfReader()
    p.getWeekMenu('FGA0')
else:
    crawl = TheCrawler()
    crawl.runCrawler()
    p = PdfReader()
    p.downloadMenu('FGA')
    p = PdfReader()