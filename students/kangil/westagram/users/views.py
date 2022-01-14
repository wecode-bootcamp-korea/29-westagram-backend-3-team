import json, re

from django.http import JsonResponse

from django.views import View
from users.models import User

class SignUpView(View):
    def post(self, request):
        try:
            user_data           = json.loads(request.body)
            EMAIL_VALIDATION    = re.compile(r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
            PASSWORD_VALIDATION = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$')
            
            email               = user_data['email']
            password            = user_data['password']
            name                = user_data['name'],
            phone_number        = user_data['phone_number'],
            
            if email == "" or password == "":
                return JsonResponse({'Message': 'KEY_ERROR'}, status = 400)
                
            if not EMAIL_VALIDATION.match(email):
                return JsonResponse({'Message' : 'Invalid Email'}, status = 404)
            
            if not PASSWORD_VALIDATION.match(password):
                return JsonResponse({'Message' : 'Invalid Password'}, status = 404)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'Message' : 'Already Exist Email'}, status = 400)
            
            user_info = User.objects.create(
                
                email          = email,
                password       = password,
                name           = name,
                phone_number   = phone_number,
            )
            return JsonResponse({'Message' : 'Created'}, status = 201)
        
        except KeyError:
            return JsonResponse({'Message': 'FAILED'}, status = 400)
    
    def get(self, request):
        users     = User.objects.all()
        user_list = []
        
        for user in users:
            user_info = {
                'name'         : user.name,
                'email'        : user.email,
                'password'     : user.password,
                'phone_number' : user.phone_number,
                'created_at'   : user.created_at,
                'updated_at'   : user.updated_at,
            }
            user_list.append(user_info)
            
        return JsonResponse({'users' : user_list}, status = 200)