from django.contrib.auth.backends import BaseBackend

from accounts.models import User


class PhoneNumberBackend(BaseBackend):

    def authenticate(self, request, phone_number=None, password=None, **kwargs):
        if phone_number is None or password is None:
            return None
        try:
            user = User.objects.get(phone_number=phone_number)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            return user
        except User.DoesNotExist:
            return None
