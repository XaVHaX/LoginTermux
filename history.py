import os

try:
    import sqlite3
    from tabulate import tabulate
except ImportError:
    os.system("pkg install sqlite3")
    os.system("pip install tabulate")
    import sqlite3
    from tabulate import tabulate
connect = sqlite3.connect('/data/data/com.termux/files/usr/login/database.db')
con = connect.cursor()
con.execute("CREATE TABLE IF NOT EXISTS notadmin (username text, password text, date_signin text)")
connect.commit()
