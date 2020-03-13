from django.urls import path
from . import views
# if you have a more app then fix the app name also that route is equal to this app that we used 
app_name = 'polls'
urlpatterns = [
    # /polls
    path('' , views.IndexView.as_view() , name="index" ),
    
    #/polls/5(or any id)
    path=('<int:pk>/', views.DetailView.as_view() , name='detail' )
    # /polls/5/result/
    path('<int:pk>/results',views.ResultsView.as_view(), name="results"),
    # /polls/5/vote/
    path('<int:question_id>/vote/', views.vote , name="vote" ),
]