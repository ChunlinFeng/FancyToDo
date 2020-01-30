# SQL models for game_snake Ranking
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Ranking_Record(models.Model):
    player_name = models.CharField(max_length= 15)
    score = models.IntegerField(default=0)
    date = models.DateTimeField('record date')

    def add_new_record(self, player_name, score, date):
        self.player_name = player_name
        self.score = score
        self.date = date

    def __str__(self):
        return str(self.date) + '->' + self.player_name + ': ' + str(self.score)
    
        