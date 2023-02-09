import smtplib,ssl
from email import message
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from  email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders

fromaddr="shaileshnikam13@gmail.com"
toaddr="shaileshnikam77@gmail.com"
subject="Python automatic mail"
body = """
Hello Shailesh,
wolcome to python
plsese find attched file.
log file cretaed at:%s
start time of scanning:
total no.of files scanned:
total no of duplicated file found:

This is auto genertaed mail.
Thanks,
Shailesh"""
msg=message.Message()
msg.add_header('from',fromaddr)
msg.add_header('to',toaddr)
msg.add_header('subject',subject)
msg.set_payload(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    print( 'waiting to login...')
    server.login(fromaddr,'*********')
    print( 'waiting to send...')


    server.send_message(msg, from_addr=fromaddr, to_addrs=[toaddr])

print( 'email appears to have been sent with attchement')