import pandas as pd 
import os 
class UIExporter: 
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


