from django.test import TestCase
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.labels.models import Label
from task_manager.statuses.models import Status


class TaskTestCase(TestCase):
    def setUp(self):
        autor = User.objects.create(username='autor')
        executor = User.objects.create(username='executor')
        status = Status.objects.create(name='test_status')
        label_1 = Label.objects.create(name='test_label_1')
        label_2 = Label.objects.create(name='test_label_2')
        Task.objects.create(name='test_name',
                            description='test',
                            status=status,
                            executor=executor,
                            autor=autor)

    def test_task(self):
        task = Task.objects.get(name='test_name')
        self.assertEquals(task.description, 'test')
        self.assertEquals(task.status.name, 'test_status')
        self.assertEquals(task.executor.username, 'executor')
        self.assertEquals(task.autor.username, 'autor')
