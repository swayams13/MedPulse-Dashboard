import smtplib
from email.mime.text import MIMEText

def send_email(data):
    sender = "your_email@gmail.com"
    password = "your_app_password"

    receiver = "receiver_email@gmail.com"

    msg = MIMEText(str(data))
    msg["Subject"] = "Burnout Report"
    msg["From"] = sender
    msg["To"] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
