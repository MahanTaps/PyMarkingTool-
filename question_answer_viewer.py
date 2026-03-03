from PyQt5 import QtCore, QtGui, QtWidgets
from ui_question_answer_viewer import Ui_QuestionAnswerViewer
from sqlitemaker2 import Sqlite3Model
import sys

class QuestionAnswerViewer(QtWidgets.QDialog,Ui_QuestionAnswerViewer):
    def __init__(self,q_filename,a_filename):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.model=Sqlite3Model(q_filename,a_filename)

    
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=QuestionAnswerViewer()
    window.show()