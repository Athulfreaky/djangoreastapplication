from django.db import models
from datetime import datetime, timedelta
from django.conf import settings
settings.DATE_FORMAT
settings.DATETIME_FORMAT

# Create your models here.

class User_Model(models.Model):

    username = models.CharField(max_length=20)

    def __str__(self):

        return self.username

class Activity_Period_Model(models.Model):


    username = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now()+timedelta(hours=5))

    class Meta:
        unique_together = ['start_time', 'end_time']
        ordering = ['username']





   