from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from task_manager.labels.forms import LabelCreation
from task_manager.labels.models import Label


class LabelsPage(LoginRequiredMixin, ListView):
    template_name = "labels/index.html"
    model = Label
    context_object_name = 'labels'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)


class CreateLabelPage(LoginRequiredMixin, CreateView):
    template_name = "labels/create_label.html"
    form_class = LabelCreation

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, _('Label created successfully'))
        return reverse_lazy('labels_page')


class UpdateLabelPage(LoginRequiredMixin, UpdateView):
    model = Label
    template_name = "labels/update_label.html"
    form_class = LabelCreation

    def get_success_url(self):
        messages.success(self.request, _('label changed successfully'))
        return reverse_lazy('labels_page')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)


class DeleteLabelPage(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = "labels/delete_label.html"

    def get_success_url(self):
        messages.success(self.request, _('Label deleted successfully'))
        return reverse_lazy('labels_page')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(self.request, _('You are not authorized! Please sign in.'))
            return redirect('login_page')
        return super().dispatch(request, *args, **kwargs)
