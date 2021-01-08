from django.db.models import Count, Q
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
    analysis = choices.annotate(liczba=Count('closedanswer__choice')).order_by('question__pk', 'closedanswer__choice')
    analysis = analysis.values('question__contents','contents','liczba')

    questions = Question.objects.filter(Q(questionnaire=questionnaire) & (Q(type='single-choice') | Q(type='multiple-choice')))
    # analysis2 = questions.order_by('pk').annotate(liczba=Count('choice__closedanswer__choice')).values('pk','choice','liczba')
    print(analysis)
    context = {
        'message': "strona z analizą ankiety "+str(id),
        'questionnaire': questionnaire,
        'respondents': number_of_respondents,
        'analysis': analysis,
        #'analysis2': analysis2,
        }
    return render(request, "polls/analysis/analysis.html", context)