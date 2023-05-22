from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.translation import gettext as _
from task_manager.labels.forms import LabelCreation
from task_manager.labels.models import Label
from task_manager.mixins import LabelPassesMixin


class LabelsPage(LabelPassesMixin, ListView):
    model = Label
    template_name = "labels/index.html"
    context_object_name = 'labels'


class CreateLabelPage(LabelPassesMixin, CreateView):
    form_class = LabelCreation
    template_name = "labels/create_label.html"
    success_message = _('Label created successfully')


class UpdateLabelPage(LabelPassesMixin, UpdateView):
    model = Label
    form_class = LabelCreation
    template_name = "labels/update_label.html"
    success_message = _('label changed successfully')


class DeleteLabelPage(LabelPassesMixin, DeleteView):
    model = Label
    template_name = "labels/delete_label.html"
    success_message = _('Label deleted successfully')
    permission_delete_message = _("Can't delete label because it's in use")
