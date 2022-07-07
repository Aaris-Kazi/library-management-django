from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')
def register(request):
    if request.method == 'POST':
        try:
            u = User()
            u.username = request.POST['username']
            u.email = request.POST['email']
            u.password = request.POST['password']
            u.save()
            messages.add_message(request, messages.SUCCESS, 'Registeration successful')
        except Exception:
            messages.add_message(request, messages.ERROR, 'A issue occur during registering')
        return render(request,'register.html')
    else:
        messages.add_message(request, messages.ERROR, '')
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
            messages.add_message(request, messages.SUCCESS, 'Registeration successful')
        else:
            messages.add_message(request, messages.ERROR, 'Login invalid please check username or passowrd')
        return render(request,'login.html')
    else:
        messages.add_message(request, messages.ERROR, '')
        return render(request,'login.html')
# messages.debug(request, '%s SQL statements were executed.' % count)
# messages.info(request, 'Three credits remain in your account.')
# messages.success(request, 'Profile details updated.')
# messages.warning(request, 'Your account expires in three days.')
# messages.error(request, 'Document deleted.')