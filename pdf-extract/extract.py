#!/usr/bin/env python3

import pdfplumber


if __name__ == '__main__':
    pdf = pdfplumber.open("path/to/my.pdf")
    page = pdf.pages[0]
    print(page.extract_table())
