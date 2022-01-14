from django.db import models

from .validators import isEmailValid, isPasswordValid, checkEmailAndPassword

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, unique=True, validators=[isEmailValid, checkEmailAndPassword])
    password = models.CharField(max_length=200, validators=[isPasswordValid, checkEmailAndPassword])
    contact = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
