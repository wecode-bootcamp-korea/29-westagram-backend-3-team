import re

from django.core.exceptions import ValidationError

def isEmailValid(email):
    REGEX_EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    if not re.fullmatch(REGEX_EMAIL, email) or email == '':
        raise ValidationError("Error: Check email.")

def isPasswordValid(password):
    REGEX_PASSWORD = '^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{8,}$'
    if not re.fullmatch(REGEX_PASSWORD, password) or password == '':
        raise ValidationError("Error: Check password.")