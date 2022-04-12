import hashlib
import sqlite3

from time import sleep

from main.lomux_logo import *
from getpass import getpass

print("This Is Adduser Where The User Change Username & Password")
print("The Previous Username & Password Will Be Deleted")
print(WM + '[' + G + '?' + WM + '] ' + WM + " Are You Sure Want To Change Username and Password")
ask = input(f"{G}Y{W}/{R}N{W}: ").lower()
sleep(1)
if ask == 'y':
    try:
        loop = 'true'
        while loop == 'true':
            password = getpass(WM + '[' + G + '?' + WM + '] ' + WM + "Password: ")
            sleep(2)
            password = password.encode()
            password = hashlib.sha1(password).hexdigest()

            connect = sqlite3.connect('/data/data/com.termux/files/usr/login/database.db')
            con = connect.cursor()
            con.execute(f"SELECT password from admin WHERE password='{password}'")

            if con.fetchall():
                con.execute("DROP TABLE admin")
                import adduser
            else:
                print(WM + '[' + G + '!' + WM + '] ' + WM + "Invalid Password")
                loop = 'true'

    except EOFError:
        print("\nexit\n")
    except:
        print("\nexit\n")
elif ask == 'n':
    print(WM + '[' + R + '!' + WM + '] ' + WM + "Okay, Have a Good Day")
    loop = 'false'
else:
    print(f"Command {ask} Not Found")
