from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class ScoutProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='scout_profile')
    organization = models.CharField(max_length=255)
    verified = models.BooleanField(default=False)

    def __str__(self):

        return self.user.username
