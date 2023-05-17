from django.contrib.admin import DateFieldListFilter, ModelAdmin, register
from task_manager.statuses.models import Status


@register(Status)
class UserAdmin(ModelAdmin):
    list_filter = (('created_at', DateFieldListFilter),)
    search_fields = ['name']
