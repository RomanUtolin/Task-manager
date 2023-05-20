from django.contrib.admin import DateFieldListFilter, ModelAdmin, register
from task_manager.labels.models import Label


@register(Label)
class UserAdmin(ModelAdmin):
    list_filter = (('created_at', DateFieldListFilter),)
    search_fields = ['name']
