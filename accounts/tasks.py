from celery import shared_task
from django.utils import timezone

from accounts.models import OtpCode
from utils.otp import send_otp_code


@shared_task
def remove_expire_otp_codes_task():
    expired_time = timezone.now() - timezone.timedelta(minutes=2)
    OtpCode.objects.filter(created__lt=expired_time).delete()


@shared_task
def send_otp_code_task(phone_number, code):
    send_otp_code(phone_number, code)
    return True
