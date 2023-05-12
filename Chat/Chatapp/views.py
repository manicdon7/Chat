from django.shortcuts import render

def index(request):
    context = {}
    return render(request, "Chatapp/index.html",context)

def details(request):
    context = {}
    return render(request, "Chatapp/details.html",context)