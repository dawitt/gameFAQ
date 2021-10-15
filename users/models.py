from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.postgres.fields import ArrayField

# Create your models here.
class MyUser(AbstractUser):
    display_name = models.CharField(max_length=30)
<<<<<<< Updated upstream
    profile_img = models.ImageField(upload_to='images/', null=True, blank=True )

=======
    profile_img = models.ImageField(upload_to='imgages/', null=True, blank=True)
    favorite_games = models.CharField(max_length=100, null=True, blank=True)
>>>>>>> Stashed changes
