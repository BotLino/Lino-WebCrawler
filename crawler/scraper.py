import pdfx
import json
import os
import pandas as pd
import re
from pdf2text import *
from tabula import convert_into
import current_date
from text2menu import get_menu
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pdf2image import convert_from_path
import logging

logger = logging.getLogger(__name__)


DOWNLOAD_PATH = './downloads/'
OUTPUT_PATH = './outputs/'
DEFAULT_CAMPUS = 'darcy'


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
        self.txt_path = ""

    def download_menu(self, campus):
        data = self.data

        start = current_date.get_first_day_week('/')

        days = []
        file_index = 0

        if not os.path.exists(OUTPUT_PATH):
            os.mkdir(OUTPUT_PATH)

        for item in data.body:
            # Adds validation in 'url' field
            # to avoid errors due changes in links text
            days = item['text'].split(" ")

            if start in days:
                pdf = pdfx.PDFx(item['url'])
                pdf.download_pdfs(DOWNLOAD_PATH)
                name = campus + str(file_index)
                file_index += 1
                file_name = item['url'].split('/')
                file_name = file_name.pop()
                file_path = f'{DOWNLOAD_PATH}{file_name}'
                self.txt_path = extract_text_from_pdfs_recursively(file_path)
                break

    def gen_menu(self):
        return get_menu()

    def gen_image(self, file_path, output_path, out_name):
        pdf = convert_from_path(file_path, 300)
        for page in pdf:
                page.save(f'{output_path}{out_name}.png', 'PNG')


def run_all():
    crawl = TheCrawler()
    crawl.runCrawler()
    p = PdfReader()
    p.download_menu(DEFAULT_CAMPUS)
    p.gen_menu()


if __name__ == '__main__':
    run_all()
