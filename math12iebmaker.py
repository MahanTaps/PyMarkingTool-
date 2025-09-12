from abstractrectanglemaker import AbstractRectangleMaker
import pymupdf 
import re 
from itertools import zip_longest
import utils

class Math12IEBMaker(AbstractRectangleMaker):
    def __init__(self,q_filename,a_filename,q_doc,a_doc,raw_text):
        self.q_doc=pymupdf.open(q_filename)
        self.a_doc=pymupdf.open(a_filename)
        self.raw_text[0]= utils.pdf_to_text(q_doc)
        self.raw_text[1]=utils.pdf_to_text(a_doc)
        self.q_list=[]
    
    def raw_text(self):
        return self.raw_text

    def regex_separators(self):
        patterns={
            "main_questions":r"(QUESTION \d+\s+[\s\S]+?)(?=\nQUESTION \d+|\Z)",
            "sub_questions": r"(\([a-z0-9]\)\s.*[\s\S]+?)((?=^\([a-hj-z]\)|^(NATIONAL)|\Z))",
            "subsub_questions":r"(?<=\([0-9]\))(\s{3,}|$)",
            "question_identifiers":r"^\([a-z]{,3}\)\s|^\([0-9]\)\s",
            "memo_raw_text":r"\([a-z0-9]+\)[\s\S]+?(?=\n\([a-z]+\)|\s\s\n\([0-9]\)|NATIONAL|\Z)",
            "memo_start_keys":r"\s\n"
        }
        return patterns 
    
    def question_rectangles(self):
        self.q_list=utils.get_questions_list((self.raw_text())[0],self.regex_separators())
        q_rects=utils.get_rectangle_list(self.q_list,self.q_doc)
        return q_rects
        
    def answer_rectangles(self):
        a_list=utils.get_answer_list(self.raw_text[1],(self.regex_separators()))
        a_rects=utils.get_answer_rectangle_list(a_list,self.a_doc)
        return a_rects
    
    def question_titles(self):
        q_titles=utils.get_question_titles(self.q_list,self.regex_separators())
        return q_titles
    
    def question_stem_rectangles(self):
    #use get_stems to get the list, then pass it to the rectangles function to get the rects. 
    ###Outside functions: 
    

    
