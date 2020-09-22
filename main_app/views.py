from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        Email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('/')
            elif User.objects.filter(email=Email).exists():
                messages.info(request, 'Email taken')
                return redirect('/')
            else:
                user = User.objects.create_user(username=username, email=Email, password=password1)
                user.save();
                print('user approved')
                return redirect('/')

        else:
            messages.info(request, 'Password not matching')
            return 

    else:
        return render(request, 'index.html')


def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            return render(request,'index.html')
        
        else:
            messages.info(request,'invalid')
            return redirect('/')
    
    else:
        return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')