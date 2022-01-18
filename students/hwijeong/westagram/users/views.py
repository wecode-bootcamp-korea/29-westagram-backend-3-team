import json
import bcrypt

from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views import View
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

from .models import User
from .validators import is_email_valid, is_password_valid

class RegisterView(View):

    def post(self, request):   
        data = json.loads(request.body)

        try:
            name     = data["name"]
            email    = data["email"]
            password = data["password"]
            contact  = data["contact"]
            note     = data["note"]

            is_email_valid(email)
            is_password_valid(password)
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            user = User.objects.create(
                name     = name,
                email    = email,
                password = hashed_password.decode('utf-8'),
                contact  = contact,
                note     = note
            )
            return JsonResponse({"message": "SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({'message': "KEY_ERROR"}, status=400)
        except IntegrityError:
            return JsonResponse({'message': "INTEGRITY_ERROR"}, status=400)
        except ValidationError as e:
            return JsonResponse({'message': f"{e.message}"}, status=401)
