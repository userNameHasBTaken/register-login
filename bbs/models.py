from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    userName = models.CharField(max_length=32)
    def __str__(self):
        return self.userName