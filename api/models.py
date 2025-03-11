from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    # The AbstractUser model already includes fields for email and password

    def __str__(self):
        return self.full_name

class Team(models.Model):
    team_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)
    captain = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teams')
    players_info = models.JSONField()  # For simplicity, using JSONField to store players' info

    def __str__(self):
        return self.team_name