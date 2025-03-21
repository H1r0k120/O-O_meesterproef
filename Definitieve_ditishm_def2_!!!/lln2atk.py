import sqlite3

def get_authenticationtoken(lln):
    try:
        with sqlite3.connect('lln2at.db') as conn:
            cur = conn.cursor()
            cur.execute('SELECT atoken FROM users WHERE lln =?', (lln,))
            atoken = cur.fetchone()
            #atoken = "nrodnludj19gqmdtehi3ueiufm"
            return atoken[0] if atoken else None
    except sqlite3.OperationalError as e:
        return str(e)

'''
lln = "08078"
atoken = get_authenticationtoken(lln)
print(atoken)
'''
