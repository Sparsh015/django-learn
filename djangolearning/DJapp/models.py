from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    
    #names changes in the database and dont display as "objects"
    def __str__(self):
        return self.name


# one to many relationship

class AnimeReview(models.Model):
    anime = models.ForeignKey(Varity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    #names changes in the database and dont display as "objects"
    def __str__(self):
        return f'{self.user.username} review for {self.anime.name}'
    

# many to many relationship

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    anime_varieties = models.ManyToManyField(Varity, related_name='stores')

    def __str__(self):
        return self.name
    

# one to one relationship

class AnimeCertificate(models.Model):
    anime = models.OneToOneField(Varity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=50)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_unitl = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.anime.name}'