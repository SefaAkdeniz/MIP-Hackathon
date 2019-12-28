from django.shortcuts import render
from django.http import HttpResponse
from Haber.models import New,Work,Life,News,Event
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import requests 

# Create your views here.

@csrf_exempt
def Haber(request):
    if request.method == 'POST': 
        URL= ""       
        #try:
        if 2>1:            
            id=request.POST['id']
            user=User.objects.filter(id=id)[0]                      
            tags=News.objects.filter(user=user).first()
            tagsArray=tags.News.split("*-*")
            print(tagsArray)           
            headers  = {'Authorization':"apikey 7Ku7gtUGVnUmjvLPKGr5w2:2GS6KaK11XfbV5FvVrItuu"}           
            response='{"success":"1","data":'
            for each in tagsArray:
                URL = "https://api.collectapi.com/news/getNews?tag="
                URL = URL+str(each)
                URL=URL+"&country=tr"
                r = requests.get(url = URL, headers  = headers)
                data = r.json()
                try:
                    print(data["result"][0]["key"])
                    response=response+str(data["result"])
                except:
                    print(data["result"])
                    
            response=response+"}"
            

            
            return HttpResponse(response)           
        #except:
            #return HttpResponse('{"success":"0"}')


    else:
        return HttpResponse("GET")

    



@csrf_exempt
def Tag(request):
    if request.method == 'POST':       
        try:       
            id=request.POST['id']
            user=User.objects.filter(id=id)[0]                      
            work = request.POST['work']
            life = request.POST['life']
            new = request.POST['news']
            event = request.POST['event']           
            workSave = Work(user=user,Work=work)
            workSave.save()
            lifeSave = Life(user=user,Life=life)
            lifeSave.save()
            newSave = News(user=user,News=new)
            newSave.save()
            eventSave = Event(user=user,Event=event)
            eventSave.save()
            return HttpResponse('{"success":"1"}')           
        except:
            return HttpResponse('{"success":"0"}')


    else:
        return HttpResponse("GET")
                
