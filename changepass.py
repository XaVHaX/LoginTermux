# coding=utf-8
import hashlib
import sqlite3

from time import sleep
from main.color import *
from getpass import getpass

try:
	print(G + "[" + R + "!" + G + "]" + WM + " Are You Sure Want To Change Password ?")
	sure = input(G + 'Y' + BWhite + '/' + R + 'N' + WM + ': ')
	sleep(1)
	if sure == 'Y' or sure == 'y':
		loop = 'true'
		while loop == 'true':
			oldpassword = getpass(WM + '[' + Y + '?' + WM + '] ' + R + 'Old Password' + Y + ': ' + WM)
			sleep(1)

			oldpassword = oldpassword.encode()
			oldpassword = hashlib.sha1(oldpassword).hexdigest()

			connect = sqlite3.connect('/data/data/com.termux/files/usr/login/database.db')
			con = connect.cursor()
			con.execute(f"SELECT password from admin WHERE password='{oldpassword}'")

			if con.fetchall():
				print(WM + '[' + G + '✓' + WM + '] ' + WM + "Old Password is Correct ")
				loop = 'false'
				newpassw = input(WM + '[' + Y + '?' + WM + '] ' + R + 'Input New Password: ' + WM)
				lup = 'true'
				while lup == 'true':
					nowpassw = input(WM + '[' + Y + '?' + WM + '] ' + R + 'Confirm New Password: ' + WM)
					sleep(1)
					if nowpassw == newpassw:
						newpassw = newpassw.encode()
						newpassw = hashlib.sha1(newpassw).hexdigest()

						con.execute(f"UPDATE admin set password='{newpassw}'")
						connect.commit()
						lup = 'false'
						sleep(1)
						print("[✓] New Password add Succesfully")
					else:
						print("[!] New Password add Failure")
						print("[!] Make Sure Confirm Your New Password")
						lup = 'true'
			else:
				print(G + "[" + R + "!" + G + "]" + WM + " Old Password Is Incorrect, Please Try Again")
				loop = 'true'
	elif sure == 'n' or sure == 'N':
		print("\nOkay, Have a Good Day")

	else:
		print(f"Command {sure} Not Found")

except EOFError:
	print("\nexit\n")
except:
	print("\nexit\n")
