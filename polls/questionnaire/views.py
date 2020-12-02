from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from itertools import chain
from operator import attrgetter

from polls.questionnaire.models import Questionnaire
from django.db.models import Prefetch
from .forms import QuestionnaireForm

from polls.choice.models import Choice
from polls.question.models import CloseQuestion, OpenQuestion

# Create your views here.


def questionnaire_create_view(request):
    if request.method == "POST":
        data = {
            'name': request.POST['name'],
            'creator': request.user,
            }
        form = QuestionnaireForm(data)
        if form.is_valid():
            new_quest = form.save()
            print(new_quest)
            return redirect('detail_questionnaire', id=new_quest.id)
    return render(request, 'polls/questionnaire/create.html')


def questionnaire_detail_view(request, id):
    questionnaire = get_object_or_404(Questionnaire, id=id)
    close_questions = CloseQuestion.objects.filter(questionnaire__id=id)
    open_questions = OpenQuestion.objects.filter(questionnaire__id=id)
    questions = sorted(
        chain(close_questions, open_questions),
        key=attrgetter('created_at'))
    print(questions)
    context = {
        'questionnaire': questionnaire,
        'questions': questions
    }
    return render(request, 'polls/questionnaire/detail.html', context)
