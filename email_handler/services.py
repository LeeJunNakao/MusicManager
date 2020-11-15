import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import EmailDto

from config import get_settings


def send_email(email: EmailDto):
    settings = get_settings()

    host = settings["SMTP_HOST"]
    port = settings["SMTP_PORT"]
    user = settings["SMTP_USER"]
    password = settings["SMTP_PASSWORD"]

    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(user, password)

    message = email.message
    email_msg = MIMEMultipart()
    email_msg["From"] = user
    email_msg["To"] = email.receiver
    email_msg["Subject"] = email.subject

    email_msg.attach(MIMEText(message, "plain"))

    server.sendmail(email_msg["From"], email_msg["To"], email_msg.as_string())
    server.quit()
