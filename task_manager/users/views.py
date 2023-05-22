from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from task_manager.mixins import EditDeletePassesMixin, UserPassesMixin
from task_manager.users.models import User
from task_manager.users.forms import UserCreation


class UsersPage(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = 'users'


class CreateUserPage(CreateView):
    template_name = "users/create_user.html"
    form_class = UserCreation
    success_message = _('User successfully registered')
    success_url = reverse_lazy('login_page')


class UpdateUserPage(UserPassesMixin, EditDeletePassesMixin, UpdateView):
    model = User
    form_class = UserCreation
    template_name = "users/update_user.html"
    success_url = reverse_lazy('users_page')
    success_message = _('User changed successfully')


class DeleteUserPage(UserPassesMixin, EditDeletePassesMixin, DeleteView):
    model = User
    template_name = "users/delete_user.html"
    success_url = reverse_lazy('index')
    success_message = _('User deleted successfully')
    permission_delete_message = _('Cannot delete user because it is in use')
