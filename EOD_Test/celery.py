from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Parse defaults from settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EOD_Test.settings')

# Instantiate Celery
app = Celery('EOD_Test')

# Load Celery config from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover Shared Tasks
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

