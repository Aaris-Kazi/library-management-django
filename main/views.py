import django
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request,'index.html')
def register(request):
    if request.method == 'POST':
        u = User()
        u.username = request.POST['username']
        u.email = request.POST['email']
        u.password = request.POST['password']
        u.save()
        # auth_user
    return render(request,'register.html')

def login(request):
    # u = User.objects.get(username = 'Aaris')
    # # u.get_username("1")
    # u.set_password('12345')
    # u.save()
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=uname, password=pwd)
        print(user)
        if user is not None:
            print('passed')
        else:
            print('failed')
    return render(request,'login.html')