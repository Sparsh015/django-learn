from django.db import models
from django.utils import timezone

# Create your models here.

class Varity(models.Model):

    ANIME_TYPE_CHOICE = [
        ('KB', 'Kuroku Basketball'),
        ('ON', 'One Piece'),
        ('DR', 'Dragon Ball Z'),
        ('NT', 'Naruto'),
        ('AT', 'Attack on Titan'),
        ('DS', 'Demon Slayer'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'imgs/')
    date_added = models.DateTimeField(default = timezone.now)
    type = models.CharField(max_length=2, choices = ANIME_TYPE_CHOICE)
    