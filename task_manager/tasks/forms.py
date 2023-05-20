from django import forms
from task_manager.tasks.models import Task


class TaskCreation(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "description",
            "status",
            "executor",
            "labels",
        )
