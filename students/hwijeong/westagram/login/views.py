import json

from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views import View
from django.core.exceptions import ValidationError

from users.models import User

class LoginView(View):
    def get(self, request):
        data = json.loads(request.body)

        try:
            email     = data["email"] 
            password  = data["password"]

            userValidation = User.objects.filter(email=email, password=password).exists()

            if not userValidation:
                raise ValidationError({'message': "Please check email or password"})
    
            return JsonResponse({'message': "SUCCESS"}, status=200)
        except KeyError:
            return JsonResponse({'message': "KEY_ERROR"}, status=400)
        except ValidationError:
            return JsonResponse({'message': "INVALID_USER"}, status=401)
