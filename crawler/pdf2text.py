from tika import parser
import os
import current_date


def extract_text_from_pdfs_recursively(path_to_pdf):
    path_to_txt = ""
    [stem, ext] = os.path.splitext(path_to_pdf)

    start = current_date.get_first_day_week('-')

    if ext == '.pdf':
        print("Processing " + path_to_pdf)
        pdf_contents = parser.from_file(path_to_pdf)
        path_to_txt = './downloads/' + start + '.txt'
        with open(path_to_txt, 'w') as txt_file:
            print("Writing contents to " + path_to_txt)
            txt_file.write(pdf_contents['content'])

    return path_to_txt
