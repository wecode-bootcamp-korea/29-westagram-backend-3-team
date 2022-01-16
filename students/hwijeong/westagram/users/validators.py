import re

from django.core.exceptions import ValidationError

from .models import User

def checkEmailAndPassword(email, password):
    if(email == '' or password == ''):
        raise ValidationError("Error: Email and password needed both.")

def isEmailValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(regex, email):
        raise ValidationError("Error: Check email format.")

def isPasswordValid(password):
    regex = re.compile(r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{8,}$')
    if not re.fullmatch(regex, password):
        raise ValidationError("Error: Password is not strong.")

def checkDuplicated(email, contact):
    users = User.objects.all()
    print(users)
    for user in users:
        if (user.email == email or user.contact == contact):
            raise ValidationError("Error: Duplicated email or contact")