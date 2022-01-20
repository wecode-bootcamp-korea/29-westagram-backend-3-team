import json
import re
import bcrypt
import jwt

from django.http        import JsonResponse

from django.views       import View
from users.models       import User
from westagram.settings import SECRET_KEY, ALGORITHM

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
            hashed_password     = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

            if not re.match(EMAIL_VALIDATION, email):
                return JsonResponse({'Message' : 'Invalid Email'},       status = 400)
            if not re.match(PASSWORD_VALIDATION, password):
                return JsonResponse({'Message' : 'Invalid Password'},    status = 400)
            if User.objects.filter(email = email).exists():
                return JsonResponse({'Message' : 'Already Exist Email'}, status = 400)
            
            User.objects.create(  
                email          = email,
                password       = hashed_password.decode('utf-8'),
                name           = name,
                phone_number   = phone_number,
            )
            return JsonResponse({'Message' : 'Created'},  status = 201)
        except KeyError:
            return JsonResponse({'Message': 'KEY_ERROR'}, status = 400)
class SignInView(View):
    def post(self, request):
        try:
            user_data_input = json.loads(request.body)
            email           = user_data_input['email']
            password        = user_data_input['password']
            user            = User.objects.get(email = email)
            
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'Message' : 'Invalid_User'}, status = 401)

            access_token = jwt.encode({'id' : user.id}, SECRET_KEY, ALGORITHM)
            return JsonResponse({"Message" : "Success", "JWT" : access_token}, status = 200)
        except KeyError:
            return JsonResponse({'Message' : 'KEY_ERROR'}, status = 400)