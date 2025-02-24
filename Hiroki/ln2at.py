import sqlite3

def get_authenticationtoken(llnum):
    try:
        with sqlite3.connect('lln2at.db') as conn:
            cur = conn.cursor()
            cur.execute('SELECT atoken FROM users WHERE lln =?', (llnum,))
            token = cur.fetchone()
            return token[0] if token else None
    except sqlite3.OperationalError as e:
        return str(e)

lln = "08099"
atoken = get_authenticationtoken(lln)
print(atoken)