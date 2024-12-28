import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender="kevin0114@gmail.com"
receiver=["hometv25355877@gmail.com","kevin93724@gmail.com"]
passwd="wcyg ddqt cavx mgvv"

for i in receiver:
  msg = MIMEMultipart()
  msg["From"] = sender
  msg["To"] = i
  msg["Subject"] = Header("Test send email","utf-8").encode()

  body="This is send by python\nhow are you"

  msg_text=MIMEText(body)
  msg.attach(msg_text)
  c= ssl.create_default_context()

  with smtplib.SMTP_SSL("smtp.gmail.com",465,context=c) as server:
      server.login(sender,passwd)
      server.sendmail(sender,i,msg.as_string())
  print(i)
print("success send mail")
    #print(i)