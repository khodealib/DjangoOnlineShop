import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoOnlineShop.settings')

app = Celery('DjangoOnlineShop')
app.autodiscover_tasks()

app.conf.broker_url = 'amqp://'
app.conf.result_backend = 'rpc://'
app.conf.task_serializer = 'json'
app.conf.result_serializer = 'pickle'
app.conf.accept_content = ['json', 'pickle']
app.conf.result_expire = timedelta(days=1)
app.conf.task_always_eager = False
app.conf.worker_prefetch_multiplier = 4

