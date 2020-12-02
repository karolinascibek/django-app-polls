from django.shortcuts import render, redirect
from .forms import CloseQuestionCreateForm, OpenQuestionCreateForm
from polls.choice.forms import ChoiceCreateForm
from polls.questionnaire.models import Questionnaire
from polls.choice.models import Choice
# Create your views here.


def question_create_view(request, id):
    if request.method == 'POST':
        new_question = {
            'contents': request.POST.get('contents-question'),
            'questionnaire': Questionnaire.objects.get(id=id),
        }

        """ pytanie z opcjami do wyboru """
        if request.POST['type'] == 'choices':
            new_question['number_of_choices'] = request.POST.get('number_of_choices')
            form_question = CloseQuestionCreateForm(new_question)
            if form_question.is_valid():
                question = form_question.save()

                Choice.objects.bulk_create(
                    [Choice(contents=choice, question=question) for choice in request.POST.getlist('contents-choice')]
                )
                return redirect('detail_questionnaire', id=id)
            else:
                print(form_question.errors)

            """ pytanie otwarte z textem lub liczbą """
        elif request.POST['type'] == 'text' or request.POST['type'] == 'number':
            is_number = True
            if request.POST['type'] == 'text':
                is_number = False
            new_question['is_number'] = is_number
            form_question = OpenQuestionCreateForm(new_question)
            if form_question.is_valid():
                form_question.save()
                return redirect('detail_questionnaire', id=id)

    return render(request, 'polls/question/create.html', {'questionnaire_id': id})