import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *


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