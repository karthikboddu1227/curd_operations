from django.shortcuts import render

# Create your views here.
from app.models import *

def topic_name(request):
    TO=Topic.objects.all()
    d={'topics':TO}
    return render(request,'topic.html',d)

def Webpage_inserction(request):
    WO=Webpage.objects.all()
    d={'Webpage':WO}
    return render(request,'web.html',d)