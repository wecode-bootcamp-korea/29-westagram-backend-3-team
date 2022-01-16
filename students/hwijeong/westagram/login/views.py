import json

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ValidationError

from users.models import User

class LoginView(View):
    def get(self, request):
        data = json.loads(request.body)

        try:
            email     = data["email"] 
            password  = data["password"]

            users = User.objects.all()

            userList = []
            for user in users:
                userList.append(
                    {
                        'email': user.email,
                        'password': user.password,
                    }
                )

            print(userList)

            emailList = []
            for emails in userList:
                emailList.append(
                    emails['email']
                )
            
            if email == '' or password == '':
                raise KeyError

            if email not in emailList:
                raise ValidationError("INVALID_USER")

            for i in range(len(emailList)):
                if userList[i]['email'] == email and userList[i]['password'] != password:
                   raise ValidationError("INVALID_USER")

            return JsonResponse({"message": "SUCCESS"}, status=200)
        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status = 400)
        except ValidationError as e:
            return JsonResponse({"message": f"{e.message}"}, status = 401)
