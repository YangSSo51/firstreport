from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def website(request):
    return render(request,'website.html')
