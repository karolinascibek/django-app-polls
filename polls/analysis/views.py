from django.db.models import Count, Q, Avg, StdDev
from django.forms import model_to_dict
from django.shortcuts import render
from polls.questionnaire.models import Questionnaire
from polls.questionnaire.question.models import Question
from polls.questionnaire.choice.models import Choice
from polls.respondents.models import Respondent
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .my_function import check_list_index
from mysite.settings import LOGIN_URL
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url=LOGIN_URL)
def analysis_view(request, id):
    questionnaire = get_object_or_404(Questionnaire, pk=id, creator=request.user)
    number_of_respondents = Respondent.objects.filter(questionnaire=questionnaire).aggregate(Count('questionnaire'))
    choices = Choice.objects.filter(question__questionnaire=questionnaire)
    analysis_choices = choices.annotate(liczba=Count('closedanswer__choice')).order_by('question__pk', 'closedanswer__choice')
    analysis_choices = analysis_choices.values('question__contents', 'contents', 'liczba', 'question__type')
    analisis_open = Question.objects.filter(questionnaire=questionnaire)
    analisis_open = analisis_open.filter(Q(type='text') | Q(type='number')).order_by('id')
    print(analisis_open)
    context = {
        'message': "strona z analizą ankiety "+str(id),
        'questionnaire': questionnaire,
        'respondents': number_of_respondents,
        'analysis': analysis_choices,
        'analysis_open': analisis_open,

        }
    return render(request, "polls/analysis/analysis.html", context)