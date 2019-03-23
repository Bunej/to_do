from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = (
        ('Done', 'Done'),
        ('New', 'New')

    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    end_date = models.DateField(auto_now_add=False)
    description = models.TextField()

    def __str__(self):
        return self.name
