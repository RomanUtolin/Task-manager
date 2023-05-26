from django.test import Client
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.tests.constants import USER, UPDATE_USER
from task_manager.tests.tets_mixins import MixinTestCase


class UserTestCase(MixinTestCase):
    user = Client()
    user_2 = Client()
    user_3 = Client()

    def setUp(self):
        self.user.force_login(User.objects.get(pk=1))
        self.user_2.force_login(User.objects.get(pk=2))

    def test_user_list(self):
        url = reverse_lazy('users_page')
        get_response = self.user.get(url)
        users = get_response.context.get('users')
        self.assertEquals(get_response.status_code, 200)
        self.assertEquals(len(users), 2)

    def test_user_create(self):
        url = reverse_lazy('create_user')
        get_response = self.user_3.get(url)
        post_response = self.user_3.post(url, USER)
        user = User.objects.get(username='User')
        message = 'User successfully registered'
        self.redirect_url = reverse_lazy('login_page')
        self.get_crud_assert(get_response, post_response, message)
        self.assertTrue(user)

    def test_user_update(self):
        url = reverse_lazy('update_user', args=(1,))
        get_response = self.user.get(url)
        post_response = self.user.post(url, UPDATE_USER)
        user = User.objects.get(username='Update_User')
        message = 'User changed successfully'
        self.redirect_url = reverse_lazy('users_page')
        self.get_crud_assert(get_response, post_response, message)
        self.assertTrue(user)

    def test_delete(self):
        url = reverse_lazy('delete_user', args=(1,))
        get_response = self.user.get(url)
        post_response = self.user.post(url)
        message = 'User deleted successfully'
        self.redirect_url = reverse_lazy('index')
        self.get_crud_assert(get_response, post_response, message)
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(username='User_1')

    def test_delete_use_user(self):
        url = reverse_lazy('delete_user', args=(2,))
        get_response = self.user_2.get(url)
        post_response = self.user_2.post(url)
        redirect_url = reverse_lazy('users_page')
        message = 'Cannot delete user because it is in use'
        self.assertEqual(self.get_message(post_response), message)
        self.assertEquals(get_response.status_code, 200)
        self.assertEquals(post_response.status_code, 302)
        self.assertRedirects(post_response, redirect_url)

    def test_user_no_permissions(self):
        update_url = reverse_lazy('update_user', args=(1,))
        get_response = self.user_2.get(update_url)
        post_response = self.user_2.post(update_url, UPDATE_USER)
        message = 'No rights to change another user'
        redirect_url = reverse_lazy('users_page')
        self.get_permissions_assert(get_response, post_response, message, redirect_url)

    def test_user_not_authorized(self):
        url = reverse_lazy('update_user', args=(1,))
        get_response = self.user_3.get(url)
        post_response = self.user_3.post(url, UPDATE_USER)
        message = 'You are not authorized! Please sign in.'
        redirect_url = self.login_page
        self.get_permissions_assert(get_response, post_response, message, redirect_url)
