from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello, Django!")



def home(request):
    return render(request, 'myapp/home.html')