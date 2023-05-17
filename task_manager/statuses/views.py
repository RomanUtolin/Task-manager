from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusCreation
from django.contrib.auth.mixins import LoginRequiredMixin


class StatusesPage(LoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/index.html"
    context_object_name = 'statuses'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)


class CreateStatusPage(LoginRequiredMixin, CreateView):
    template_name = "statuses/create_status.html"
    form_class = StatusCreation

    def get_success_url(self):
        messages.success(self.request, _('Status successfully registered'))
        return reverse_lazy('statuses_page')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)


class UpdateStatusPage(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusCreation
    template_name = "statuses/update_status.html"

    def get_success_url(self):
        messages.success(self.request, _('Status changed successfully'))
        return reverse_lazy('statuses_page')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)


class DeleteStatusPage(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = "statuses/delete_status.html"

    def get_success_url(self):
        messages.success(self.request, _('Status deleted successfully'))
        return reverse_lazy('statuses_page')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)
