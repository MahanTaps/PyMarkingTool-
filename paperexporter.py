from screenshotter import ScreenShotter
from math12iebmaker import Math12IEBMaker
from itertools import zip_longest
import pymupdf

class PaperExporter:
    def __init__(self,q_doc,a_doc):
        self.rectmaker=Math12IEBMaker(q_doc,a_doc)
        self.rect_locations=self.rectmaker.export_rectangles()
        self.screenshotter=ScreenShotter(q_doc,a_doc,self.rect_locations)
        self.img_locations=self.screenshotter.batch_filenames
        print(self.img_locations)
    
    def make_item(self,val1,val2,val3,val4):
        keys=['q_num','sect','scored','avail','error','lost','q_location','q_stem','answer']
        vals=[val1,None,None,None,None,None,val2,val3,val4]
        return {k:v for (k,v) in zip(keys,vals)}

    def prep_export(self):
        titles = self.rect_locations['q_titles']
        q_locations=self.img_locations['q_pics']
        qstem_locations=self.img_locations['stem_pics']
        a_locations=self.img_locations['a_pics']
        paper_data=[]
        for a,b,c,d in zip_longest(titles,q_locations,qstem_locations,a_locations):
            paper_data.append(self.make_item(a,b,c,d))
        return paper_data

            
    



