# coding=utf-8
from os import system
from time import sleep
from main.lomux_logo import *

print(R + WM + '[' + Y + '*' + WM + '] ' + R + "Try To Setup Login Termux")
sleep(5)
system('mkdir $PREFIX/login/')
system('chmod 700 $PREFIX/login/')
system("python history.py")
system('mv .login.py $PREFIX/login/')
system('mv history.py $PREFIX/login/')
system('mv db_falselogin.py $PREFIX/login/')
system('mv main $PREFIX/login/')
system('mv bash.bashrc $PREFIX/etc/')
system('mv adduser.py $PREFIX/login/')
system('mv changepass.py $PREFIX/login/')
system('mv readduser.py $PREFIX/login/')
system('rm $PREFIX/etc/motd')
print(WM + '[' + Y + '✓' + WM + '] ' + R + "Successfully")
sleep(1)
system('cd $HOME')
