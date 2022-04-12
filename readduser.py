import hashlib
import sqlite3

from getpass import getpass


try:
    loop = 'true'
    while loop == 'true':
        password = getpass()

        password = password.encode()
        password = hashlib.sha1(password).hexdigest()

        connect = sqlite3.connect('/data/data/com.termux/files/usr/login/database.db')
        con = connect.cursor()
        con.execute(f"SELECT password from admin WHERE password='{password}'")

        if con.fetchall():
            con.execute("DROP TABLE admin")
            import adduser
            loop = 'false'
        else:
            print("Invalid Password")
            loop = 'true'

except EOFError:
    print("\nexit\n")
except:
    print("\nexit\n")
