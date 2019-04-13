from __future__ import absolute_import, unicode_literals
from .celery import app as celery_app

# Start Celery with Django

__all__ = ('celery_app',)
