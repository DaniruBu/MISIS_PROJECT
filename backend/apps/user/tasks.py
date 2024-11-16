from celery import shared_task
from django.core.mail import send_mail
from .models import User
from django.conf import settings


@shared_task
def send_verification_email(user_id):
    try:
        user = User.objects.get(id=user_id)
        verification_link = f"http://localhost:8000/user/verify-email/{user_id}/"
        send_mail(
            "Verify your email",
            f"Click the link to verify your email: {verification_link}",
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            fail_silently=False,
        )
    except User.DoesNotExist:
        pass
