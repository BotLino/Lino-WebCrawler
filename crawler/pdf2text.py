from tika import parser
import os


def extract_text_from_pdfs_recursively(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path_to_pdf = os.path.join(root, file)
            [stem, ext] = os.path.splitext(path_to_pdf)
            if ext == '.pdf':
                print("Processing " + path_to_pdf)
                pdf_contents = parser.from_file(path_to_pdf)
                path_to_txt = stem + '.txt'
                with open(path_to_txt, 'w') as txt_file:
                    print("Writing contents to " + path_to_txt)
                    txt_file.write(pdf_contents['content'])


if __name__ == "__main__":
    extract_text_from_pdfs_recursively(os.getcwd())


def creates_table():
    file = open("teste.txt", 'r')
    stringzona = ""
    for line in file:
        stringzona.append(line)
