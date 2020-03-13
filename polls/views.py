from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
# import model 
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Question,Choice
# Create your views here.

# when everything is done then not need to load loder and httpResponce we do every thing with render


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the five published questions (not including those set to be published in the future) """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
            Excludes any question that aren't published yet
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results' ,args=(question.id,) ))

    




"""     in detail() function  get_object_or_404() used
        It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. Django provides a shortcut. Here’s the detail() view, rewritten:
        so this code
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request,'polls/detail.html',{'question':question})

        changed
    """