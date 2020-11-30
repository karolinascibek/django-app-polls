from django.db import models
from django.utils import timezone

from account.models import MyUser

# Create your models here.


class Questionnaire(models.Model):
    creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=False) # czy udostepniona czy jeszcze w trakcie edycji, domyslnie w trakcie edycji
    type = models.BooleanField(default=False) # prywatna czy publiczna domyslnie publiczna
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    
