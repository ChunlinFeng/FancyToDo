import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')

    def __repr__(self):
        return "Question Object is represented as: " + self.question_text

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        if self.pub_date >= timezone.now() - datetime.timedelta(hours = 10):
            return True
        else:
            return False


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __repr__(self):
        # print('This choice linked to ' + str(self.question))
        # return "Choice Object is represented as " + self.choice_text
        return self.choice_text

    def __str__(self):
        return self.choice_text