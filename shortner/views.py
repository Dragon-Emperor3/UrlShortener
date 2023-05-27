from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'shortner/index.html', {})

# def create(request):
#     if request.method== 'POST':
#         link= request.POST['link']
#         check= Url.objects.get(link= str(link))        
#         if(check is not None):
#             return HttpResponse(str(check.uuid))
#         else:
#             uid= str(uuid.uuid4())[:5]
#             newUrl= Url(link= link, uuid=uid)
#             newUrl.save()
#             return HttpResponse(uid)

def create(request):
    if request.method== 'POST':
        link= request.POST['link']
        
        try:
            check= Url.objects.get(link= str(link))                
        except:
            uid= str(uuid.uuid4())[:5]
            newUrl= Url(link= link, uuid=uid)
            newUrl.save()
            return HttpResponse(uid)
        return HttpResponse(str(check.uuid))

def go(request, pk):
    url_details= Url.objects.get(uuid=pk)
    return redirect(str(url_details.link))