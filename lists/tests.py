from django.test import TestCase


# Create your tests here.

class HomepPageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/') # We deleted the old test_root_​url_resolves test, because that’s tested implicitly by the Django Test Client

        self.assertTemplateUsed(response, 'home.html')
