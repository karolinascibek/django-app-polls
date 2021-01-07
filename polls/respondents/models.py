from django.db import models
from account.models import MyUser
from polls.questionnaire.models import Questionnaire
from polls.questionnaire.question.models import Question
from polls.questionnaire.choice.models import Choice
# Create your models here.


class Respondent(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    respondent = models.ForeignKey(Respondent, on_delete=models.CASCADE, null=True)


class ClosedAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)


class OpenAnswer(models.Model):
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE)
    contents = models.TextField(max_length=500)
