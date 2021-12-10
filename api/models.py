from django.contrib.auth.models import User
from django.db import models


class PersonalDashboard(models.Model):
    name = models.CharField(max_length=10, default='NONAME')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    TYPE_OF_PD_CHOICES = [
        ('DRAWING', 'Drawing'),
        ('TASK', 'Task'),
        ('NOTE', 'Note'),
    ]

    type_of_pd = models.CharField(
        max_length=7,
        choices=TYPE_OF_PD_CHOICES,
        default='TASK'
    )

    class Meta:
        unique_together = ('name', 'user')


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
