import json, re

from django.http import JsonResponse

from django.views import View
from users.models import User

class SignUpView(View):
    def post(self, request):
        try:
            user_data           = json.loads(request.body)
            EMAIL_VALIDATION    = r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            PASSWORD_VALIDATION = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
            
            email               = user_data['email']
            password            = user_data['password']
            name                = user_data['name'],
            phone_number        = user_data['phone_number'],

            if not re.match(EMAIL_VALIDATION, email):
                return JsonResponse({'Message' : 'Invalid Email'}, status = 400)
            
            if not re.match(PASSWORD_VALIDATION, password):
                return JsonResponse({'Message' : 'Invalid Password'}, status = 400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'Message' : 'Already Exist Email'}, status = 400)
            
            User.objects.create(  
                email          = email,
                password       = password,
                name           = name,
                phone_number   = phone_number,
            )
            return JsonResponse({'Message' : 'Created'}, status = 201)
        
        except KeyError:
            return JsonResponse({'Message' : 'KEY_ERROR'}, status = 400)