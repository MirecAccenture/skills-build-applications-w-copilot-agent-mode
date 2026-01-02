from django.db import models


# Placeholder model for the core app
from octofit_tracker.accounts.models import CustomUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(CustomUser, related_name='teams')

class Activity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    date = models.DateField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField(CustomUser, related_name='suggested_workouts')

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
