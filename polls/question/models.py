from django.db import models
from polls.questionnaire.models import Questionnaire
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    type = models.CharField(max_length=30)
    number_of_choices = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


# class CloseQuestion(models.Model):
#     number_of_choices = models.IntegerField(default=1)
#
#
# class OpenQuestion(models.Model):
#     is_number = models.BooleanField(default=True)

