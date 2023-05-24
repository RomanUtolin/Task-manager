from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.messages.views import SuccessMessageMixin


class IndexPage(TemplateView):
    template_name = "index.html"


class LoginPage(SuccessMessageMixin, LoginView):
    success_message = _('You are logged in')
    template_name = "form.html"
    redirect_authenticated_user = reverse_lazy('index')
    next_page = reverse_lazy('index')
    context = {'header': _('Entrance'), 'button': _('Log in')}
    extra_context = context


class Logout(LogoutView):
    def get_success_url(self):
        messages.info(self.request, _('You are logged out'))
        return reverse_lazy('index')
