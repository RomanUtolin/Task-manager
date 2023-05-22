from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.translation import gettext as _
from django_filters.views import FilterView
from task_manager.tasks.forms import TaskCreation
from task_manager.tasks.models import Task
from task_manager.tasks.filter import TaskFilter
from task_manager.mixins import TaskPassesMixin, EditDeletePassesMixin


class TasksPage(TaskPassesMixin, FilterView):
    template_name = "tasks/index.html"
    context_object_name = 'tasks'
    filterset_class = TaskFilter


class CreateTaskPage(TaskPassesMixin, CreateView):
    form_class = TaskCreation
    template_name = "tasks/create_task.html"
    success_message = _('Task created successfully')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class UpdateTaskPage(TaskPassesMixin, UpdateView):
    model = Task
    template_name = "tasks/update_task.html"
    form_class = TaskCreation
    success_message = _('Task changed successfully')


class DeleteTaskPage(TaskPassesMixin, EditDeletePassesMixin, DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    success_message = _('Task deleted successfully')
    permission_denied_message = _('A task can only be deleted by its author.')


class OpenTaskPage(DetailView):
    model = Task
    template_name = "tasks/open_task.html"
