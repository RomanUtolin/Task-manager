from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = (('date_joined', DateFieldListFilter),)
    search_fields = ['username']
