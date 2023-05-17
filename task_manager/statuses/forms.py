from django import forms
from task_manager.statuses.models import Status


class StatusCreation(forms.ModelForm):
    class Meta:
        model = Status
        fields = (
            "name",
        )
