from django import forms
from .models import Task
from django.utils.translation import gettext_lazy
from django.forms import Textarea, TextInput


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        labels = {
            "title": gettext_lazy("Title:"),
            "description": gettext_lazy("Description:"),
        }
        widgets = {
            "title": TextInput(attrs={"class": "form-control"}),
            "description": Textarea(
                attrs={"class": "form-control", "rows": "4", "cols": "50"}
            ),
        }
