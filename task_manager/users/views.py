from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from task_manager.mixins import UserTestMixin
from task_manager.users.models import User
from task_manager.users.forms import UserCreation


class UsersPage(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = 'users'


class CreateUserPage(CreateView):
    template_name = "users/create_user.html"
    form_class = UserCreation

    def get_success_url(self):
        messages.success(self.request, _('User successfully registered'))
        return reverse_lazy('login_page')


class UpdateUserPage(UserTestMixin, UpdateView):
    model = User
    form_class = UserCreation
    template_name = "users/update_user.html"

    def get_success_url(self):
        messages.success(self.request, _('User changed successfully'))
        return reverse_lazy('users_page')


class DeleteUserPage(UserTestMixin, DeleteView):
    model = User
    template_name = "users/delete_user.html"

    def get_success_url(self):
        messages.success(self.request, _('User deleted successfully'))
        return reverse_lazy('index')
