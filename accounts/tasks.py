from celery import shared_task

from utils.otp import send_otp_code


@shared_task
def send_otp_code_task(phone_number, code):
    send_otp_code(phone_number, code)
    return True
