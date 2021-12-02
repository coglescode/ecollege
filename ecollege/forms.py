from django import forms
from django.contrib.contenttypes import fields
from django.forms.models import inlineformset_factory
from . models import Course, Module

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


ModuleFormSet = inlineformset_factory(Course, 
 Module, fields=['title', 'description'], extra=2, can_delete=True)


class UserRegisterForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    
    class Meta: 
      model = User
      fields = ['username', 'password1', 'password2', 'group']