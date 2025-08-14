from MainWindow import Ui_MainWindow
from question_answer_viewer import QuestionAnswerViewer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox
import sys

class Main(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
    #Connections
        self.btn_loadPastPaper.clicked.connect(self.on_loadPastPaper_clicked)
        self.btn_loadMemo.clicked.connect(self.on_loadMemo_clicked)
        self.btn_generateLayout.clicked.connect(self.warn_user_to_check_match)
    #Slots 
    def loadFileDialog(self,fileType):
        fname=QFileDialog.getOpenFileName(self,"Select the document","C:/","PDF Files (*.pdf)")
        #Output filename to screen 
        if (fname and fileType=="paper"):
            self.label_pastPaperFileName.setText(str(fname))
        elif (fname and fileType=="memo"):
            self.label_memoFileName.setText(str(fname))
        if self.are_both_files_loaded():
            self.btn_generateLayout.setEnabled(True)

    def on_loadMemo_clicked(self):
        print("btn_LoadMemo clicked!")
        self.loadFileDialog("memo")
    def on_loadPastPaper_clicked(self):
        print("btn_loadPastPaper clicked!")
        self.loadFileDialog("paper")
    def are_both_files_loaded(self):
        return(bool(self.label_pastPaperFileName.text() and self.label_memoFileName.text()))
    def warn_user_to_check_match(self):
        warning_box=QMessageBox(self)
        warning_box.setIcon(QMessageBox.Warning)
        warning_box.setText("Unknown issues with presentation may occur if the paper and memo do not correspond.")
        warning_box.setWindowTitle("Proceed to marking window?")
        warning_box.setStandardButtons(QMessageBox.Yes|QMessageBox.Cancel)
        warning_box.setDetailedText("Make sure that the question paper and the memo correspond.")
        warning_box.buttonClicked.connect(self.handle_warning_response)
        warning_box.exec_()
    
    def handle_warning_response(self,i):
        print(i)
        if (i.text()=="Yes"):
            self.show_layout_window()

 
    #Other Functions 
    def show_layout_window(self):
        viewer=QuestionAnswerViewer(parent=self)
        viewer.exec_()




if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window=Main()
    window.show()

    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())