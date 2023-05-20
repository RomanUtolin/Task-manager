from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from task_manager.tasks.forms import TaskCreation
from task_manager.tasks.models import Task


class TasksPage(LoginRequiredMixin, ListView):
    template_name = "tasks/index.html"
    model = Task
    context_object_name = 'tasks'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)


class CreateTaskPage(LoginRequiredMixin, CreateView):
    template_name = "tasks/create_task.html"
    form_class = TaskCreation

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, _('Task created successfully'))
        return reverse_lazy('tasks_page')


class UpdateTaskPage(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/update_task.html"
    form_class = TaskCreation

    def get_success_url(self):
        messages.success(self.request, _('Task changed successfully'))
        return reverse_lazy('tasks_page')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)


class DeleteTaskPage(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"

    def get_success_url(self):
        messages.success(self.request, _('Task deleted successfully'))
        return reverse_lazy('tasks_page')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
        if not self.get_object().autor == self.request.user:
            messages.error(self.request, _('A task can only be deleted by its author.'))
            return redirect('tasks_page')
        return super().dispatch(request, *args, **kwargs)


class OpenTaskPage(LoginRequiredMixin, DetailView):
    template_name = "tasks/open_task.html"
    model = Task

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)
