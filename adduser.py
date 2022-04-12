# -*- coding: utf-8 -*-
import os
import hashlib
import sqlite3
from time import sleep
from getpass import getpass
os.system('clear')

from main.lomux_logo import *
print(R + "[" + WM + "√" + R + "]" + WM + " Author	" + R + ":" + WM + " XAVHAX")
print(R + "[" + WM + "√" + R + "]" + WM + " Team	" + R + ":" + WM + " Sicx Brother")
print(R + "[" + WM + "√" + R + "]" + WM + " Github	" + R + ":" + WM + " github.com/XaVHaX")
print(W + "═════════════════════════════════")
print(G + "[" + R + "!" + G + "]" + WM + " Login Termux" + G + " v.1")
print(G + "[" + R + "!" + G + "]" + WM + " This program can only make 1 user")
print(G + "[" + R + "!" + G + "]" + WM + " But you can still change your password")
print(G + "[" + R + "?" + G + "]" + WM + " Input username for new user")

user = input(G + 'Username[]: ' + W)
sleep(1)
print(G + "[" + W + "*" + G + "] " + WM + "Adding new user '%s'" % user)
sleep(1)
print(G + "[" + W + "*" + G + "] " + WM + "Successfully")
sleep(1)
loop0 = 'true'
try:
    while loop0 == 'true':
        pasw = getpass(G + 'Input New Termux Password[]: ' + W)
        sleep(2)
        if pasw == "":
            print(G + "[" + R + "!" + G + "]" + WM + " Your Password Cannot Be Empty")
            loop0 = 'true'
        else:
            loop1 = 'true'
            while loop1 == 'true':
                confirmpasw = getpass(G + "Confirm New Termux Password[]: " + W)  # type: confirmpasw
                if confirmpasw == pasw:
                    sleep(2)
                    loop1 = 'false'
                    os.system('mkdir -p $PREFIX/login/')
                    os.system('chmod 700 $PREFIX/login/')
                    os.system('touch $PREFIX/login/database.db')
                    connect = sqlite3.connect('/data/data/com.termux/files/usr/login/database.db')
                    con = connect.cursor()
                    con.execute("CREATE TABLE IF NOT EXISTS admin (username text, password text)")
                    confirmpasw = confirmpasw.encode()
                    confirmpasw = hashlib.sha1(confirmpasw).hexdigest()
                    con.execute(f"INSERT INTO admin VALUES ('{user}', '{confirmpasw}')")
                    connect.commit()
                    print(G + "[" + W + "*" + G + "]" + WM + ' password: password add successfully')
                else:
                    sleep(2)
                    print(G + "[" + R + "!" + G + "]" + WM + " password: pasword add failure")
                    print(G + "[" + R + "!" + G + "]" + WM + " Note : make sure confirm your password")
                    loop1 = 'true'
            loop0 = 'false'

    print(G + "[" + R + "!" + G + "]" + WM + " Next running setup.py")
    print(G + "[" + R + "!" + G + "]" + WM + " $ python2 setup.py")
    os.remove('bash.bashrc')
    y = open('bash.bashrc', 'a', encoding="utf-8")
    y.write('#!/bin/bash\n')
    y.write("if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then\n")
    y.write('\tcommand_not_found_handle() {\n')
    y.write('\t\t/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"\n')
    y.write('\t}\n')
    y.write('fi\n\n')
    y.write('adduser(){\n')
    y.write('\tpython $PREFIX/login/readduser.py\n')
    y.write('}\n')
    y.write('falselogin(){\n')
    y.write('\tpython $PREFIX/login/db_falselogin.py\n')
    y.write('}\n')
    y.write('changepass(){\n')
    y.write('\tpython $PREFIX/login/changepass.py\n}\n')
    y.write('clear\n')
    y.write('python $PREFIX/login/.login.py\n')
    y.write('clear\n')
    y.write('neofetch\n')
    y.write("PS1='\e[0;37m\]┌─\[\e[1;37m\][\[\e[0;36m\]root\[\e[0;37m\]@\[\e[1;31m\]")
    y.write(f"{user}\[\e[1;37m]\[\e[1;30m\]\w\\n\[\e[0;37m\]└─╼\[\e[1;31m\]$ \[\e[0;32m\]'")
    y.close()
    sleep(4)
except EOFError:
    print(G + "[" + R + "!" + G + "]" + WM + " exit")
