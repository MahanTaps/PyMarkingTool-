from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from ui_question_answer_viewer import Ui_QuestionAnswerViewer
from sqlitemaker2 import Sqlite3Model
from PyQt5.QtCore import QTimer
import os.path
import sys

class QuestionAnswerViewer(QtWidgets.QDialog,Ui_QuestionAnswerViewer):
    def __init__(self,q_filename,a_filename):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.model=Sqlite3Model(q_filename,a_filename).model
        self.currentIndex=0
        self.initialize_viewer()
        self.model_row_count=self.model.rowCount()
        self.questionImageLabel.setScaledContents(True)
        self.answerImageLabel.setScaledContents(True)
        self.stemImageLabel.setScaledContents(True)
        #Timer setup
        self.timer=QTimer()
        self.timer.setSingleShot(True)
        #Connections
        self.nextToolButton.clicked.connect(self.btn_nextButton_clicked)
        self.prevToolButton.clicked.connect(self.btn_prevButton_clicked)
        #Connections for the save button 
        self.sectionComboBox.currentIndexChanged.connect(self.start_timer)
        self.marksScoredEdit.textChanged.connect(self.start_timer)
        self.marksAvailableEdit.textChanged.connect(self.start_timer)
        self.errorComboBox.currentIndexChanged.connect(self.start_timer)
        self.commentsEdit.textChanged.connect(self.start_timer)
        self.timer.timeout.connect(self.fields_changed)
        self.saveButton.clicked.connect(self.btn_saveButton_clicked)


    def initialize_viewer(self):
        self.set_question_title(self.questionLabel, self.model.record(0).value(0))
        self.saveButton.setEnabled(False)
        self.questionImageLabel.setPixmap(self.make_pixmap(0,"q"))
        self.answerImageLabel.setPixmap(self.make_pixmap(0,"a"))
        self.stemImageLabel.setPixmap(self.make_pixmap(0,"s"))

    
    def update_viewer(self,currentIndex):
        self.set_question_title(self.questionLabel, self.model.record(currentIndex).value(0))
        self.sectionComboBox.setCurrentText(self.model.record(currentIndex).value('sect'))
        self.marksScoredEdit.setText(str(self.model.record(currentIndex).value('scored')))
        self.marksAvailableEdit.setText(str(self.model.record(currentIndex).value('avail')))
        self.errorComboBox.setCurrentText(self.model.record(currentIndex).value('error'))
        self.commentsEdit.setPlainText(self.model.record(currentIndex).value('comment'))
        self.questionImageLabel.setPixmap(self.make_pixmap(currentIndex,"q"))
        self.answerImageLabel.setPixmap(self.make_pixmap(currentIndex,"a"))
        self.stemImageLabel.setPixmap(self.make_pixmap(currentIndex,"s"))
        self.stop_timer()
        print("Viewer Updated!")

    def switch_tool_buttons(self,on_or_off):
        val=None
        if on_or_off=="on":
            val=True
        elif on_or_off=="off":
            val=False
        self.nextToolButton.setEnabled(val)
        self.prevToolButton.setEnabled(val)



    def make_pixmap(self,currentIndex,key):
        pixmap=None
        if key == "q":
            fname=self.model.record(currentIndex).value(6)
            pixmap=QPixmap(fname)
        elif key=="s":
            fname=self.model.record(currentIndex).value(7)
            pixmap=QPixmap(fname)
        elif key=="a":
            fname=self.model.record(currentIndex).value(8)
            pixmap=QPixmap(fname)
        return pixmap


    
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
    
    def btn_saveButton_clicked(self):
        self.update_db()
        self.saveButton.setEnabled(False)
        self.switch_tool_buttons("on")


    def update_db(self):
        record=self.model.record(self.currentIndex)
        record.setValue('comment',self.commentsEdit.toPlainText())
        record.setValue("avail",self.marksAvailableEdit.text())
        record.setValue("scored",self.marksScoredEdit.text())
        record.setValue("error",self.errorComboBox.currentText())
        record.setValue("sect",self.sectionComboBox.currentText())
        self.model.setRecord(self.currentIndex,record)
        self.model.submitAll()
        

    def fields_changed(self):
        print("Fields changed!")
        if (not self.saveButton.isEnabled()):
            self.saveButton.setEnabled(True)
            self.switch_tool_buttons("off")

    def set_question_title(self,label,text):
        label.setText("Question: "+text)
    
    def start_timer(self):
        print("Timer started!")
        self.timer.start(2000)
    
    def stop_timer(self):
        print("Timer stopped!")
        self.timer.stop()


if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=QuestionAnswerViewer()
    window.show()