import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.core.urlresolvers import reverse
def create_question(question_text, days):

    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text,
                                   pub_date=time)
class QuestionIndexDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        future_question = create_question(question_text='Future question.',
                                          days=5)
        response = self.client.get(reverse('polls:detail',
                                   args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        past_question = create_question(question_text='Past Question.',
                                        days=-5)
        response = self.client.get(reverse('polls:detail',
                                   args=(past_question.id,)))
        self.assertContains(response, past_question.question_text,
                            status_code=200)



"""
class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_past_qt(self):
        time= timezone.now() - datetime.timedelta(days=30)
        past_qt= Question(pub_date=time)
        self.assertEqual(past_qt.was_published_recently(),  False)

    def test_was_published_recently_now_qt(self):
        time= timezone.now() - datetime.timedelta(hours=2)
        now_qt= Question(pub_date=time)
        self.assertEqual(now_qt.was_published_recently(),  True)

"""