from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page



    # Create your tests here.
class SMokeTest(TestCase):

    def test_bad_math(self):
          self.assertEqual(1+1,3)


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found= resolve("/")
        self.assertEqual(found.func,homepage)


    def test_hoe_page_return_correct_home(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startwith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endwith('</html>'))


