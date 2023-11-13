from django.core.management.base import BaseCommand
from django.utils import timezone

from accounts.models import OtpCode


class Command(BaseCommand):
    help = 'remove all expire otp codes'

    def handle(self, *args, **options):
        expired_time = timezone.now() - timezone.timedelta(minutes=2)
        OtpCode.objects.filter(created__lt=expired_time).delete()
        self.stdout.write('All expired otp codes removed.')
