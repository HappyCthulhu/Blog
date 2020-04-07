from django.core.mail import send_mail
from blogproject.settings import EMAIL_HOST_USER

def send(name, message, phone, email):
    send_mail(
        f'От {name}',
        f'Письмо: {message} . Телефон: {phone}',
        'Твоя почта',
        [email],
        fail_silently=False
    )
