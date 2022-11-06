from django.shortcuts import render
from .forms import UserProfile, UserProfileForm

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import resolve
from django.contrib.auth.decorators import login_required
from django.urls import reverse



def home(request):
    return render(request, 'base/index.html')

def register(request):
    user_form = UserProfileForm
    profile_form = UserProfile
    registered = False
    if request.method == 'POST':
        user_form = user_form(request.POST)
        profile_form = profile_form(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
    return render(request, 'base/register.html', {'form': user_form, 'port': profile_form, 'registered': registered})

@login_required
def special(request):
    return HttpResponse('You are logged in')

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'base/index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                print('active')
                return render(request, 'base/index.html')
            else:
                print('Invalid login details')
        else:
            print('User is not logged in')
            return HttpResponse('Login was not succesfull, make sure you are logged in')
    return render(request, 'base/login.html')