import sys

import pdfplumber

pdf_path="../data/advanced_invoice_sample.pdf"
print(pdf_path)

def extract_text(pdf_Fullpath):
    pdftext=""
    with pdfplumber.open(pdf_Fullpath) as pdf:
        for page in pdf.pages:
            pdftext +=page.extract_text()

    return pdftext

if __name__=="__main__":
    text=extract_text(pdf_path)
    print(text)

