import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    def __str__(self):
        return self.choice_text



class Note(models.Model):
    note_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    private = models.BooleanField()
    def __str__(self):
        return self.note_text