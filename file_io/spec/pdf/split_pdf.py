# encoding=utf-8
from Py2 import PdfFileWriter, PdfFileReader


def pdf_split(pdf_in, pdf_out, start, end):
    output = PdfFileWriter()
    # 读取pdf
    with open(pdf_in, 'rb') as in_pdf:
        pdf_file = PdfFileReader(in_pdf)

        for i in range(start-1, end):
            output.addPage(pdf_file.getPage(i))

        with open(pdf_out, 'ab') as f:
            output.write(f)


if __name__ == '__main__':
    pdf_in = './book.pdf'
    pdf_out = './book_split.pdf'
    s, e = 197, 245  # 拆分的起始位置和结束位置
    pdf_split(pdf_in, pdf_out, s, e)
