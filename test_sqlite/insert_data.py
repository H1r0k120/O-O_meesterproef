import sqlite3


#connect to database
conn = sqlite3.connect('lln2at.db')

#make cursor
cur = conn.cursor()

#make table
cur.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    lln TEXT,
    atoken TEXT)''')

#insert data
cur.execute("INSERT INTO users (lln, atoken) VALUES (?, ?)", ('08078', '8jcm5uhbpn9nogsl7kcickuaq1'))

#commit and save changes
conn.commit()