from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):

    title = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Next, what should I do...'}))

    class Meta:
        model = Task
        fields = '__all__'      # all field from models.Task
        exclude = ('user',)     # exclude user selection in update page