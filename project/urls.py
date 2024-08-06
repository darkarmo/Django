"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render
def index_view(request):
    return render(request,"index.html")
    #return HttpResponse("<h1>This is index page</h1>")
def homepage(request):
    return render(request,"homepage.html")
def login(request):
    return render("<h1>This is login page</h1>")
def reg(request):
    return HttpResponse("This is register page")

    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view),
    path('homepage/',homepage),
    path('login/',login),
    path('register/',reg)
]
