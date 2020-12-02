from django.db import models
from polls.questionnaire.models import Questionnaire
from django.utils import timezone

# Create your models here.


class CloseQuestion(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    number_of_choices = models.IntegerField(default=1)
    contents = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class OpenQuestion(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    is_number = models.BooleanField(default=True)
    contents = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
