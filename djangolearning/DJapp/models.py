from django.db import models
from django.utils import timezone
from django.contrib.auth.models import user

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
    description = models.TextField(default='')
    

    def __str__(self):
        return self.name
    
#one to many relationship

class AnimeReview(models.Model):
    anime = models.ForeignKey(Varity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(user, on_delete=models.CASCADE)