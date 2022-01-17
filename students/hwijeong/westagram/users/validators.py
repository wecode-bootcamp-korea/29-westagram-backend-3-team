import re

from django.core.exceptions import ValidationError

def is_email_valid(email):
    REGEX_EMAIL = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    if not re.fullmatch(REGEX_EMAIL, email):
        raise ValidationError("EMAIL_INPUT_ERROR")

def is_password_valid(password):
    REGEX_PASSWORD = '^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{8,}$'
    if not re.fullmatch(REGEX_PASSWORD, password):
        raise ValidationError("PASSWORD_INPUT_ERROR")
