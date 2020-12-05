from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.forms.models import model_to_dict

import json
from django.http import JsonResponse
from django.utils.safestring import SafeString

from django.contrib.auth.decorators import login_required
from mysite.settings import LOGIN_REDIRECT_URL, LOGIN_URL

from polls.choice.forms import ChoiceCreateForm
from polls.question.forms import QuestionCreateForm
from polls.questionnaire.models import Questionnaire
from polls.question.models import Question
from polls.choice.models import Choice

# Create your views here.


@login_required(login_url=LOGIN_URL)
def question_create_view(request, id):
    if request.method == "POST":
        contents = request.POST.get('contents-question')
        questionnaire = Questionnaire.objects.get(id=id)
        """ pytanie z opcjami do wyboru """
        question = Question(contents=contents, questionnaire=questionnaire, type=request.POST['type'])
        question.save()
        if request.POST['type'] == 'choices':
            Choice.objects.bulk_create(
                [Choice(contents=choice, question=question) for choice in request.POST.getlist('contents-choice')]
            )
            return redirect('detail_questionnaire', id=id)

            """ pytanie otwarte z textem lub liczbą """
        elif request.POST['type'] == 'text':
            question = Question(contents=contents, questionnaire=questionnaire, type='text').save()
        elif request.POST['type'] == 'number':
            question = Question(contents=contents, questionnaire=questionnaire, type='number').save()

    return render(request, 'polls/question/create.html', {'questionnaire_id': id})


@login_required(login_url=LOGIN_URL)
def close_question_update_view(request, id, id_question):
    question = get_object_or_404(Question, id=id_question)
    context = {
        'questionnaire_id': id,
        'question': question
    }
    return render(request, 'polls/question/close_question_update.html', context)

#
# def open_question_update_view(request, id, id_question):
#     return render(request, 'polls/question/open_question_update.html', {'questionnaire_id': id})