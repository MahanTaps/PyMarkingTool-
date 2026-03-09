from PyQt5 import QtCore, QtGui, QtWidgets
from ui_question_answer_viewer import Ui_QuestionAnswerViewer
from sqlitemaker2 import Sqlite3Model
import sys

class QuestionAnswerViewer(QtWidgets.QDialog,Ui_QuestionAnswerViewer):
    def __init__(self,q_filename,a_filename):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.model=Sqlite3Model(q_filename,a_filename).model
        self.currentIndex=0
        self.initialize_viewer()
        self.model_row_count=self.model.rowCount()
        #Connections
        self.nextToolButton.clicked.connect(self.btn_nextButton_clicked)
        self.prevToolButton.clicked.connect(self.btn_prevButton_clicked)

    def initialize_viewer(self):
        self.set_question_title(self.questionLabel, self.model.record(0).value(0))
    
    def update_viewer(self,currentIndex):
        self.set_question_title(self.questionLabel, self.model.record(currentIndex).value(0))


    #Slots 
    def btn_nextButton_clicked(self):
        print(self.currentIndex)
        if (self.currentIndex<self.model_row_count-1):
            self.currentIndex+=1
        self.update_viewer(self.currentIndex)
    
    def btn_prevButton_clicked(self):
        print(self.currentIndex)
        if(self.currentIndex>0):
            self.currentIndex-=1
        self.update_viewer(self.currentIndex)

    def set_question_title(self,label,text):
        label.setText("Question: "+text)


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=QuestionAnswerViewer()
    window.show()