from tika import parser
from datetime import datetime, timedelta
import os


def get_first_day_week(self):
    today = datetime.today().date()
    today = today + timedelta(days=1)
    today = today.strftime('%d/%m/%Y')
    dt = datetime.strptime(today, '%d/%m/%Y')
    start = dt - timedelta(days=dt.weekday())
    start = start.strftime('%d-%m-%Y')

    return start


def extract_text_from_pdfs_recursively(path_to_pdf):
    path_to_txt = ""
    [stem, ext] = os.path.splitext(path_to_pdf)

    start = get_first_day_week()

    if ext == '.pdf':
        print("Processing " + path_to_pdf)
        pdf_contents = parser.from_file(path_to_pdf)
        path_to_txt = './downloads/' + start + '.txt'
        with open(path_to_txt, 'w') as txt_file:
            print("Writing contents to " + path_to_txt)
            txt_file.write(pdf_contents['content'])

    return path_to_txt
