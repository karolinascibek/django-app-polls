from account.auth.forms import UserCreationForm, UserLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from mysite.settings import LOGIN_REDIRECT_URL, LOGIN_URL
from django.contrib.auth.hashers import make_password

# Create your views here.


def register_view(request):
    if request.user.is_authenticated:
        return redirect(LOGIN_REDIRECT_URL)
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'success': 'Rejestracja się udała.'}
            return render(request, 'account/auth/login.html', context)
    return render(request, 'account/auth/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect(LOGIN_REDIRECT_URL)
    context = {}
    form = UserLoginForm()
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(LOGIN_REDIRECT_URL)
            else:
                context['falied'] = 'Logowanie nie powiodło się, spróbuj jeszcze raz.';
    context['form'] = form
    return render(request, 'account/auth/login.html', context)


@login_required(login_url=LOGIN_URL)
def logout_view(request):
    logout(request)
    return redirect(LOGIN_URL)