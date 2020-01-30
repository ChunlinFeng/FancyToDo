from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Ranking_Record
# Create your views here.

def index(request):
    ranking_list = Ranking_Record.objects.order_by('-score')[:10]
    context = {
        'ranking_list' : ranking_list,
    }
    return render(request,'game_snake/index.html', context)
    
def ranking_upload(request):
    try:
        player_name = request.POST['player_name']
        score = request.POST['score']
        date = request.POST['date']
    except(KeyError, Ranking_Record.DoesNotExist):
        context = {
            'error_message': "You didn't enter a valid name.",
        }
        return render(request, 'game_snake/', context)
    else:
        record = Ranking_Record()
        record.add_new_record(player_name, score, date)
        record.save()

        ranking = 0
        ranking_list = Ranking_Record.objects.order_by('-score')
        for ind in range(len(ranking_list)):
            if ranking_list[ind].score == score:
                ranking = ind
                break

        context = {
            'ranking_list' : ranking_list[:10],
            'ranking': ranking
        }

        return HttpResponseRedirect(render(request, 'game_snake:index', context))