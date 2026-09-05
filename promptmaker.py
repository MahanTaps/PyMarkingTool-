from xml.etree import ElementTree as et
import pandas as pd 

class PromptDataCompiler:
    def __init__(self,sql_table):
        self.data=sql_table

    def prep_json(self):
        json_list=[]
        for i in range(self.data.rowCount()):
            row=[]
            for j in range(self.data.record(i).count()):
                if j==5 or j==6 or j==7 or j==8:
                    continue
                else:
                    row.append(self.data.record(i).value(j))
            json_list.append(row)
        print("json List: ",json_list)
        return json_list

    def make_dict(self,data):
        empty_dict={'Question number':[],'Section/ Taxonomy Title':[],'Marks Scored':[],'Marks Available':[],'Error Type':[],'Comments':[],'Question Text':[]}
        for row in data:
            i=0
            for x in empty_dict:
                empty_dict[x].append(row[i])
                i+=1
        return(empty_dict)

    def make_json_array(self):
        export_data=self.make_dict(self.prep_json())
        df=pd.DataFrame(export_data)
        return(df.to_json(orient='records'))

class PromptXmlRenderer:
    def __init__(self,xml_file,json_data):
        self.file=xml_file
        self.data=json_data
        self.tree=self.set_tree()
        self.root=self.set_root()

    def set_tree(self):
        tree=et.parse(self.file)
        return tree

    def set_root(self):
        root=self.tree.getroot()
        return root

    def insert_performance_data(self):
        #finding input data
        input=self.root.find('input_data')
        #performance
        performance=input.find('performance_data')
        performance.text=self.data
        self.tree.write(self.file)

    def make_prompt(self):
        self.insert_performance_data()
        f=open(self.file,"r")
        return(f.read())