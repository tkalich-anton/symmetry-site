# users/models.py
from django.contrib.auth.models import AbstractUser, User
from django.db import models

class CustomUser(AbstractUser):
    role = models.CharField('Роль', max_length=300, null=True, blank=True)


class userProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_organizer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username