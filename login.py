import atexit
import hashlib
import os
import sys
import time
import sqlite3
import copy
from getpass import getpass
from time import sleep
from main.logo import *

if True:
    os.system("stty eof ^X")
    atexit.register(lambda: os.system("stty eof ^D"))


def loading():
    print("Try to Login", end='')
    load = ".....\n"
    for login in load:
        sleep(0.5)
        sys.stdout.write(login)
        sys.stdout.flush()


loop = 'true'
while loop == 'true':
    try:
        usr = input(WM + '[' + Y + '?' + WM + '] ' + R + 'Username' + Y + ': ' + WM)
        password = getpass(WM + '[' + Y + "?" + WM + "] " + R + "Password" + Y + ": " + WM)
        passmord = copy.copy(password)
        password = password.encode()
        password = hashlib.sha1(password).hexdigest()

        reconnect = sqlite3.connect('/data/data/com.termux/files/usr/login/database.db')
        cursor = reconnect.cursor()

        cursor.execute(f"SELECT username from admin WHERE username='{usr}' AND password='{password}'")

        if cursor.fetchall():
            sleep(2)
            loading()
            print(G + "Successfully Login as " + R + f"{usr}")
            loop = 'false'
            sleep(2)
        else:
            date = time.strftime("%c")
            from history import con, connect
            con.execute(f"INSERT INTO notadmin VALUES ('{usr}', '{passmord}', '{date}')")
            connect.commit()
            loading()
            print(G + "Username or Password doesn't exist")
            loop = 'true'
    except EOFError:
        print("\nCannot Close Login\n")
        loop = 'true'
    except KeyboardInterrupt:
        print("\nCannot Close Login\n")
        loop = 'true'
