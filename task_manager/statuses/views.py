from django.utils.translation import gettext as _
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
    template_name = "statuses/create_status.html"
    success_message = _('Status successfully registered')


class UpdateStatusPage(StatusPassesMixin, UpdateView):
    model = Status
    form_class = StatusCreation
    template_name = "statuses/update_status.html"
    success_message = _('Status changed successfully')


class DeleteStatusPage(StatusPassesMixin, DeleteView):
    model = Status
    template_name = "statuses/delete_status.html"
    success_message = _('Status deleted successfully')
    permission_delete_message = _("Can't delete status because it's in use")
