from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# todo:
# 1. upload score to the server SQL
# 2. add button to control the snake

# the first layout of an index -> need URLconf to link 
# index
def home(request):
    return render(request,"index.html",{})

def staticWeb_snake(request):
    return render(request, 'staticWeb/snake.html', {})