import os
import imaplib

mailcount = 0

user = 'ethangaver166@gmail.com'
passw = 'foxytrixie'
server = imaplib.IMAP4_SSL('smtp.gmail.com')
server.login(user, passw)



server.select('Inbox')
result, its = server.search(None, '(FROM "ethangaver166@gmail.com")')


statu, data = server.fetch(b'1', '(RFC822)')
if data != [None]:
    rdata = data[0][1]
    raw = rdata.decode('utf-8')
    if 'mkd' in raw:
        print(raw)
        for x in raw:
            print(x)
            if 'mkd' in x:
                commandl = x
        print(commandl)
        commandl.split('input')
        os.mkdir('the email said so')
else:
    print('no mail')