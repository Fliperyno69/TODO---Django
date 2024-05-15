from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
