from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            
            username = request.POST['username']
            password = request.POST['password']
            print(password.split("*-*"))
            user = auth.authenticate(username=username,password=password)       
            if user is not None:
                return HttpResponse('{"success":"1","id":'+str(user.id)+'}')
            else:
                return HttpResponse('{"success":"0"}')
        except:
            return HttpResponse('{"success":"0"}')

    else:
        return HttpResponse("GET")

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:    
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,password=password,email=email)
            user.save()
            return HttpResponse('{"success":"1","id":'+str(user.id)+'}')           
        except:
            return HttpResponse('{"success":"0"}')


    else:
        return HttpResponse("GET")
                
      
