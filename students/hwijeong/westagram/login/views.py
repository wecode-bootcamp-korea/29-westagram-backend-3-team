import json
import bcrypt
import jwt

from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views import View
from django.core.exceptions import ValidationError

from users.models import User
from my_settings import SECRET_KEY, ALGORITHM

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            email     = data["email"] 
            password  = data["password"]

            validated_user = User.objects.get(email=email)

            if not validated_user:
                raise ValidationError("INVALID_USER")

            validating_password = bcrypt.checkpw(password.encode('utf-8'), validated_user.password.encode('utf-8'))
            
            if not validating_password:
                raise ValidationError("INVALID_PASSWORD")

            access_token = jwt.encode({'id': validated_user.id}, SECRET_KEY, algorithm=ALGORITHM)


            user_information = decoding_access_token(access_token, SECRET_KEY)

            return JsonResponse({'message': f"SUCCESS, USER TOKEN: {access_token}, USER INFORMATION: {user_information}"}, status=200)

        except KeyError:
            return JsonResponse({'message': "KEY_ERROR"}, status=400)
        except ValidationError as e:
            return JsonResponse({'message': f"{e.message}"}, status=401)
