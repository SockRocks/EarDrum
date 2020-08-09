import smtplib
from email.mime.text import MIMEText

msg = MIMEText("<h1>Hi</h1> <p>Fat ass lil chicken</p>", 'html')
msg['Subject'] = 'Improve my grade Mr. Slack'
msg['From'] = 'Epic Games'
msg['To'] = 'Ethan'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('ethangaver166@gmail.com', 'foxytrixie')
server.sendmail('ethangaver166@gmail.com', 'ethangaver166@gmail.com', msg.as_string())