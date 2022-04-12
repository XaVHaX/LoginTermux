import time
import os
from main.lomux_logo import *

sure = input(W + 'Are you sure want to uninstall this program [y/n]: ').lower()
if sure == 'y':
    print(WM + '[' + R + '!' + WM + '] ' + WM + "Uninstalling The Program")
    time.sleep(3)
    os.system('rm -rf $PREFIX/login')
    os.system('mv bash.bashrc.dpkg-old $PREFIX/etc/bash.bashrc')
    os.system('mv motd $PREFIX/etc/')
    print("Thank You For Using This Program :v")
    print("If you want to install it again, you need to clone the repo again")
elif sure == 'n':
    print(WM + '[' + R + '!' + WM + '] ' + WM + "Abort Uninstall The Program")
    time.sleep(1)
    print(WM + '[' + G + '*' + WM + '] ' + WM + "Okay, Have a good day")
else:
    print("Command " + sure + " Not Found")
