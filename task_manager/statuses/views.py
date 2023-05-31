from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusCreation
from task_manager.mixins import StatusPassesMixin


class StatusesPage(StatusPassesMixin, ListView):
    model = Status
    template_name = "statuses/index.html"
    context_object_name = 'statuses'


class CreateStatusPage(StatusPassesMixin, CreateView):
    form_class = StatusCreation
    template_name = "form.html"
    success_message = _('Status created successfully')
    context = {'header': _('Create status'), 'button': _('Create')}
    extra_context = context


class UpdateStatusPage(StatusPassesMixin, UpdateView):
    model = Status
    form_class = StatusCreation
    template_name = "form.html"
    success_message = _('Status changed successfully')
    context = {'header': _('Change status'), 'button': _('Edit')}
    extra_context = context


class DeleteStatusPage(StatusPassesMixin, DeleteView):
    model = Status
    template_name = "delete_form.html"
    success_message = _('Status deleted successfully')
    permission_delete_message = _("Can't delete status because it's in use")
    context = {'header': _('Deleting a status')}
    extra_context = context
