from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.messages import get_messages
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.tests.constants import USER, UPDATE_USER


class UserTestCase(TestCase):
    fixtures = ['task.json', 'status.json', 'label.json', 'user.json']

    def setUp(self):
        self.test_user1 = User.objects.get(pk=1)
        self.test_user2 = User.objects.get(pk=2)

    def test_user_create(self):
        url = reverse_lazy('create_user')
        get_response = self.client.get(url)
        post_response = self.client.post(url, USER)
        user = User.objects.get(username='User')
        messages = list(get_messages(post_response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'User successfully registered')
        self.assertEquals(get_response.status_code, 200)
        self.assertEquals(post_response.status_code, 302)
        self.assertRedirects(post_response, reverse_lazy('login_page'))
        self.assertTrue(user)

    def test_user_update(self):
        user = self.client
        user.force_login(self.test_user1)
        url = reverse_lazy('update_user', args=(1,))
        get_response = user.get(url)
        post_response = user.post(url, UPDATE_USER)
        user = User.objects.get(username='Update_User')
        messages = list(get_messages(post_response.wsgi_request))
        self.assertEqual(str(messages[0]), 'User changed successfully')
        self.assertEquals(get_response.status_code, 200)
        self.assertEquals(post_response.status_code, 302)
        self.assertRedirects(post_response, reverse_lazy('users_page'))
        self.assertTrue(user)

    def test_delete(self):
        user = self.client
        user.force_login(self.test_user1)
        url = reverse_lazy('delete_user', args=(1,))
        get_response = user.get(url)
        post_response = user.post(url)
        messages = list(get_messages(post_response.wsgi_request))
        self.assertEqual(str(messages[0]), 'User deleted successfully')
        self.assertEquals(get_response.status_code, 200)
        self.assertEquals(post_response.status_code, 302)
        self.assertRedirects(post_response, reverse_lazy('index'))
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(username=self.test_user1.username)

    def test_delete_use_user(self):
        user = self.client
        user.force_login(self.test_user2)
        url = reverse_lazy('delete_user', args=(2,))
        post_response = user.post(url)
        messages = list(get_messages(post_response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Cannot delete user because it is in use')
        self.assertEquals(post_response.status_code, 302)
        self.assertRedirects(post_response, reverse_lazy('users_page'))

    def test_user_no_permissions(self):
        user = self.client
        user.force_login(self.test_user2)
        update_url = reverse_lazy('update_user', args=(1,))
        get_response = user.get(update_url)
        post_response = user.post(update_url, UPDATE_USER)
        messages = list(get_messages(post_response.wsgi_request))
        self.assertEqual(str(messages[0]), 'No rights to change another user')
        self.assertEquals(get_response.status_code, 302)
        self.assertEquals(post_response.status_code, 302)
        self.assertRedirects(post_response, reverse_lazy('users_page'))
        self.assertRedirects(get_response, reverse_lazy('users_page'))

    def test_user_not_authorized(self):
        url = reverse_lazy('update_user', args=(1,))
        user = self.client
        get_response = user.get(url)
        post_response = user.post(url, UPDATE_USER)
        messages = list(get_messages(get_response.wsgi_request))
        self.assertEqual(str(messages[0]), 'You are not authorized! Please sign in.')
        self.assertEquals(get_response.status_code, 302)
        self.assertEquals(post_response.status_code, 302)
        self.assertRedirects(get_response, reverse_lazy('login_page'))
        self.assertRedirects(post_response, reverse_lazy('login_page'))
