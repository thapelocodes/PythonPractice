from email.mime.text import MIMEText
import smtplib

msg = MIMEText("<h1>A Heading</h1><p>Hello There!</p>", "html")
msg['Subject'] = 'A Test HTML Message'
msg['From'] = 'tm.moumakoe@gmail.com'
msg['To'] = 'tm.moumakoe@gmail.com'

s = smtplib.SMTP('localhost')
s.sendmail('tm.moumakoe@gmail.com', ['tm.moumakoe@gmail.com'], msg.as_string())

print("Message Sent!")
