# this is a URLcong inner webapp: polls to map url to the views of this app
from django.contrib import admin
from django.urls import include, path
from . import views

# todo:
# 1. add link back to mysite
# 2. optimize the layout of each page
# 3. admin page should have function to change choice
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name = 'detail'),
    path('<int:question_id>/results/', views.results, name = 'results'),
    path('<int:question_id>/vote/', views.vote, name = 'vote'),
]