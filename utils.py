##Helper functions go in here 
import pymupdf
import re
from itertools import zip_longest

def pdf_to_text(doc): 
        text=""
        for page in doc: 
            text+=page.get_text()
        return text



def main_questions(pattern,text): 
    main_questions=re.findall(pattern,text)
    print("There are ", len(main_questions)," main questions")
    return main_questions

def sub_questions(pattern,mainqs):
    subqs=[]
    for q in mainqs:
        matches=(re.finditer(pattern,q,re.MULTILINE))
        match_list= [match.group() for match in matches]
        match_list=sanitize_list(match_list)
        subqs.append(match_list)
    print("There are ", len(subqs)," sub questions")
    return subqs

def sanitize_list(questions): #Should remove blank entries, entries with just white spaces, and all white space characters at the end of a string
    cleaned_questions=[]
    for q in questions:
        cleaned_questions.append(q.rstrip(" \n"))
        cleaned_questions=remove_empty_strings(cleaned_questions)
    return cleaned_questions

def remove_empty_strings(list):#Removes the empty strings from a list 
    full_list=[x for x in list if x]
    return full_list

def subsub_questions(pattern,list):#Splits the subquestions into further subsubquestions
    newlist=[]
    for i,q in enumerate(list):
        print("i: ",i)
        for subq in q:
            sublist=[]
            if nested_sub_check(subq):
                sublist=re.split(pattern,subq)
                sublist=sanitize_list(sublist)
            else:
                sublist=subq
            newlist.append(sublist)
    return newlist

def nested_sub_check(text):#Checks if a single sub question has a further sub question 
    pattern=r"\([0-9]\)"
    matches=(re.finditer(pattern,text,re.MULTILINE))
    match_list= [match.group() for match in matches]
    return (len(match_list)>1)

def get_questions_list(text,patterns):
     main_qs=main_questions(patterns['main_questions'],text)
     sub_qs=sub_questions(patterns['sub_questions'],main_qs)
     subsub_qs=subsub_questions(patterns['subsub_questions'],sub_qs)
     return subsub_qs

def get_answer_list(text,patterns):
    a_list=get_answers_data(text,patterns['memo_raw_text'])
    a_keys=get_answer_keys(a_list,patterns['memo_start_keys'])
    return a_keys

def get_answers_data(text,pattern):
    answer_list=re.findall(pattern,text,re.DOTALL)
    return answer_list

def get_answer_keys(answer_list,pattern):
    start_keys=[]
    for text in answer_list:
        start_key=(re.split(pattern,text))[0]
        start_keys.append(start_key)
    return start_keys 

def get_answer_rectangle_list(start_keys,doc):
    page_num=0
    rectangle_list=[]
    clip_box=None
    page=doc[page_num]
    page_width=get_page_width(page)
    page_bottom=get_page_bottom(page)
    bottom_border=None
    found_page=0 #This is to make sure that the pages are consistent 
    for key,next_key in zip_longest(start_keys,start_keys[1:],fillvalue="done!"):
        if key=="done!":
            break
        top=get_rectangle(key,page,clip_box)
        while(not top):
            page_num+=1
            page=doc[page_num]
            clip_box=None
            top=get_rectangle(key,page,clip_box)
        clip_box=make_search_area(top,page_width,page_bottom)
        found_page=page_num
        bottom=get_rectangle(next_key,page,clip_box)
        # if bottom:
        #     clip_box=make_search_area(bottom,page_width,page_bottom)
        #     bottom_border=bottom.y0
        # else:
        #     page_num+=1
        #     page=doc[page_num]
        #     clip_box=None
        #     bottom_border=page_bottom
        if (not bottom and page_num<len(doc)-1): 
            page_num+=1 
            page=doc[page_num] 
            clip_box=None 
            bottom_border=page_bottom 
        elif not page_num<len(doc):
            bottom_border=page_bottom 
            break
        elif bottom:
            clip_box=make_search_area(bottom,page_width,page_bottom)
            bottom_border=bottom.y0
        else: 
            bottom_border=page_bottom
        rect=pymupdf.Rect(top.x0,top.y0,page_width,bottom_border)
        if rect.height>10:
            rectangle_list.append((rect,found_page))
        print(found_page)
        print(len(rectangle_list))
    return rectangle_list
    
def get_page_width(page): 
    page_rect=page.rect
    return page_rect.x1

def get_page_bottom(page):
    page_rect=page.rect
    return page_rect.y1

def get_rectangle(text,page,area=None):
    rect= page.search_for(text,clip=area)
    if rect:
        return rect[0]

def make_search_area(rect,width,bottom):
    search_area=pymupdf.Rect(0,rect.y0,width,bottom)
    return search_area

