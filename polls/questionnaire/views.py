from django.shortcuts import render, redirect, get_object_or_404

from django.utils.crypto import get_random_string

from polls.questionnaire.models import Questionnaire
from .forms import QuestionnaireForm
from .my_function import answers_save
from polls.questionnaire.question.models import Question
from polls.respondents.models import Respondent, Answer, ClosedAnswer, OpenAnswer

from django.contrib.auth.decorators import login_required
from mysite.settings import LOGIN_URL

import random

# Create your views here.


@login_required(login_url=LOGIN_URL)
def questionnaire_create_view(request):
    if request.method == "POST":
        data = {
            'name': request.POST['name'],
            'creator': request.user,
            'code': get_random_string(random.randint(5, 10))
            }

        form = QuestionnaireForm(data)
        if form.is_valid():
            new_quest = form.save()
            # print(new_quest)
            return redirect('detail_questionnaire', id=new_quest.id)
    return render(request, 'polls/questionnaire/create.html')


@login_required(login_url=LOGIN_URL)
def questionnaire_detail_view(request, id):
    questionnaire = get_object_or_404(Questionnaire, id=id , creator=request.user)
    questions = Question.objects.filter(questionnaire__id=id)
    context = {
        'questionnaire': questionnaire,
        'questions': questions,
        'id': id,
    }
    return render(request, 'polls/questionnaire/detail.html', context)


@login_required(login_url=LOGIN_URL)
def questionnaire_delete_view(request, id):
    if request.method == 'POST':
        questionnaire = get_object_or_404(Questionnaire, id=id)
        questionnaire.delete()
        return redirect('index')
    return redirect('detail_questionnaire', id=id)


@login_required(login_url=LOGIN_URL)
def questionnaire_update_view(request, id):
    questionnaire = get_object_or_404(Questionnaire, id=id, creator=request.user)
    if request.method == 'POST':
        questionnaire.name = request.POST['name']
        questionnaire.save()
        return redirect('detail_questionnaire', id=id)
    return render(request, 'polls/questionnaire/update.html', {'questionnaire': questionnaire})


@login_required(login_url=LOGIN_URL)
def questionnaire_share_view(request, id):
    questionnaire = get_object_or_404(Questionnaire, id=id,creator=request.user)
    context = {
        'questionnaire': questionnaire,
    }
    if request.method == "POST":
        questionnaire.type = request.POST['type']
        questionnaire.status = True
        questionnaire.save()
        context['status'] = questionnaire.status
        print('ankieta udostępniona ------ ')
    return render(request, 'polls/questionnaire/share.html', context)


# questionnaire view for the respondent
def questionnaire_display_view(request, questionnaire_code):
    questionnaire = get_object_or_404(Questionnaire, code=questionnaire_code)
    context = {}

    if request.user.is_authenticated and Respondent.objects.filter(user=request.user, questionnaire=questionnaire):
        context['message'] = "Ankieta została przez ciebie już wypełniona"
        return render(request, "polls/respondent/questionnaire_sent.html", context)

    if request.method == "GET":
        if not questionnaire.status or (questionnaire.type == 'private' and not request.user.is_authenticated):
            context['message'] = "Aby wypełnić to ankiete musisz byc zalogowany"
        context['questionnaire'] = questionnaire
        return render(request, 'polls/questionnaire/respondent/questionnaire.html', context)

    if request.method == "POST":
        respondent = None
        if request.user.is_authenticated:
            respondent = request.user

        respondent = Respondent.objects.create(user=respondent, questionnaire=questionnaire)
        print(request.POST)
        dict = request.POST.copy()
        dict.pop("csrfmiddlewaretoken")
        answers_save(respondent, questionnaire, dict)
        context = {"message": "Dziękujmey za wypełnienie ankiety. użtkownikowi = " + str(request.user) + " ankiety: " + str(questionnaire_code)}
        return render(request, "polls/respondent/questionnaire_sent.html", context)


def questionnaires_view(request):
    if request.user.is_authenticated:
        print('user zalogowany')
        questionnaires = Questionnaire.objects.filter(status=True)
    else:
        print('ankiety publiczne')
        questionnaires = Questionnaire.objects.filter(type='public', status=True)
    return render(request,'polls/questionnaire/questionnaires.html', {'questionnaires': questionnaires})


def questionnaires_search_view(request):
    return render(request, 'polls/questionnaire/questionnaires.html', {
        'questionnaires': Questionnaire.objects.filter(type='public', status=True)})