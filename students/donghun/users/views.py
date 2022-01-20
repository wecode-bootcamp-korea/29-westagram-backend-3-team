import json
import re
import bcrypt
import jwt

from django.http import JsonResponse
from django.views import View
from django.conf import settings

from users.models import User

class SignUpView(View):
    def post(self,request):
        user_data = json.loads(request.body)

        try:
            name     = user_data['name']
            email    = user_data['email']
            contact  = user_data['contact']
            password = user_data['password']

            REGEX_EMAIL        = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            REGEX_PASSWORD     = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&.]{8,}$'
            REGEX_PHONE_NUMBER = '\d{3}-\d{3,4}-\d{4}'

            if not re.match(REGEX_EMAIL, email):
                return JsonResponse({"messeage" : "EMAIL ERROR"}, status=400)
            if not re.match(REGEX_PASSWORD, password):
                return JsonResponse({"messeage" : "PASSWORD ERROR"}, status=400)
            if not re.match(REGEX_PHONE_NUMBER, contact):
                return JsonResponse({"messeage" : "CONTACT ERROR"}, status=400)
            if User.objects.filter(email = email).exists():
                return JsonResponse({"messeage" : "ALEADY_EXISTS"},status=400)

            hashed_password = bcrypt.hashpw(user_data['password'].encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            User.objects.create(
                email    = email,
                name     = name,
                password = hashed_password,
                contact  = contact,
            )

            return JsonResponse({"message" : "success"}, status=201)
        except KeyError:
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)

class SignInView(View):
    def post(self,request):

        try:
            user_data  = json.loads(request.body)
            user_email = user_data['email']

            user = User.objects.get(email=user_email)

            if bcrypt.checkpw(user_data['password'].encode('utf-8'), user.password.encode('utf-8')) :
                access_token = jwt.encode({"user_id" : user.id}, settings.SECRET_KEY, settings.ALGORITHM)
                return JsonResponse({"access_token" : access_token}, status=200)

            return JsonResponse({"messeage" : "INVALID_USER"}, status=401)

        except KeyError:
            return JsonResponse({"messeage" : "KEY_ERROR"}, status=400)
        except User.DoesNotExist:
            return JsonResponse({"messeage" : "INVALID_USER"}, status=401)