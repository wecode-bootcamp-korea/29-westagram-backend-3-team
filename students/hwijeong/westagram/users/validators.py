import re

from django.core.exceptions import ValidationError

from .models import User

# def checkEmailAndPassword(email, password):
#     if(email == '' or password == ''):
#         raise ValidationError("Error: Email and password needed both.")

def isEmailValid(email):
    REGEX_EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    if not re.fullmatch(REGEX_EMAIL, email) and email == '':
        raise ValidationError("Error: Check email.")

def isPasswordValid(password):
    REGEX_PASSWORD = '^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{8,}$'
    if not re.fullmatch(REGEX_PASSWORD, password) and password == '':
        raise ValidationError("Error: Check password.")

def checkDuplicated(email, contact):
    try:
        userEmail = User.objects.get('email'=email)
        userContact = User.objects.get('contact'=contact)
    except User.DoesNotExist as e:
        print(e)
        raise ValidationError("Error: Duplicated email or contact")
        
    # for user in users:
    #     if (user.email == email or user.contact == contact):
    #         raise ValidationError("Error: Duplicated email or contact")

    