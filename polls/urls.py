from django.urls import path
from . import views
# if you have a more app then fix the app name also that route is equal to this app that we used 
app_name = 'polls'
urlpatterns = [
    # /polls
    path('' , views.index , name="index" ),
    #/polls/5(or any id)
    path('<int:question_id>/', views.detail , name="detail" )     ,
    # /polls/5/result/
    path('<int:question_id>/results',views.results, name="results"),
    # /polls/5/vote/
    path('<int:question_id>/vote', views.vote , name="vote" ),
]