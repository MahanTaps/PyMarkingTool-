import pandas as pd 
import os 
from retrying import retry
from dotenv import load_dotenv,find_dotenv
from promptmaker import PromptDataCompiler,PromptXmlRenderer
from spire.doc import *
from spire.doc.common import *

from google import genai
class UIExporter:
    def __init__(self,sql_table):
        self.data=sql_table
        self.excel_writer=ExcelWriter(self.data)
        self.ai_output=AIFormatter(self.data).export()
        self.word_writer=WordWriter(self.ai_output)
        self.export()

    def export(self):
        self.excel_writer.export()
        self.word_writer.export()

        


class ExcelWriter:
    def __init__(self,sql_table):
        self.data=sql_table
        self.file_name='GI Marking Sheet v1.2.3.xlsx'
        

    def prep_excel(self):
            xlx_list=[]
            for i in range(self.data.rowCount()):
                row=[]
                for j in range(5):
                    row.append(self.data.record(i).value(j))
                xlx_list.append(row)
            print("XLX List: ",xlx_list)
            return xlx_list
    
    def export_excel(self): 
            export_data=self.prep_excel()
            df2=pd.DataFrame(export_data,columns=['Question number','Section/ Taxonomy Title','Marks Scored','Marks Available','Select Error Type'])
            print("Database Frame: \n",df2)
            with pd.ExcelWriter(self.file_name,mode='a',if_sheet_exists='overlay') as writer:
                df2.to_excel(writer,sheet_name='Input Sheet',startrow=2,startcol=0,index=False,header=False)

    def export(self):
        self.prep_excel()
        self.export_excel()
        os.startfile(self.file_name)

class WordWriter:
    def __init__(self,prompt_output):
        self.filename=r"html_test.docx"
        self.result=prompt_output
        print(f"WordWriter self.result {self.result}")
        
        
    def export_to_word(self):
        document = Document()
        section = document.AddSection()
        paragraph=section.AddParagraph()
        try:
            paragraph.AppendHTML(self.result)
        except:
            paragraph.AppendHTML(f"<html>{self.result}</html>")
        document.SaveToFile(self.filename,FileFormat.Docx2016)
        document.Close()

    def open(self):
        os.startfile(self.filename)

    def export(self):
        self.export_to_word()
        self.open()



         
class AIFormatter:
    def __init__(self,sql_table):
        self.prompt=PromptXmlRenderer('prompt.xml',sql_table).make_prompt()
        self.client=genai.Client(api_key=self.get_api_key())
        

    def get_file_text(self,filename):
        with open(filename,"r",encoding="utf-8") as f:
             content=f.read()
        return content
    
    def run_prompt(self):
        response=None
        try:
            response=self.client.models.generate_content(
                        model="gemini-3.7-flash",
                        contents=self.prompt
                    )
            return(response.text)
        except Exception as e:
            print(f"ERROR: {e}")
            return e

    
    def get_api_key(self):
        env_path = find_dotenv()
        print(load_dotenv(env_path))
        API_KEY= os.getenv("MY_API_KEY")
        return API_KEY
    
    def export(self):
        return self.run_prompt_with_fallbacks(self.run_prompt)

    def models_list(self,index):
        models = [
        "gemini-3.8-flash",
        "gemini-3.7-flash",
        "gemini-3.6-flash",
        "gemini-2.5-pro",
        "gemini-3.5-flash",
        "gemini-2.5-flash",
        "gemini-3.5-flash-lite",
        "gemini-2.5-flash-lite",
        ]
        print(f"Model: {models[index]}")
        return models[index]
    
    def run_prompt(self,num_attempt):
        response=self.client.models.generate_content(
                                model=self.models_list(num_attempt),
                                contents=self.prompt
                            )
        print(response.text)
        return(response.text)

    def run_prompt_with_fallbacks(self,func):
        print("Starting retry...")
        chances=4
        attempt=0
        error=None
        while (attempt<chances):
            print("Entering loop..")
            attempt+=1
            try:
                print(f"Attempt: {attempt}")
                return(func((attempt-1)))
            except Exception as e:
                error=e
                print(show_error_msg(error,attempt))
        return show_error_msg(error,attempt)


def show_error_msg(error,attempt_num):
    return f"Error on attempt {attempt_num}: {error}"




        


