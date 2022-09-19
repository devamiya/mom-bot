import ssl
import smtplib
print('hii')

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "coderaiders2022@gmail.com"
password = 'Hack@123'
print('hii2')
context = ssl.create_default_context()
server = smtplib.SMTP(smtp_server, port)
server.ehlo()  # Can be omitted
server.starttls(context=context)  # Secure the connection
server.ehlo()  # Can be omitted
server.login(sender_email, password)
sent_from = 'coderaiders2022@gmail.com'
to = 'priyanka.tomar1991@gmail.com'
subject = 'Minutes Of meeting'
body = 'I am message'
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
server.sendmail(sender_email, 'priyanka.tomar1991@gmail.com', email_text)
