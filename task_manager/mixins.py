from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class PassesMixin(SuccessMessageMixin, LoginRequiredMixin):
    redirect_url = None
    login_url = reverse_lazy('login_page')
    success_message = None
    permission_denied_message = None
    permission_delete_message = None
    permission_is_not_authenticated_message = _('You are not authorized! Please sign in.')

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            messages.error(self.request, self.permission_denied_message)
            return redirect(self.redirect_url)
        elif not self.request.user.is_authenticated:
            messages.error(self.request, self.permission_is_not_authenticated_message)
            return redirect(self.login_url)

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, self.permission_delete_message)
            return redirect(self.redirect_url)


class EditDeletePassesMixin(PassesMixin):

    def dispatch(self, request, *args, **kwargs):
        try:
            user = self.get_object().autor.username
        except AttributeError:
            user = self.get_object().username
        if not self.request.user.username == user:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class TaskPassesMixin(PassesMixin):
    success_url = reverse_lazy('tasks_page')
    redirect_url = reverse_lazy('tasks_page')


class StatusPassesMixin(PassesMixin):
    success_url = reverse_lazy('statuses_page')
    redirect_url = reverse_lazy('statuses_page')


class LabelPassesMixin(PassesMixin):
    success_url = reverse_lazy('labels_page')
    redirect_url = reverse_lazy('labels_page')


class UserPassesMixin(PassesMixin):
    redirect_url = reverse_lazy('users_page')
    permission_denied_message = _('No rights to change another user')
