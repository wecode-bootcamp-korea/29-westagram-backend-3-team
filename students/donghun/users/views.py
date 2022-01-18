import json
import re
import bcrypt

from django.http import JsonResponse
from django.views import View

from users.models import User

class SignUpView(View):
    def post(self,request):
        user_data = json.loads(request.body)

        try:

            encoded_password = user_data['password'].encode('utf-8')
            password_bcrypt = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

            name     = user_data['name']
            email    = user_data['email']
            contact  = user_data['contact']
            password = password_bcrypt

            REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zxA-Z0-9-.]+$'
            REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&.]{8,}$'
            REGEX_PHONE_NUMBER = '\d{3}-\d{3,4}-\d{4}'

            if not re.match(REGEX_EMAIL, email):
                return JsonResponse({"messeage": "EMAIL ERROR"}, status=400)
            if not re.match(REGEX_PASSWORD, user_data['password']):
                return JsonResponse({"messeage" : "PASSWORD ERROR"}, status=400)
            if not re.match(REGEX_PHONE_NUMBER, contact):
                return JsonResponse({"messeage" : "CONTACT ERROR"}, status=400)
            if User.objects.filter(email = email).exists():
                return JsonResponse({"messeage" : "ALEADY_EXISTS"},status=400)



            User.objects.create(
                email    = email,
                name     = name,
                password = password.decode('utf-8'),
                contact  = contact,
            )

            return JsonResponse({"message":"success"}, status=201)
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

class SignInView(View):
    def post(self,request):

        try:
            user_data = json.loads(request.body)

            user_email = user_data['email']
            user_password = user_data['password']

            if User.objects.filter(email = user_email, password = user_password).exists():
                return JsonResponse({"messeage" : "SUCCESS"}, status = 200)
            else:
                return JsonResponse({"messeage" : "INVALID_USER"}, status = 401)

        except KeyError:
            return JsonResponse({"messeage" : "KEY_ERROR"}, status=400)