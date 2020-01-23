from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls_01/
    path('', views.index, name='index'),
    # ex: /polls_01/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls_01/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls_01/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]