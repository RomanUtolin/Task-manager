import django_filters
from task_manager.tasks.models import Task
from task_manager.labels.models import Label
from django import forms
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):
    labels = django_filters.ModelChoiceFilter(queryset=Label.objects.all(), label=_('Label'))
    autor = django_filters.BooleanFilter(field_name='autor',
                                         method='current_user',
                                         label=_('Only your tasks'),
                                         widget=forms.CheckboxInput)

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def current_user(self, queryset, *args, **kwargs):
        if self.request.GET.get('autor'):
            return queryset.filter(autor=self.request.user)
        return queryset
