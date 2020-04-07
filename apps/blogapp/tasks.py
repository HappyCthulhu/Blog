from blogproject.celery import app
from .service import send

@app.task
def send_spam_email(name, message, phone, email):
    send(name, message, phone, email)
