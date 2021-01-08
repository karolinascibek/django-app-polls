from django.shortcuts import render
from polls.questionnaire.models import Questionnaire
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.


def analysis_view(request, id):
    questionnaire = get_object_or_404(Questionnaire, pk=id)
    analysis = questionnaire
    context = {
        'message': "strona z analizą ankiety "+str(id),
        'questionnaire': questionnaire,
               }
    return render(request, "polls/analysis/analysis.html", context)