import json

from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views import View
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from .models import User
from .validators import isEmailValid, isPasswordValid

class RegisterView(View):

    def post(self, request):   
        data = json.loads(request.body)

        try:
            name     = data["name"]
            email    = data["email"]
            password = data["password"]
            contact  = data["contact"]
            note     = data["note"]

            isEmailValid(email)
            isPasswordValid(password)
       
            user = User.objects.create(
                name     = name,
                email    = email,
                password = password,
                contact  = contact,
                note     = note
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({'message': "Please check the input, all values needed"})
        except IntegrityError:
            return JsonResponse({'message': "Please check the input, it might be duplicated"})
        except ValidationError as e:
            return JsonResponse({'message': f"{e.message}"})
