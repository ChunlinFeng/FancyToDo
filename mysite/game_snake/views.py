from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import Ranking_Record
# Create your views here.

def index(request):
    ranking_set = Ranking_Record.objects.order_by('-score')[:5]
    std_list = []
    for ind,ele in enumerate(ranking_set):
        player_name = ele.player_name + '' * (20-len(ele.player_name))
        score, date = str(ele.score) + ' '*(4-len(str(ele.score))), str(ele.date)[:10]
        index = str(ind+1) + '.' + ' ' * (2-len(str(ind+1)))
        std_list.append(index + ' ' + date + ' | ' + player_name + ' | ' + score )
    
    context = {
        'ranking_list' : std_list,
        'message': '',
    }
    message = ''
    try:
        message = request.GET['message']
    except(KeyError):
        message = ''
    else:
        context['message'] = message

    return render(request,'game_snake/index.html', context)
    
def ranking_upload(request):
    try:
        player_name = request.POST['player_name']
        score = int(request.POST['score'])
        date = timezone.now()
    except(KeyError, Ranking_Record.DoesNotExist):
        context = {
            'error_message': "You didn't enter a valid name.",
        }
        return render(request, 'game_snake/', context)
    else:
        record = Ranking_Record()
        record.add_new_record(player_name, score, date)
        record.save()

        # todo: use a better way to save ranking details
        ranking_message = '?message='
        ranking_list = Ranking_Record.objects.order_by('-score')
        print(len(ranking_list))
        for ind in range(len(ranking_list)):
            if ranking_list[ind].score == score:
                ranking_message += 'You has achieved NO.' + str(ind+1) + ' last time!'
                break

        return HttpResponseRedirect('/game_snake/' + ranking_message)