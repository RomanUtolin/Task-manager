from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from task_manager.mixins import EditDeletePassesMixin, UserPassesMixin
from task_manager.users.models import User
from task_manager.users.forms import UserCreation


class UsersPage(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = 'users'


class CreateUserPage(SuccessMessageMixin, CreateView):
    template_name = "form.html"
    form_class = UserCreation
    success_message = _('User successfully registered')
    success_url = reverse_lazy('login_page')
    context = {'header': _('Registration'), 'button': _('Register')}
    extra_context = context


class UpdateUserPage(UserPassesMixin, EditDeletePassesMixin, UpdateView):
    model = User
    form_class = UserCreation
    template_name = "form.html"
    success_url = reverse_lazy('users_page')
    success_message = _('User changed successfully')
    context = {'header': _('Change User'), 'button': _('Edit')}
    extra_context = context


class DeleteUserPage(UserPassesMixin, EditDeletePassesMixin, DeleteView):
    model = User
    template_name = "delete_form.html"
    success_url = reverse_lazy('users_page')
    success_message = _('User deleted successfully')
    permission_delete_message = _('Cannot delete user because it is in use')
    context = {'header': _('Deleting a user')}
    extra_context = context
