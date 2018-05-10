from django.db import models

# Create your models here.
class Thing(models.Model):
    stuff = models.DateTimeField(auto_now=True)