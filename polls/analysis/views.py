from django.db.models import Count, Q, Avg, StdDev, Sum
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
    number_of_respondents = number_of_respondents['questionnaire__count']

    choices = Choice.objects.filter(question__questionnaire=questionnaire)

    answers_choice = Count('closedanswer__choice')
    analysis_choices = choices.annotate(liczba= answers_choice).annotate(proc=answers_choice/number_of_respondents*100)
    analysis_choices = analysis_choices.order_by('question__pk', 'closedanswer__choice')
    analysis_choices = analysis_choices.values('question__id', 'question__contents', 'id', 'contents',
                                               'liczba', 'question__type', 'proc')

    closed_questions = analysis_choices.values('question__id', 'question__contents').order_by('question__id').distinct()

    for q in closed_questions:
        a = analysis_choices.filter(question__id= q['question__id'])
        q['choices'] = a

    questions = Question.objects.filter(questionnaire=questionnaire)
    questions_open_text = questions.filter(type='text').order_by('id')
    column = 'answer__openanswer__contents'
    questions_open_number = questions.filter(type='number')\
        .annotate(avg=Avg(column))\
        .annotate(sum=Sum(column))\
        .annotate(stan_dev=StdDev(column)).order_by('id')

    context = {
        'message': "strona z analizą ankiety "+str(id),
        'questionnaire': questionnaire,
        'respondents': number_of_respondents,
        'analysis': analysis_choices,
        'questions_open_text': questions_open_text,
        'questions_open_number': questions_open_number,
        'closed_questions': closed_questions

        }
    return render(request, "polls/analysis/analysis.html", context)