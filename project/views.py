from django.shortcuts import HttpResponse,render
from random import randint
def index_view(request):
    
    random_number=randint(1,100)
    
    data={"name":"John Doe",
          "hobbies":["Singing","Dancing","Running"],
          "random_num":random_number,
          "is_adult":True,}
    
    return render(request,"index.html",data)
    #return HttpResponse("<h1>This is index page</h1>")
def login(request):
    return render(request,"login.html",{"name":"Hyu Jack","age":"100"})
def reg(request):
    return HttpResponse("This is register page")