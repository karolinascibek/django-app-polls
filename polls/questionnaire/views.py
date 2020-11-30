from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from polls.questionnaire.models import Questionnaire
from .forms import QuestionnaireForm

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
    return render(request, 'polls/questionnaire/detail.html',{'questionnaire': questionnaire})
