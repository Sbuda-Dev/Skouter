from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # You can add additional fields here if needed
    
    USER_TYPE_CHOICES = (

        ('athlete', 'Athlete'),
        ('scout', 'Scout'),
        ('parent', 'Parent')
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    is_verified = models.BooleanField(default=False)

def __str__(self):
    return self.username
