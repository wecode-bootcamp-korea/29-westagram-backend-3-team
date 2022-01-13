from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=300, unique=True)
    password = models.CharField(max_length=100)
    contact = models.IntegerField(max_length=30, unique=True)

    class Meta:
        db_table = 'users'