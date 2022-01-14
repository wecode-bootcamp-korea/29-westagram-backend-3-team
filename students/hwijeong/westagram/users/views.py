import json

from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views import View

from .models import User
from .validators import isEmailValid, isPasswordValid, checkEmailAndPassword

class RegisterView(View):

    def post(self, request):   
        data = json.loads(request.body)
        statusMessage = JsonResponse({"message": "SUCCESS"}, status=201)

        try:
            isEmailValid(data["email"])
        except:
            statusMessage = JsonResponse({"message": "FAILURE > Please check email format."}, status=400)
            return statusMessage

        try:
            checkEmailAndPassword(data["email"], data["password"])
        except:
            statusMessage = JsonResponse({"message": "KEY_ERROR > Please input email and password."}, status=400)
            return statusMessage

        try:
            isPasswordValid(data["password"])
        except:
            statusMessage = JsonResponse({"message": "FAILURE > Password must be at least 8 characters with 1 upper case letter and 1 number"}, status=400)
            return statusMessage

        try:            
            user = User.objects.create(
                name = data["name"],
                email = data["email"],
                password = data["password"],
                contact = data["contact"]
            )
        except:
            statusMessage = JsonResponse({"message": "FAILURE > Already registerd email or contact."}, status=400)

        return statusMessage
