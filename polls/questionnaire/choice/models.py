from django.db import models
from polls.questionnaire.question.models import Question
from django.utils import timezone

# Create your models here.


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    is_answer = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

