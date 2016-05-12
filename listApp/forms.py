from django import forms
from django.forms import DateTimeInput
from .models import Todo

class TodoForm(forms.ModelForm):


    class Meta:
        model = Todo
        fields = ('text', 'deadline', 'progress',)
