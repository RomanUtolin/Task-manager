from django.test import Client
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.tasks.models import Task
from task_manager.tests.constants import TASK, UPDATE_TASK
from task_manager.tests.tets_mixins import MixinTestCase


class TasksTestCase(MixinTestCase):
    user = Client()
    user_2 = Client()
    user_3 = Client()
    redirect_url = reverse_lazy('tasks_page')

    def setUp(self):
        self.user.force_login(User.objects.get(pk=1))
        self.user_2.force_login(User.objects.get(pk=2))

    def test_task_open(self):
        url = reverse_lazy('open_task', args=(1,))
        get_response = self.user_2.get(url)
        self.assertEquals(get_response.status_code, 200)

    def test_task_create(self):
        url = reverse_lazy('create_task')
        get_response = self.user.get(url)
        post_response = self.user.post(url, TASK)
        task = Task.objects.get(name='Task')
        message = 'Task created successfully'
        self.get_crud_assert(get_response, post_response, message)
        self.assertTrue(task)

    def test_task_update(self):
        url = reverse_lazy('update_task', args=(1,))
        get_response = self.user_2.get(url)
        post_response = self.user_2.post(url, UPDATE_TASK)
        task = Task.objects.get(name='Update Task')
        message = 'Task changed successfully'
        self.get_crud_assert(get_response, post_response, message)
        self.assertTrue(task)

    def test_task_delete(self):
        url = reverse_lazy('delete_task', args=(1,))
        get_response = self.user_2.get(url)
        post_response = self.user_2.post(url)
        message = 'Task deleted successfully'
        self.get_crud_assert(get_response, post_response, message)
        with self.assertRaises(ObjectDoesNotExist):
            Task.objects.get(name='Django')

    def test_delete_no_permissions(self):
        url = reverse_lazy('delete_task', args=(1,))
        get_response = self.user.get(url)
        post_response = self.user.post(url)
        message = 'A task can only be deleted by its author.'
        self.get_permissions_assert(get_response, post_response, message, self.redirect_url)

    def test_not_authorized(self):
        url = reverse_lazy('create_task')
        get_response = self.user_3.get(url)
        post_response = self.user_3.post(url, TASK)
        message = 'You are not authorized! Please sign in.'
        redirect_url = self.login_page
        self.get_permissions_assert(get_response, post_response, message, redirect_url)
