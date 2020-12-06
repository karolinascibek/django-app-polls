from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from itertools import chain
from operator import attrgetter

from polls.questionnaire.models import Questionnaire
from django.db.models import Prefetch
from .forms import QuestionnaireForm

from polls.choice.models import Choice
from polls.question.models import Question

from django.contrib.auth.decorators import login_required
from mysite.settings import LOGIN_REDIRECT_URL, LOGIN_URL

# Create your views here.


@login_required(login_url=LOGIN_URL)
def questionnaire_create_view(request):
    if request.method == "POST":
        data = {
            'name': request.POST['name'],
            'creator': request.user,
            }
        form = QuestionnaireForm(data)
        if form.is_valid():
            new_quest = form.save()
            # print(new_quest)
            return redirect('detail_questionnaire', id=new_quest.id)
    return render(request, 'polls/questionnaire/create.html')


@login_required(login_url=LOGIN_URL)
def questionnaire_detail_view(request, id):
    questionnaire = get_object_or_404(Questionnaire, id=id)
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
    questionnaire = get_object_or_404(Questionnaire, id=id)
    if request.method == 'POST':
        questionnaire.name = request.POST['name']
        questionnaire.save()
        return redirect('detail_questionnaire', id=id)
    return render(request, 'polls/questionnaire/update.html', {'questionnaire': questionnaire})
