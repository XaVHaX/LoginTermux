import sqlite3
from tabulate import tabulate

recon = sqlite3.connect('/data/data/com.termux/files/usr/login/database.db')
try:
    from history import con
    print("This Is False Login")
    print("Where The User Trying To Login With Another User and Password")
    con.execute("SELECT * FROM notadmin")
    show = con.fetchall()
    head = ["Username", "Password", "Date"]
    print(tabulate(show, headers=head, tablefmt='grid'))
except NameError:
    print("Currently There's Nothing Wrong Input Username & Password Now")
