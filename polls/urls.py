from django.urls import path
from . import views

urlpatterns = [
    # /polls
    path('' , views.index , name = "index" ),
    #/polls/5(or any id)
    path('<int:question_id>/', views.detail , name="detail" )     ,
    # /polls/5/result/
    path('<int:question_id>/results',views.results, name="results"),
    # /polls/5/vote/
    path('<int:question_id>/vote', views.vote , name="vote" ),
]