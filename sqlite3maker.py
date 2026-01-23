import sqlite3
class Sqlite3Model:
    def __init__(self):
        self.con= sqlite3.connect("test.db") #create db in memory and connect to it
        print(self.con)
        self.cur=self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("CREATE TABLE question(q_num TEXT, sect TEXT, scored INT,avail INT, error INT, lost INT,q_location TEXT,q_stem TEXT,answer TEXT,comment TEXT)")

    def insert_row(self,row_item):
        self.cur.execute("INSERT INTO question VALUES(:q_num, :sect, :scored, :avail, :error, :lost, :q_location, :q_stem, :answer, :comment)",row_item)
        self.con.commit()

    def insert_rows(self,row_items):
        for row in row_items: 
            self.insert_row(row)