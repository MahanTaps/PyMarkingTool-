import pandas as pd 
import os 
from dotenv import load_dotenv,find_dotenv
from promptmaker import PromptDataCompiler,PromptXmlRenderer

from google import genai
class UIExporter:
    def __init__(self,sql_table):
        self.data=sql_table
        self.excel_writer=ExcelWriter(sql_table)
        #self.ai_service=



class ExcelWriter:
    def __init__(self,sql_table):
        self.data=sql_table
        self.prep_excel()
        self.export_excel()
        os.startfile('GI Marking Sheet v1.2.3.xlsx')

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
            with pd.ExcelWriter('GI Marking Sheet v1.2.3.xlsx',mode='a',if_sheet_exists='overlay') as writer:
                df2.to_excel(writer,sheet_name='Input Sheet',startrow=2,startcol=0,index=False,header=False)

class WordWriter:
    def __init__(self):
        pass
    def write_to_word(self,data):
         return None
         
class AIFormatter:
    def __init__(self,prompt_data):
        self.prompt=self.get_file_text(prompt_data)
        self.client=genai.Client(api_key=self.get_api_key())

    def get_file_text(self,filename):
        with open(filename,"r",encoding="utf-8") as f:
             content=f.read()
        return content
    
    def run_prompt(self):
        response=self.client.models.generate_content(
            model="gemini-3.7-flash",
            contents=self.prompt
        )
        return response.text
    
    def get_api_key(self):
        env_path = find_dotenv()
        print(load_dotenv(env_path))
        API_KEY= os.getenv("MY_API_KEY")
        return API_KEY

        


