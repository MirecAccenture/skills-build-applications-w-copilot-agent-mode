from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model for OctoFit Tracker."""
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username
