import sqlite3
from paperexporter import PaperExporter
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import *
from PyQt5.QtWidgets import QApplication,QTableView

class Sqlite3Model:
    def __init__(self,q_file,memo_file):
        self.con= sqlite3.connect("test.db") #create db in memory and connect to it
        print(self.con)
        self.cur=self.con.cursor()
        self.create_table()
        exporter=PaperExporter(q_file,memo_file)
        data=exporter.do_export()
        self.insert_rows(data)
        db= QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("test.db")
        if(db.open()):
            print("Yeah!")
        else:
            print("Nah..")

    def create_table(self):
        self.cur.execute("CREATE TABLE question(q_num TEXT, sect TEXT, scored INT,avail INT, error INT, lost INT,q_location TEXT,q_stem TEXT,answer TEXT,comment TEXT)")

    def insert_row(self,row_item):
        self.cur.execute("INSERT INTO question VALUES(:q_num, :sect, :scored, :avail, :error, :lost, :q_location, :q_stem, :answer, :comment)",row_item)
        self.con.commit()

    def insert_rows(self,row_items):
        for row in row_items: 
            self.insert_row(row)
    
    def create_model(self,db):
        model= QSqlTableModel(None,db)
        model.setTable("question")
        model.select() #populate table with data 

        