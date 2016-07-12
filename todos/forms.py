from django.contrib.auth.models import User

from django import forms
from django.forms.formsets import BaseFormSet, formset_factory
from django.forms.models import inlineformset_factory

from todos.models import ToDoList, ToDoItem


class Userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password']


class TodoListForm(forms.ModelForm):
    class Meta:
        model=ToDoList
        fields=['name','created']



class TodoItemForm(forms.ModelForm):
    class Meta:
        model=ToDoItem
        fields=['desc','due_date','completed']


