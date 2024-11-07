import os
from celery import Celery

# set teh default django setting module for the 'celery' program

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shoping.settings')

app = Celery('shoping')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()