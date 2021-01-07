from django import forms
from .models import Question


class QuestionCreateForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['contents', 'questionnaire', 'type']

# from .models import CloseQuestion, OpenQuestion
#
#
# class CloseQuestionCreateForm(forms.ModelForm):
#     class Meta:
#         model = CloseQuestion
#         fields = ['contents', 'questionnaire', 'number_of_choices']
#
#
# class OpenQuestionCreateForm(forms.ModelForm):
#     class Meta:
#         model = OpenQuestion
#         fields = ['contents', 'questionnaire', 'is_number']