from django.db import models
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Name'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               verbose_name=_('Status'),
                               related_name='status')
    executor = models.ForeignKey(User, blank=True, on_delete=models.PROTECT,
                                 verbose_name=_('Executor'),
                                 related_name='executor')
    autor = models.ForeignKey(User, on_delete=models.PROTECT,
                              verbose_name=_('Autor'),
                              related_name='autor')
    labels = models.ManyToManyField(Label, blank=True, through="TaskLabels",
                                    verbose_name=_('Labels'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class TaskLabels(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    labels = models.ForeignKey(Label, on_delete=models.PROTECT)
