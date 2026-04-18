from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

POSITION_CHOICES = (
    ('forward', 'Forward'),
    ('midfielder', 'Midfielder'),
    ('defender', 'Defender'),
    ('goalkeeper', 'Goalkeeper'),
)

LOCATION_CHOICES = (
    ('gauteng', 'Gauteng'),
    ('western_cape', 'Western Cape'),
    ('kwazulu_natal', 'KwaZulu-Natal'),
    ('free_state', 'Free State'),
    ('eastern_cape', 'Eastern Cape'),
    ('northern_cape', 'Northern Cape'),
    ('mpumalanga', 'Mpumalanga'),
    ('limpopo', 'Limpopo'),
    ('north_west', 'North West'),
)


class Athlete(models.Model):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, related_name='athletes')

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

    date_of_birth = models.DateField(default='2000-01-01')

    nationality = models.CharField(max_length=255)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)

    height = models.PositiveIntegerField(null=True, blank=True, help_text="cm")
    weight = models.PositiveIntegerField(null=True, blank=True, help_text="kg")

    # 🔒 Lock to football for MVP
    sport = models.CharField(max_length=50, default="football", editable=False)

    position = models.CharField(max_length=50, choices=POSITION_CHOICES)

    school_team = models.CharField(max_length=255, blank=True)
    club = models.CharField(max_length=255, blank=True)

    bio = models.TextField(max_length=1000, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class AthleteMedia(models.Model):
    MEDIA_TYPE_CHOICES = (
        ('photo', 'Photo'),
        ('video', 'Video'),
    )

    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='media')
    file = models.FileField(upload_to='athlete_media/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.athlete} - {self.media_type}"