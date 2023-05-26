from django.test import Client
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.tests.tets_mixins import MixinTestCase


class StatusesTestCase(MixinTestCase):
    user = Client()
    user_2 = Client()
    redirect_url = reverse_lazy('statuses_page')

    def setUp(self):
        self.user.force_login(User.objects.get(pk=1))

    def test_status_create(self):
        url = reverse_lazy('create_status')
        get_response = self.user.get(url)
        post_response = self.user.post(url, {'name': 'test_status'})
        status = Status.objects.get(name='test_status')
        message = 'Status successfully registered'
        self.get_crud_assert(get_response, post_response, message)
        self.assertTrue(status)

    def test_status_update(self):
        url = reverse_lazy('update_status', args=(1,))
        get_response = self.user.get(url)
        post_response = self.user.post(url, {'name': 'Update'})
        status = Status.objects.get(name='Update')
        message = 'Status changed successfully'
        self.get_crud_assert(get_response, post_response, message)
        self.assertTrue(status)

    def test_task_delete(self):
        url = reverse_lazy('delete_status', args=(2,))
        get_response = self.user.get(url)
        post_response = self.user.post(url)
        message = 'Status deleted successfully'
        self.get_crud_assert(get_response, post_response, message)
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(name='Open')

    def test_delete_no_permissions(self):
        url = reverse_lazy('delete_status', args=(1,))
        get_response = self.user.get(url)
        post_response = self.user.post(url)
        message = "Can't delete status because it's in use"
        self.assertEqual(self.get_message(post_response), message)
        self.assertEquals(get_response.status_code, 200)
        self.assertEquals(post_response.status_code, 302)
        self.assertRedirects(post_response, self.redirect_url)

    def test_not_authorized(self):
        url = reverse_lazy('statuses_page')
        get_response = self.user_2.get(url)
        post_response = self.user_2.post(url)
        message = 'You are not authorized! Please sign in.'
        redirect_url = self.login_page
        self.get_permissions_assert(get_response, post_response, message, redirect_url)
