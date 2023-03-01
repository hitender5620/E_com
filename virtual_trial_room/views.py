from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data={
        'title':'VIRTUAL TRIAL ROOM'
    }
    return render(request, "index.html",data)
def cam(request):
    data={
        'title':'VIRTUAL TRIAL ROOM'
    }
    return render(request, "cam.py",data)

def btn(request):
    return HttpResponse('<b>welcome to Virtual Trial Room</b>')



    