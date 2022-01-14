import re

from django.core.exceptions import ValidationError

def checkEmailAndPassword(email, password):
    if(email == '' or password == ''):
        raise ValidationError("이메일과 패스워드를 모두 입력하세요!")

def isEmailValid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if not re.fullmatch(regex, email):
        raise ValidationError("이메일 형식을 확인하세요!")

def isPasswordValid(password):
    regex = re.compile(r'^(?=.*[\d])(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{6,12}$')
    if not re.fullmatch(regex, password):
        raise ValidationError("비밀번호를 확인하세요. 최소 1개 이상의 소문자, 대문자, 숫자, 특수문자로 구성되어야 하며 길이는 8자리 이상이어야 합니다.")
