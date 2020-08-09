import time
import os
import sys


time.sleep(50)
username = os.environ['USERNAME']


with open('C:\\Users\\' + username + '\\Windows32\\t_d', 'w')as timeDone:
	timeDone.close()
time.sleep(3)
sys.exit()