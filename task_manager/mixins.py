from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class UserTestMixin(UserPassesTestMixin):

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def handle_no_permission(self):
        if self.raise_exception or self.request.user.is_authenticated:
            messages.error(self.request, _('No rights to change another user'))
            return redirect('users_page')
        elif not self.request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
