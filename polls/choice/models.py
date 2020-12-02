from django.db import models
from polls.question.models import CloseQuestion
from django.utils import timezone

# Create your models here.


class Choice(models.Model):
    question = models.ForeignKey(CloseQuestion, on_delete=models.CASCADE)
    contents = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

