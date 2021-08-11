from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def login(request):
    return render(request, 'login.html')

def dashboard_v2(request):
    return render(request,'dashboard_v2.html')

def dashboard_v3(request):
    return render(request,'dashboard_v3.html')

def recover(request):
    return render(request,'recover.html')

def register(request):
    return render(request,'register.html')
# Create your views here.
