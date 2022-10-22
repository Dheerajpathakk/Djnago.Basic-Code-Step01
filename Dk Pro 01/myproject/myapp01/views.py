from django.shortcuts import render
from django.http import HttpResponse
def registration(request):
    return HttpResponse("<h1>Hello Guys I'm Dheeraj</h1>")
    # return render(request,"regi.html")
