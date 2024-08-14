import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'katsu_dev.settings')
app = Celery('katsu_dev')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()