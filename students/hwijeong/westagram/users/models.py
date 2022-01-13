from django.db import models

class user(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=300, unique=True)
    password = models.CharField(max_length=200)
    contact = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'