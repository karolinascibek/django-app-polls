from account.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, 'base.html')


def register_view(request):
    form = UserCreationForm()
    if request.method == "POST":
        print(request.POST)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    return render(request, 'account/auth/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')

    return render(request, 'account/auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('/login')