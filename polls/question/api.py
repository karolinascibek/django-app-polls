from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from mysite.settings import LOGIN_REDIRECT_URL, LOGIN_URL

import json
from django.http import JsonResponse

from polls.question.models import Question
from polls.choice.models import Choice

# Create your views here.


@login_required(login_url=LOGIN_URL)
def question_detail(request, id_question):
    question = get_object_or_404(Question, id=id_question)
    choices = []
    for ch in question.choice_set.all():
        choices.append(model_to_dict(ch))
    data = {
        'question': model_to_dict(question),
        'choices': choices,
    }
    print(data)
    return JsonResponse({'data': data})


@login_required(login_url=LOGIN_URL)
def question_update(request, id_question):
    question = get_object_or_404(Question, id=id_question)
    data = json.loads(request.body)
    if data['update_choices']:
        choices = []
        for choice in data['update_choices']:
            choice['question'] = question
            choices.append(Choice(**choice))
        Choice.objects.bulk_update(choices, ['contents'])
    if data['new_choices']:
        Choice.objects.bulk_create(
            [Choice(contents=choice['contents'], question=question) for choice in data['new_choices']]
        )
    if data['question']:
        new_question = data['question']
        question.contents = new_question['contents']
        question.type = new_question['type']
        question.save()
    return JsonResponse({"success": 'Zmiany zostały zapisane.'}, status=200)


# @login_required(login_url=LOGIN_URL)
# def close_question(request, id_question):
#     question = get_object_or_404(CloseQuestion, id=id_question)
#     choices = []
#     for ch in question.choice_set.all():
#         choices.append(model_to_dict(ch))
#     data = {
#         'question': model_to_dict(question),
#         'choices': choices,
#     }
#     return JsonResponse({'data': data})
#
#
# @login_required(login_url=LOGIN_URL)
# def close_question_update(request, id_question):
#     question = get_object_or_404(CloseQuestion, id=id_question)
#     data = json.loads(request.body)
#     if data['update_choices']:
#         choices = []
#         for choice in data['update_choices']:
#             choice['question'] = question
#             choices.append(Choice(**choice))
#         Choice.objects.bulk_update(choices, ['contents'])
#     if data['new_choices']:
#         Choice.objects.bulk_create(
#             [Choice(contents=choice['contents'], question=question) for choice in data['new_choices']]
#         )
#     if data['question']:
#         new_question = data['question']
#         question.contents = new_question['contents']
#         question.number_of_choices = new_question['number_of_choices']
#         question.save()
#     return JsonResponse({"success": 'Zmiany zostały zapisane.'}, status=200)
#
#
# @login_required(login_url=LOGIN_URL)
# def close_question_delete_api(request):
#     data = json.loads(request.body)
#     question = get_object_or_404(CloseQuestion, id=data['id'])
#     question.delete()
#     return JsonResponse({"success": 'Zmiany zostały zapisane.'}, status=200)
#
#
# def open_question_update_view(request, id, id_question):
#     return render(request, 'polls/question/open_question_update.html', {'questionnaire_id': id})