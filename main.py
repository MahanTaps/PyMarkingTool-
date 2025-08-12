from MainWindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys

class Main(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
    #Slots 
    def loadFileDialog(self):
        fname=QFileDialog.getOpenFileName(self,"Select the document","C:/","PDF (*.pdf)")
        
    def on_loadMemo_clicked(self):
        print("btn_LoadMemo clicked!")
    def on_loadPastPaper_clicked(self):
        print("btn_loadPastPaper clicked!")
        self.loadFileDialog()
        print(self.loadFileDialog())
    #Connections
        self.btn_loadPastPaper.clicked.connect(self.on_loadPastPaper_clicked)
        self.btn_loadMemo.clicked.connect(self.on_loadMemo_clicked)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())