from django import test
from django.contrib.messages import get_messages
from django.urls import reverse_lazy


@test.modify_settings(MIDDLEWARE={'remove': [
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]})
class MixinTestCase(test.TestCase):
    fixtures = ['task.json', 'status.json', 'label.json', 'user.json']
    redirect_url = None
    login_page = reverse_lazy('login_page')

    def get_message(self, response):
        messages = list(get_messages(response.wsgi_request))
        return str(messages[0])

    def get_crud_assert(self, get_response, post_response, message):
        self.assertEqual(self.get_message(post_response), message)
        self.assertEquals(get_response.status_code, 200)
        self.assertEquals(post_response.status_code, 302)
        self.assertRedirects(post_response, self.redirect_url)

    def get_permissions_assert(self, get_response, post_response, message, redirect_url):
        self.assertEqual(self.get_message(get_response), message)
        self.assertEqual(self.get_message(post_response), message)
        self.assertEquals(get_response.status_code, 302)
        self.assertEquals(post_response.status_code, 302)
        self.assertRedirects(get_response, redirect_url)
        self.assertRedirects(post_response, redirect_url)
