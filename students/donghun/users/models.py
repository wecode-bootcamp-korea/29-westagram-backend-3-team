from django.db import models

# Create your models here.

class User(models.Model):
    name     = models.CharField(max_length=20)
    email    = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    contact  = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "users"
