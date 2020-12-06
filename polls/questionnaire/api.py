from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from mysite.settings import LOGIN_REDIRECT_URL, LOGIN_URL

import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

from polls.questionnaire.models import Questionnaire
from polls.question.models import Question

# Create your views here.


@login_required(login_url=LOGIN_URL)
def detail_questionnaire(request, id):
    questionnaire = get_object_or_404(Questionnaire, id=id)
    questions = []
    for question in questionnaire.question_set.all():
        choices = []
        for ch in question.choice_set.all():
            choices.append(model_to_dict(ch))
        data = {'question': model_to_dict(question), 'choices': choices}
        questions.append(data)
    context = {
        'questionnaire': model_to_dict(questionnaire),
        'questions': questions
    }
    return JsonResponse({"data": context}, status=200)