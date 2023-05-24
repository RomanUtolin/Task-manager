from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from task_manager.labels.forms import LabelCreation
from task_manager.labels.models import Label
from task_manager.mixins import LabelPassesMixin


class LabelsPage(LabelPassesMixin, ListView):
    model = Label
    template_name = "labels/index.html"
    context_object_name = 'labels'


class CreateLabelPage(LabelPassesMixin, CreateView):
    form_class = LabelCreation
    template_name = "form.html"
    success_message = _('Label created successfully')
    context = {'header': _('Create label'), 'button': _('Create')}
    extra_context = context


class UpdateLabelPage(LabelPassesMixin, UpdateView):
    model = Label
    form_class = LabelCreation
    template_name = "form.html"
    success_message = _('label changed successfully')
    context = {'header': _('Edit label'), 'button': _('Edit')}
    extra_context = context


class DeleteLabelPage(LabelPassesMixin, DeleteView):
    model = Label
    template_name = "delete_form.html"
    success_message = _('Label deleted successfully')
    permission_delete_message = _("Can't delete label because it's in use")
    context = {'header': _('Deleting a label')}
    extra_context = context
