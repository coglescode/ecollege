from django import forms
from django.contrib.contenttypes import fields
from django.forms.models import inlineformset_factory
from . models import Course, Module
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User, Group




ModuleFormSet = inlineformset_factory(Course, 
  Module, fields=['title', 'description'], extra=2, can_delete=True)



class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
    username = UsernameField(widget=forms.TextInput(attrs={'class': 'form-control shadow-sm '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control shadow-sm'}))