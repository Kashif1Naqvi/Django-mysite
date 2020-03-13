import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls import reverse

# Create your tests here.

class QuestionModelTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """ was_published_recently returns false for question whose pub_date is in the future """  
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(),False)


    def test_was_published_recently_with_old_question(self):
        """ was_published_recently returns False for questions whose pub_date is older than 1 day """ 
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date = time)
        self.assertIs(old_question.was_published_recently(),False)
      

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.was_published_recently(),True)

    def create_question(question_text,days):
        """  
          create a question with the given 'question_text' and published the given number of 'days' offset to now ( nagitive to test published 
          in the past , positive for questions that have yet to be published)
        """
        time = timezone.now() = datetime.timedelta(days=days)
        return Question.objects.create(question_text=question_text,pub_date=time)

    class QuestionIndexViewTests(TestCase):
        def test_no_question(self):
            """
              If no questions exists, an appropriate message is displayed
            """

            responce = self.client.get(reverse('polls:index'))
            self.assertEqual(responce.status_code,200)
            self.assertContains(responce,'No polls are available!')
            self.assertQuerysetEqual(responce.context['latest_question_list'],[])

        def past_question(self):
            """
              Questions with a pub_date  in the past are displayed on the index page
            """
            create_question(question_text='Past questions',days=-30)
            responce = self.client.get(reverse('polls:index'))
            self.assertQuerysetEqual(
              responce.context['latest_question_list'],['<Question: Past question.>']
            )
        def test_future_question(self):
            """
              Question with pub_date in the future aren't displayed on the index page
            """
            create_question(question_text='Future questions',days=30)
            responce = self.client.get(reverse('polls:index'))
            self.assertContains(responce,'No Polls Are Available')
            self.assertQuerysetEqual(
              responce.context['latest_question_list'],[]
            )
        def test_future_question_and_past_question(self):
            """
              Even if both past and future question exists ,only past question is displayed
            """
            create_question(question_text="Past question",days=-30)
            create_question(question_text="Future question",days=30)
            responce = self.client.get(reverse('polls:index'))
            self.assertQuerysetEqual(
                responce.context['latest_question_list'],['<Question:Past question.>']
            )