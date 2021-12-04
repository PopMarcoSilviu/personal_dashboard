from django.contrib.auth.models import User
from django.db import models


class PersonalDashboard(models.Model):
    type_of_pd = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Note(models.Model):
    title = models.CharField(max_length=100)
    msg = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    pd = models.ForeignKey(PersonalDashboard, on_delete=models.CASCADE, blank=True, null=True)


class Task(models.Model):
    name = models.CharField(max_length=300)
    date_added = models.DateField(auto_now_add=True)
    date_to_complete = models.DateField()
    pd = models.ForeignKey(PersonalDashboard, on_delete=models.CASCADE, blank=True, null=True)


class Drawing(models.Model):
    drawing = models.ImageField()
    date_added = models.DateField(auto_now_add=True)
    pd = models.ForeignKey(PersonalDashboard, on_delete=models.CASCADE, blank=True, null=True)
