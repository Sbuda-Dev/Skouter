from django.db import models
from accounts.models import User
from datetime import date
from django.utils import timezone

# Create your models here.

LOCATION_CHOICES = (
        ('johannesburg', 'Johannesburg'),
        ('cape town', 'Cape Town'),
        ('durban', 'Durban'),
        ('pretoria', 'Pretoria'),
        ('port elizabeth', 'Port Elizabeth'),
        ('bloemfontein', 'Bloemfontein'),
        ('east london', 'East London'),
        ('kimberley', 'Kimberley'),
        ('nelspruit', 'Nelspruit'))

STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    )

class Invite(models.Model):

  
    scout = models.ForeignKey(User, on_delete=models.CASCADE)
    athlete = models.ForeignKey('athletes.Athlete', on_delete=models.CASCADE)

    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    start_time = models.TimeField(default=timezone.now)
    end_time = models.TimeField(default=timezone.now)

    message = models.TextField(max_length=1000, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invite from {self.scout.user.username} to {self.athlete.name} {self.athlete.surname}"


