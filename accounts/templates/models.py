from django.db import models
from django.contrib.auto.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
