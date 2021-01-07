from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from mysite.settings import LOGIN_URL

from django.http import JsonResponse
from django.forms.models import model_to_dict

from polls.questionnaire.models import Questionnaire


# Create your views here.


def detail_questionnaire(request, id):

    questionnaire = get_object_or_404(Questionnaire, id=id)
    questions = []
    for question in questionnaire.question_set.all():
        choices = []
        for choice in question.choice_set.all():
            choices.append(model_to_dict(choice))
        question = model_to_dict(question)
        question['choices'] = choices
        questions.append(question)
    questionnaire = model_to_dict(questionnaire)
    questionnaire['questions'] = questions
    context = {
        'questionnaire': questionnaire
    }
    return JsonResponse({"data": context}, status=200)

