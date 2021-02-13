from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import authenticate, login as loginuser, logout as logoutuser
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, CreateLoginForm


# Create your views here.

def index(request):
    return render(request, 'app/index.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User Registered Successfully. Please Login To Continue.')
            return redirect('login')

    context = {'form': form}
    return render(request, 'app/auth/register.html', context)


def login(request):
    form = CreateLoginForm()
    if request.method == 'POST':
        form = CreateLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                loginuser(request, user)
                return redirect('home')
            else:
                messages.error(request, "Incorrect Username Or Password")

    context = {'form': form}
    return render(request, 'app/auth/login.html', context)


@login_required(login_url='login')
def home(request):
    return render(request, 'app/home/index.html')


def logout(request):
    logoutuser(request)
    return redirect('login')
