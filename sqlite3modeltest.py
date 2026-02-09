import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication,QTableView

app = QApplication(sys.argv)
db= QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("test.db")
if(db.open()):
    print("Yeah!")
else:
    print("Nah..")
model= QSqlTableModel(None,db)
model.setTable("question")
model.select() #populate table with data 
print("Record:",model.record(0).value('answer'))
table_view=QTableView()
table_view.setModel(model)
sys.exit(app.exec())
print('Current Index:',table_view.currentIndex())
#It seems like there's an infinite loop going on? Maybe I need to set the index first