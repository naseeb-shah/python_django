from django.db import models
from django.utils import timezone  # Add this import


# Create your models here.
class Todo(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200)
    details=models.TextField(max_length=200)
    status=models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title},{self.details},{self.status}"