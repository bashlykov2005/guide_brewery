from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.models import User


def send_contact_email_message(subject, email, content, ip, user_id):

    """Отправка электронного письма из формы обратной связи сайта"""

    user = User.objects.get(id=user_id) if user_id else None
    message = render_to_string(
        "feedback/feedback_email_send.html",
        {
            "email": email,
            "content": content,
            "ip": ip,
            "user": user,
        },
    )
    email = EmailMessage(subject, message, settings.EMAIL_SERVER, settings.EMAIL_ADMIN)
    email.send(fail_silently=False)