def get_rectangle_list(question_texts,doc):
    page_num=0
    rectangle_list=[]
    page=doc[page_num]
    for q in question_texts:
        if type(q) is list: 
            for subq in q:
                while((get_rectangles(subq,page)==[])):
                    page_num+=1
                    page=doc[page_num]
                rect=(get_rectangles(subq,page))
                rectangle_list.append((rect,page.number))
                
        else:
                rects=get_rectangles(q,page)
                while(not rects):
                    rects=get_disjointed_rectangles(q,page)
                    if rects:
                        rects=merged_rectangle(rects)
                        break
                    page_num+=1
                    if(not page_num<len(doc)):
                       print("Not found!:\n",q)
                       break
                    page=doc[page_num]
                    rects=get_rectangles(q,page)
    
                rect=(rects)
                rectangle_list.append((rect,page.number))
                #make_clipping(page,rect,page.number)
    print(rectangle_list)
    print("We found", len(rectangle_list)," rectangles.")
    return rectangle_list

def get_rectangles(text,page):
    rectangles=page.search_for(text)
    if (len(rectangles)>1):
        rectangles=merged_rectangle(rectangles)       
    return rectangles

def merged_rectangle(rectangles): 
    # get the top left of the first rectangle 
    tl=rectangles[0].top_left
    #get the bottom right of the last rectangle 
    last_index =len(rectangles)-1
    br=rectangles[last_index].bottom_right
    #Return a new rectangle made of the previous two parts 
    merged_rect=pymupdf.Rect(tl,br)
    return merged_rect

def get_disjointed_rectangles(text,page): 
    first_and_last_list=get_first_and_last(text)
    page_blocks=get_text_blocks(page)
    rects=[]
    for needle in first_and_last_list:
        rect=get_match_blocks(needle,page_blocks)
        if rect: 
            rects.append(tuple_to_rect(rect))
        else:
            return []
    return rects

def get_first_and_last(text):
    first_and_last=[]
    split_pattern=r"\n \n"
    split_text=re.split(split_pattern,text)
    first=split_text[0]
    last=split_text[-1]
    first_and_last.extend([first,last])
    return first_and_last


def get_text_blocks(page):
    text_page=page.get_textpage()
    text_blocks=(text_page.extractBLOCKS())
    return text_blocks

def get_match_blocks(needle,text_blocks):
    match_rects=[tup[:4] for tup in text_blocks if needle in tup[-3]]
    if (len(match_rects)==1):
        return match_rects[0]
    else:
        return[]
def tuple_to_rect(tup):
    rect=[]
    if len(tup)==4:
        rect=pymupdf.Rect(tup[0],tup[1],tup[2],tup[3])
    return rect 


def get_question_starts(question_list,pattern):
    question_starts=[]
    for q in question_list:
        if type(q) is list:
            for subq in q:
                q_start=get_question_start(subq,pattern)
                question_starts.append(q_start)
        else:
            q_start=get_question_start(q,pattern)
            question_starts.append(q_start)
    print(len(question_starts))
    return question_starts

def get_question_start(question,pattern):
    return get_match(question,pattern)

def get_match(text,pattern):
    match=re.search(pattern,text,re.MULTILINE)
    match_text=match.group(0)
    return match_text 

def get_question_titles(question_list,patterns):
    q_starts=get_question_starts(question_list,patterns["question_identifiers"])
    return format_question_starts(q_starts)

def format_question_starts(question_starts):
    index=0
    tag=""
    subtag=""
    sub_subtag=""
    prev_q_start=None
    formatted_q_starts=[]
    for x,y in zip_longest(question_starts,question_starts[1:],fillvalue="end"):
        if (has_letter(x)):
            if (is_new_question(x)):
                index+=1
            tag=x 
            if (has_number(y)):
                subtag="(1)"
            elif (is_sub_subquestion(y)):
                subtag="(1)"
                sub_subtag="(i)"
            else:
                subtag=""
                sub_subtag=""
        elif (has_number(x)):
            subtag=x
            if (is_sub_subquestion(y)):
                sub_subtag="(1)"
            else:
                sub_subtag=""
        elif(is_sub_subquestion(x)):
            sub_subtag=x
        formatted_q_starts.append(get_modified_question_title(index,tag,subtag,sub_subtag))
        

    return formatted_q_starts
def has_letter(question):
    letter_pattern=r"\([a-z]\)"
    return (has_substring(question,letter_pattern))

def has_substring(string,substring): 
    match=re.search(substring,string)
    return bool(match)

def has_number(question):
    number_pattern=r"\([0-9]\)"
    return (has_substring(question,number_pattern))

def is_new_question(question): 
    pattern=r"^\(a\)"
    return(has_substring(question,pattern))

def is_sub_subquestion(question):
    pattern=r"^\(i+\)"
    return has_substring(question,pattern)

def get_modified_question_title(index,tag,subtag="",sub_subtag=""):
    mod_q_start=str(index)+tag+subtag+sub_subtag
    return mod_q_start

def get_stems(questions,pattern):#Used for getting stems 
    stems=[]
    for q in questions:
        stems.append(get_match(q,pattern))
    return stems

def get_stem_list(text,patterns):
    text_list=main_questions(text,patterns["main_questions"])
    stems_list=get_stems(text_list,patterns["question_stems"])
    return stems_list