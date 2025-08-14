from PyQt5 import QtCore, QtGui, QtWidgets
from ui_question_answer_viewer import Ui_QuestionAnswerViewer
import sys

class QuestionAnswerViewer(QtWidgets.QDialog,Ui_QuestionAnswerViewer):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
    
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=QuestionAnswerViewer()
    window.show()