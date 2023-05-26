from django.test import Client
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.labels.models import Label
from task_manager.tests.tets_mixins import MixinTestCase


class LabelsTestCase(MixinTestCase):
    user = Client()
    user_2 = Client()
    redirect_url = reverse_lazy('labels_page')

    def setUp(self):
        self.user.force_login(User.objects.get(pk=1))

    def test_labels_list(self):
        url = reverse_lazy('labels_page')
        get_response = self.user.get(url)
        labels = get_response.context.get('labels')
        self.assertEquals(get_response.status_code, 200)
        self.assertEquals(len(labels), 2)

    def test_label_create(self):
        url = reverse_lazy('create_label')
        get_response = self.user.get(url)
        post_response = self.user.post(url, {'name': 'test_label'})
        label = Label.objects.get(name='test_label')
        message = 'Label created successfully'
        self.get_crud_assert(get_response, post_response, message)
        self.assertTrue(label)

    def test_label_update(self):
        url = reverse_lazy('update_label', args=(1,))
        get_response = self.user.get(url)
        post_response = self.user.post(url, {'name': 'Update'})
        label = Label.objects.get(name='Update')
        message = 'label changed successfully'
        self.get_crud_assert(get_response, post_response, message)
        self.assertTrue(label)

    def test_label_delete(self):
        url = reverse_lazy('delete_label', args=(2,))
        get_response = self.user.get(url)
        post_response = self.user.post(url)
        message = 'Label deleted successfully'
        self.get_crud_assert(get_response, post_response, message)
        with self.assertRaises(ObjectDoesNotExist):
            Label.objects.get(name='urgently')

    def test_delete_no_permissions(self):
        url = reverse_lazy('delete_label', args=(1,))
        get_response = self.user.get(url)
        post_response = self.user.post(url)
        message = "Can't delete label because it's in use"
        self.assertEqual(self.get_message(post_response), message)
        self.assertEquals(get_response.status_code, 200)
        self.assertEquals(post_response.status_code, 302)
        self.assertRedirects(post_response, self.redirect_url)

    def test_not_authorized(self):
        url = reverse_lazy('labels_page')
        get_response = self.user_2.get(url)
        post_response = self.user_2.post(url)
        message = 'You are not authorized! Please sign in.'
        redirect_url = self.login_page
        self.get_permissions_assert(get_response, post_response, message, redirect_url)
