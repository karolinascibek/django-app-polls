from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from mysite.settings import LOGIN_URL

from polls.questionnaire.models import Questionnaire
from polls.questionnaire.question.models import Question
from polls.questionnaire.choice.models import Choice

# Create your views here.


@login_required(login_url=LOGIN_URL)
def question_create_view(request, id):
    questionnaire = Questionnaire.objects.get(id=id)
    if request.method == "POST":
        contents = request.POST.get('contents-question')
        number_of_choices = 1
        if request.POST['type'] == 'multiple-choice':
            number_of_choices = int(request.POST['number_of_choices'])
        question = Question(contents=contents, questionnaire=questionnaire, type=request.POST['type'], number_of_choices=number_of_choices )
        question.save()
        if request.POST['type'] == 'single-choice' or request.POST['type'] == 'multiple-choice':
            Choice.objects.bulk_create(
                [Choice(contents=choice, question=question) for choice in request.POST.getlist('contents-choice')]
            )
        return redirect('detail_questionnaire', id=id)
    return render(request, 'polls/question/create.html', {'questionnaire': questionnaire})


@login_required(login_url=LOGIN_URL)
def question_update_view(request, id_question):
    question = get_object_or_404(Question, id=id_question)
    questionnaire = get_object_or_404(Questionnaire, id=question.questionnaire.id)
    print("questionnaire --- ")
    print(questionnaire)
    context = {
        'questionnaire': questionnaire,
        'question': question
    }
    return render(request, 'polls/question/update.html', context)


@login_required(login_url=LOGIN_URL)
def question_delete_view(request, id_question):
    question = get_object_or_404(Question, id=id_question)
    question.delete()
    print('question delete view -----------')
    return redirect('detail_questionnaire', id=question.questionnaire.id)
