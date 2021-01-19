from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from mysite.settings import LOGIN_REDIRECT_URL, LOGIN_URL
from django.contrib.auth import update_session_auth_hash, logout

from .forms import UserUpdateForm, UserPasswordChangeForm
from .models import MyUser

from django.shortcuts import render, redirect, get_list_or_404
from polls.questionnaire.models import Questionnaire
from polls.respondents.models import Respondent


# Create your views here.


def index(request):
    if request.user.is_authenticated:
        if request.user.is_creator:
            questionnaires = Questionnaire.objects.filter(creator=request.user)
            return render(request, 'account/dashboard/creator.html', {'questionnaires': questionnaires})
        else:
            respondent = Respondent.objects.filter(user=request.user)
            questionnaires = []
            for r in respondent:
                questionnaires.append(r.questionnaire)
            context = {'questionnaires': questionnaires}
            return render(request, 'account/dashboard/respondent.html', context)
    return render(request, 'home.html')

@login_required(login_url=LOGIN_URL)
def profile_view(request):
    username = request.user.username.replace(" ", ".")
    return render(request, 'account/profile.html', {'url_username': username})


@login_required(login_url=LOGIN_URL)
def update_profile_view(request):
    form = UserUpdateForm()
    if request.method == "POST":
        instance = get_object_or_404(MyUser, id=request.user.id)
        form = UserUpdateForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return render(request, 'account/detail_profile/update.html', {'success': "Nazwa została zmieniona"})
    return render(request, 'account/detail_profile/update.html', {'form': form})


@login_required(login_url=LOGIN_URL)
def delete_profile_view(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        return redirect('register')
    return render(request, 'account/detail_profile/delete.html', {})


@login_required(login_url=LOGIN_URL)
def password_change_view(request):
    form = UserPasswordChangeForm(request.user)
    if request.method == 'POST':
        instance = get_object_or_404(MyUser, id=request.user.id)
        form = UserPasswordChangeForm(instance, data=request.POST)
        if form.is_valid():
            form.save()
            print("przeszło walidacje, zapisano zmiany")
            update_session_auth_hash(request, form.user)
            return redirect('password_change')
    return render(request, 'account/detail_profile/password_change.html', {'form': form})




