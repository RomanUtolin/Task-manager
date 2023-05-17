from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext as _


class IndexPage(TemplateView):
    template_name = "index.html"


class LoginPage(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = "index.html"

    def get_success_url(self):
        messages.success(self.request, _('You are logged in'))
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    messages.info(request, _('You are logged out'))
    return redirect('index')
