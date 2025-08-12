from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys

class Main(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
    #Connections
        self.btn_loadPastPaper.clicked.connect(self.on_loadPastPaper_clicked)
        self.btn_loadMemo.clicked.connect(self.on_loadMemo_clicked)
    #Slots 
    def loadFileDialog(self,fileType):
        fname=QFileDialog.getOpenFileName(self,"Select the document","C:/","PDF Files (*.pdf)")
        #Output filename to screen 
        if (fname and fileType=="paper"):
            self.label_pastPaperFileName.setText(str(fname))
        elif (fname and fileType=="memo"):
            self.label_memoFileName.setText(str(fname))


    def on_loadMemo_clicked(self):
        print("btn_LoadMemo clicked!")
        self.loadFileDialog("memo")
    def on_loadPastPaper_clicked(self):
        print("btn_loadPastPaper clicked!")
        self.loadFileDialog("paper")


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window=Main()
    window.show()
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    sys.exit(app.exec_())