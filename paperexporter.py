from screenshotter import ScreenShotter
from math12iebmaker import Math12IEBMaker
import pymupdf

class PaperExporter:
    def __init__(self,q_doc,a_doc):
        self.rectmaker=Math12IEBMaker(q_doc,a_doc)
        self.rect_locations=self.rectmaker.export_rectangles()
        self.screenshotter=ScreenShotter(q_doc,a_doc,self.rect_locations)
        self.img_locations=self.screenshotter.batch_filenames
        print(self.img_locations)