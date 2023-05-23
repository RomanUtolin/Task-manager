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
    template_name = 'form.html'
    success_message = _('Task created successfully')
    context = {'header': _('Create task'), 'button': _('Create')}
    extra_context = context

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class UpdateTaskPage(TaskPassesMixin, UpdateView):
    model = Task
    template_name = 'form.html'
    form_class = TaskCreation
    success_message = _('Task changed successfully')
    context = {'header': _('Edit task'), 'button': _('Edit')}
    extra_context = context


class DeleteTaskPage(TaskPassesMixin, EditDeletePassesMixin, DeleteView):
    model = Task
    template_name = "delete_form.html"
    success_message = _('Task deleted successfully')
    permission_denied_message = _('A task can only be deleted by its author.')
    context = {'header': 'Deleting a task'}
    extra_context = context


class OpenTaskPage(DetailView):
    model = Task
    template_name = "tasks/open_task.html"
