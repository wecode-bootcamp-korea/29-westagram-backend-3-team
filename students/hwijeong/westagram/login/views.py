import json
import bcrypt
import jwt

from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views import View
from django.core.exceptions import ValidationError

from users.models import User
from my_settings import SECRET_KEY 

class LoginView(View):
    def get(self, request):
        data = json.loads(request.body)

        try:
            email     = data["email"] 
            password  = data["password"]

            user_email = User.objects.get(email=email)

            if not user_email:
                raise ValidationError("INVALID_USER")

            validating_password = bcrypt.checkpw(password.encode('utf-8'), user_email.password.encode('utf-8'))
            
            if not validating_password:
                raise ValidationError("INVALID_PASSWORD")

            def get_access_token(user_email, SECRET_KEY):
                access_token = jwt.encode({'id': user_email.id}, SECRET_KEY, algorithm='HS256')

                def decoding_access_token(access_token, SECRET_KEY):
                    payload = jwt.decode(access_token, SECRET_KEY, algorithms='HS256')
                    return payload
                    
                return decoding_access_token(access_token, SECRET_KEY)

            token = get_access_token(user_email, SECRET_KEY)

            return JsonResponse({'message': f"SUCCESS, USER TOKEN: {token}"}, status=200)

        except KeyError:
            return JsonResponse({'message': "KEY_ERROR"}, status=400)
        except ValidationError as e:
            return JsonResponse({'message': f"{e.message}"}, status=401)
