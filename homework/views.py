from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("Это мой первый проект Django")

def welcome(request):
    return render(request,"welcome.html")    
