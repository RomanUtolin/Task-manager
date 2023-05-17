from django.contrib.admin import DateFieldListFilter, ModelAdmin, register
from task_manager.users.models import User


@register(User)
class UserAdmin(ModelAdmin):
    list_filter = (('date_joined', DateFieldListFilter),)
    search_fields = ['username']
