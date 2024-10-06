from django.db import models

# Create your models here.
class ToDoClass(models.Model):
  content=models.TextField()
