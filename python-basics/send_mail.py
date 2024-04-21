import smtplib
import ssl
from email.message import EmailMessage

subject = "Congratulations!!"
body = "We are deleighted to welcome you to the team!"
sender_email = "dbriane208@gmail.com"
receiver_email = "dbriane208@gmail.com"
password = input('Enter you password : ')

message = EmailMessage()
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email
message.set_content(body)

context = ssl.create_default_context()
print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message.as_string)
print("Success")    