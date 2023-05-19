from django.contrib.admin import DateFieldListFilter, ModelAdmin, register
from task_manager.tasks.models import Task


@register(Task)
class UserAdmin(ModelAdmin):
    list_filter = (('created_at', DateFieldListFilter),)
    search_fields = ['name']