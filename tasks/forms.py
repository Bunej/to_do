from django import forms
from .models import Task
from django.forms.widgets import SelectDateWidget


class CreateTaskForm(forms.ModelForm):
    end_date = forms.DateField(widget=SelectDateWidget())

    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'end_date',
            'status',
        )


class TaskStatusForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'status',
        )
