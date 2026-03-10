import hashlib
from flask import Flask
from flask_mail import Mail, Message


salt="5gz"
def hash_password(password):
    password_salt = password + salt
    return hashlib.sha256(password_salt.encode()).hexdigest()


mail = Mail()
def init_mail(app):
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USE_SSL"] = True
    app.config["MAIL_USERNAME"] = "socialsocieties10@gmail.com"
    app.config["MAIL_PASSWORD"] =  "cegc blba etoj ozwx"
    app.config["MAIL_DEFAULT_SENDER"] = "SocialSocieties <noreply@socialsocieties.co.uk>"

    mail.init_app(app)


def send_email(to_email, code):
    if mail is None:
        raise RuntimeError("Mail not working. Contact Administrator. Initialise App first")
    
    message = Message (
        subject = "Your MFA Verification Code",
        recipients = [to_email],
        body = f"Your code is: {code} \n It expires in 5 minutes"
    )
    mail.send(message)