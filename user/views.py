from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def loginpage(request):
    msg=None
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('admin2')
            if user is not None and user.is_volunteer:
                login(request, user)
                return redirect('volunteer')
            if user is not None and user.is_coordinator:
                login(request, user)
                return redirect('coordinator')
            else:
                msg='invalid credentials'
    else:
            form = LoginForm()
    return render(request,'user/login.html',{'form':form,'msg':msg})



def register(request):
    if request.method=='POST':
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form =UserRegisterForm()
    
    return render(request,'user/register.html',{'form':form})

def volunteer(request):
    return render(request,'user/volunteer.html')

def admin(request):
    return render(request,'user/admin.html')

def coordinator(request):
    return render(request,'user/coordinator.html')

def home_home(request):
    return render(request,'user/home_home.html')

def home(request):
    return render(request,'user/home.html')