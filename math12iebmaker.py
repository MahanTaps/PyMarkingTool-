from abstractrectanglemaker import AbstractRectangleMaker
import pymupdf 
import re 
from itertools import zip_longest

class Math12IEBMaker(AbstractRectangleMaker):
    def regex_separators(self):
        patterns={
            "main_questions":r"(QUESTION \d+\s+[\s\S]+?)(?=\nQUESTION \d+|\Z)",
            "sub_questions": r"(\([a-z0-9]\)\s.*[\s\S]+?)((?=^\([a-hj-z]\)|^(NATIONAL)|\Z))",
            "subsub_questions":r"(?<=\([0-9]\))(\s{3,}|$)",
            "memo_raw_text":r"\([a-z0-9]+\)[\s\S]+?(?=\n\([a-z]+\)|\s\s\n\([0-9]\)|NATIONAL|\Z)",
            "memo_start_keys":r"\s\n"
        }
        return patterns 
    #def answer_rectangles(self,memo):
    




    ###Outside functions: 
    def pdf_to_text(doc): 
        text=""
        for page in doc: 
            text+=page.get_text()
        return text
    
    def get_answer_texts():
        file="example2.pdf"
        doc=pymupdf.open(file)
        text=pdf_to_text(doc)
        pattern=
        answer_text=re.findall(pattern,text,re.DOTALL)
        return answer_text
    
