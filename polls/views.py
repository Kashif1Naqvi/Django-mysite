from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# import model 
from .models import Question
# Create your views here.

# when everything is done then not need to load loder and httpResponce we do every thing with render


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list':latest_question_list,
    }
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    """
        A shortcut: get_object_or_404()
        It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut. Here’s the detail() view, rewritten:
        so this code
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request,'polls/detail.html',{'question':question})

        changed
    """
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})


def results(request,question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You're voting on question %s."%question_id)

