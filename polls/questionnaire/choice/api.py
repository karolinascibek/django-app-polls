from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from mysite.settings import LOGIN_URL

import json
from django.http import JsonResponse

from polls.questionnaire.choice.models import Choice
# Create your views here.

#
# # @login_required(login_url=LOGIN_URL)
# # def choice_update_api(request, id_question):
# #     question = get_object_or_404(CloseQuestion,id=id_question)
# #     choices = []
# #     data = json.loads(request.body)
# #     for choice in data:
# #         choice['question'] = question
# #         choices.append(Choice(**choice))
# #     Choice.objects.bulk_update(choices, ['contents'])
# #     return JsonResponse({"success": 'Zmiany zostały zapisane.'})
#
# #
# # @login_required(login_url=LOGIN_URL)
# # def choice_create_api(request, id_question):
# #     question = get_object_or_404(CloseQuestion, id=id_question)
# #     data = json.loads(request.body)
# #     Choice.objects.bulk_create(
# #         [Choice(contents=choice['contents'], question=question) for choice in data]
# #     )
# #     return JsonResponse({"success": 'Zmiany zostały zapisane.'})
#
#


@login_required(login_url=LOGIN_URL)
def choice_delete_api(request):
    data = json.loads(request.body)
    choice = get_object_or_404(Choice, id=data['id'])
    choice.delete()
    return JsonResponse({"success": 'Zmiany zostały zapisane.'})