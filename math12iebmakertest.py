from abstractrectanglemaker import AbstractRectangleMaker
from math12iebmaker  import Math12IEBMaker

if __name__=="__main__":
    q_filename="examplepdfs\example.pdf"
    a_filename="examplepdfs\example2.pdf"
    maker=Math12IEBMaker(q_filename,a_filename)
    print(maker.export_rectangles())