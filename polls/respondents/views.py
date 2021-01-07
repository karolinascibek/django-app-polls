from django.forms import model_to_dict
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from polls.respondents.models import Respondent, Answer, ClosedAnswer, OpenAnswer
from polls.questionnaire.models import Questionnaire
from polls.questionnaire.question.models import Question
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def respondent_questionnaires(request):
    questionnaires = Respondent.objects.filter(user=request.user)
    context = {'questionnaires': questionnaires}
    return render(request, "polls/respondent/questionnaires.html", context)


def respondent_questionnaire(request, id_questionnaire):
    respondent = Respondent.objects.filter(user=request.user, questionnaire__pk=id_questionnaire).first()
    questionnaire = respondent.questionnaire
    context = {'questionnaire': questionnaire}
    return render(request, "polls/respondent/questionnaire.html", context)