import sqlite3


#connect to database
conn = sqlite3.connect('lln2at.db')

#make cursor
cur = conn.cursor()

#insert data
cur.execute("DELETE FROM users WHERE id = 2")

#commit and save changes
conn.commit()