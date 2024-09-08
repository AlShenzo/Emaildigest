import smtplib
import ssl
import os

def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    username = 'alanshenjc@@gmail.com'
    app_password = os.getenv('emaildigestpassword')
    receiver = 'alanshenjc@gmail.com'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, app_password)
        server.sendmail(username, receiver, message)




