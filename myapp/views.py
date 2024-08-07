from django.shortcuts import render
from .models import Student
# Create your views here.

def index(request):
    return render(request,"app_index.html")

def about(request):
    return render(request,"about.html")

def list(request):
        students = Student.objects.all()
        data={
            'students':students,
        }
        return render(request,"list.html",data)