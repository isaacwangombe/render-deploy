from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def port(request):
    return render(request, 'port.html', {})