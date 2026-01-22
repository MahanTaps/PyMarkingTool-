import sqlite3
def __init__(self,paper_dict):
    self.con= sqlite3.connect("test.db") #create db in memory and connect to it
    self.cur=self.con.cursor()

def create_table(self):
    self.cur.execute("CREATE TABLE question(q_num TEXT, sect TEXT, scored INT,avail INT, error INT, lost INT,q_location TEXT,q_stem TEXT,answer TEXT,comment TEXT)")

def insert_row(self,row_item):
    self.cur.execute("INSERT INTO question VALUES(:q_num, :sect, :scored, :avail, :error, :lost, :q_location, :q_stem, :answer, :comment)",row_item)
    self.con.commit()
