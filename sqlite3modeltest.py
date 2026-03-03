import sqlite3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication,QTableView

#Setting up database 
app = QApplication(sys.argv)
db= QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("test.db")
if(db.open()):
    print("Yeah!")
else:
    print("Nah..")
#Setting up model 
model= QSqlTableModel(None,db)
model.setTable("question")
model.select() #populate table with data 
print("Record:",model.record(1).value("answer"))
table_view=QTableView()
table_view.setModel(model)
print("Table view set up!")
print("Setting Index...")
#Try to create a QModelIndex item here and pass it to rootIndex 19/02/2026 
table_view.setRootIndex(model.index(0,0))
table_view.setCurrentIndex(model.index(0,6))
print('Current Index:',table_view.currentIndex().isValid())
print('Checking Data:',model.data(table_view.currentIndex()))
print('Row Count:',model.rowCount())
#sys.exit(app.exec())

#Selecting a row 
