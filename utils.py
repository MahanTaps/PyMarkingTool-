##Helper functions go in here 
import pymupdf
import re

def pdf_to_text(doc): 
        text=""
        for page in doc: 
            text+=page.get_text()
        return text

def get_answer_texts(pattern):
        file="example2.pdf"
        doc=pymupdf.open(file)
        text=pdf_to_text(doc)
        answer_text=re.findall(pattern,text,re.DOTALL)
        return answer_text

