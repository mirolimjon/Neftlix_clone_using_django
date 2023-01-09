from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField("Profile", blank=True)

AGE_LIMIT = (
    ('All', 'All'),
    ('Kids', 'Kids')
)

class Profile(models.Model):
    name = models.CharField(max_length=200)
    age_limit = models.CharField(choices=AGE_LIMIT, max_length=4)
    uuid = models.UUIDField(default=uuid.uuid4)
    
    def __str__(self):
        return self.name



MOVIE_CHOICES = (
    ('Seasonal','Seasonal'),
    ('Single','Single')
)
class Movies(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4)
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    type = models.CharField(choices=MOVIE_CHOICES, max_length=10)
    video = models.ManyToManyField("Video")
    image = models.ImageField(upload_to="cover-images/")
    age_limit = models.CharField(choices=AGE_LIMIT, max_length=4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=1000)
    file = models.FileField(upload_to="movies")

    def __str__(self):
        return self.title