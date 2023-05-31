from django.contrib.messages import get_messages
from django.test import TestCase, Client
from django.urls import reverse_lazy
from django.contrib.auth import get_user
from task_manager.users.models import User


class IndexTestCase(TestCase):
    user = Client()
    user_2 = Client()

    def get_message(self, response):
        messages = list(get_messages(response.wsgi_request))
        return str(messages[0])

    def setUp(self):
        test_user = User.objects.create(username='test_user')
        test_user.set_password('12345')
        test_user.save()

    def test_login(self):
        url = reverse_lazy('login_page')
        get_response = self.user.get(url)
        post_response = self.user.post(url, {'username': 'test_user', 'password': '12345'})
        authenticated_get_response = self.user.get(url)
        message = 'You are logged in'
        self.assertEquals(get_response.status_code, 200)
        self.assertEquals(post_response.status_code, 302)
        self.assertEqual(self.get_message(post_response), message)
        self.assertTrue(get_user(self.user).is_authenticated)
        self.assertFalse(get_user(self.user_2).is_authenticated)
        self.assertRedirects(post_response, reverse_lazy('index'))
        self.assertEquals(authenticated_get_response.status_code, 302)
        self.assertRedirects(authenticated_get_response, reverse_lazy('index'))

    def test_logout(self):
        url = reverse_lazy('logout')
        self.user.force_login(User.objects.get(username='test_user'))
        get_response = self.user.get(url)
        message = 'You are logged out'
        self.assertEquals(get_response.status_code, 302)
        self.assertFalse(get_user(self.user).is_authenticated)
        self.assertRedirects(get_response, reverse_lazy('index'))
        self.assertEqual(self.get_message(get_response), message)

    def test_index(self):
        url = reverse_lazy('index')
        get_response = self.user.get(url)
        self.assertEquals(get_response.status_code, 200)
