import sqlite3
con= sqlite3.connect(":memory:") #create db in memory and connect to it
cur=con.cursor()
cur.execute("CREATE TABLE question(title TEXT, section TEXT, scored INT,avail INT, error INT, lost INT,q_location TEXT,q_stem TEXT,answer TEXT,comment TEXT)")
res= cur.execute("SELECT name FROM sqlite_master")
question1={'q_num': '1(a) (1)', 'sect': None, 'scored': None, 'avail': None, 'error': None, 'lost': None, 'q_location': 'Questions\\Question 0.png', 'q_stem': None, 'answer': 'Answers\\Question 0.png', 'comment': None}
cur.execute("INSERT INTO question VALUES(:q_num, :sect, :scored, :avail, :error, :lost, :q_location, :q_stem, :answer, :comment)")
con.commit()
cur.execute('SELECT * FROM question')
print(res.fetchone())