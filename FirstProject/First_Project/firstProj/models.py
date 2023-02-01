from django.db import models
import mysql

# Create your models here.
class AdminPanel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()


