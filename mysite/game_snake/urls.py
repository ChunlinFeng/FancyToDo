# this is a URLcong inner webapp: game_snake to map url to the views of this app
from django.contrib import admin
from django.urls import include, path
from . import views


app_name = 'game_snake'
urlpatterns = [
    path('', views.index, name='index'),
    path('ranking_upload', views.ranking_upload, name='ranking_upload'),
    
]