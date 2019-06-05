import pdfx
import json
import os
import pandas as pd
import re
from pdf2text import *
from datetime import datetime, timedelta
from tabula import convert_into
from text2menu import get_menu
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pdf2image import convert_from_path

DOWNLOAD_PATH = './downloads/'
OUTPUT_PATH = './outputs/'
DEFAULT_CAMPUS = 'DARCY'


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
        self.txtPath = ""

    def downloadMenu(self, campus):
        """
        Parses the pdf file to tsv.
        """
        data = self.data

        today = datetime.today().date()
        today = today + timedelta(days=1)
        today = today.strftime('%d/%m/%Y')
        dt = datetime.strptime(today, '%d/%m/%Y')
        start = dt - timedelta(days=dt.weekday())
        start = start.strftime('%d/%m/%Y')

        days = []
        fileIndex = 0

        if not os.path.exists(OUTPUT_PATH):
            os.mkdir(OUTPUT_PATH)

        for item in data.body:
            # Adds validation in 'url' field
            # to avoid errors due changes in links text
            days = item['text'].split(" ")

            if start in days:
                if campus in item['path']:
                    pdf = pdfx.PDFx(item['url'])
                    pdf.download_pdfs(DOWNLOAD_PATH)
                    name = campus + str(fileIndex)
                    fileIndex += 1
                    fileName = item['url'].split('/')
                    fileName = fileName.pop()
                    filePath = f'{DOWNLOAD_PATH}{fileName}'
                    self.txtPath = extract_text_from_pdfs_recursively(filePath)

    def genMenu(self):
        return get_menu(self.txtPath)

    def genImage(self, file_path, output_path, out_name):
        pdf = convert_from_path(file_path, 300)
        for page in pdf:
                page.save(f'{output_path}{out_name}.png', 'PNG')


def runAll():
    crawl = TheCrawler()
    crawl.runCrawler()
    p = PdfReader()
    p.downloadMenu(DEFAULT_CAMPUS)
    p.genMenu()


if __name__ == '__main__':
    runAll()
