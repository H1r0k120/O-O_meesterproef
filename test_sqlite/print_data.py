import sqlite3

#connect to database
conn = sqlite3.connect('lln2at.db')

#make cursor
cur = conn.cursor()

#get data
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()
