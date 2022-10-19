from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from teacherApp.models import App

# Create your views here.
def index(request):
    return render(request,'teacherApp/index.html')

def search(request):
    school = request.POST['schoolInput']
    subject = request.POST['subjectInput']
    money = request.POST['moneyInput']
    value = request.POST['valueInput']
    machine = request.POST['machineInput']
    app = App.objects.filter(subject = subject)
    context = {
        'app':app,
    }
    return render(request,"teacherApp/search.html",context)