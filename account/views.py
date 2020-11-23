from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mysite.settings import LOGIN_REDIRECT_URL, LOGIN_URL


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'account/dashboard.html')
    return render(request, 'base.html')


@login_required(login_url=LOGIN_URL)
def profile_view(request):
    username = request.user.username.replace(" ", ".")
    return render(request, 'account/profile.html', {'url_username': username})


@login_required(login_url=LOGIN_URL)
def detail_profile_view(request, username):
    return render(request, 'account/detail_profile.html', {})


@login_required(login_url=LOGIN_URL)
def password_change_view(request, username):
    if request.method == "POST":
        print("zmiana chasła POST ............................. ")
        print(request.user.id)
    return render(request, 'account/detail_profile.html', {})



