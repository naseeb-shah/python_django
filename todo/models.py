from django.db import models
from django.utils import timezone  # Add this import


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    details=models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.title