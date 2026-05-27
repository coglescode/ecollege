from django import forms
from django.contrib.contenttypes import fields
from django.forms import EmailField
from django.forms.models import inlineformset_factory
from . models import Course, Module, Subject
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User, Group


class SubjectForm(forms.ModelForm):
  # Override title to be a ModelChoiceField populated by the Subject model
  title = forms.ModelChoiceField(
    queryset=Subject.objects.all(),
    empty_label="--- Select a Subject ---",
    widget=forms.Select(attrs={'class': 'form-control'})  # You can add CSS classes here!
  )

  class Meta:
    model = Subject
    fields = ['title']

ModuleFormSet = inlineformset_factory(
  Course,
  Module,
  #fields=['title', 'description'],
  form=SubjectForm,
  extra=2,
  can_delete=True)



class LoginForm(AuthenticationForm):

    username = forms.CharField(label='Your user name:', widget=forms.TextInput(attrs={'class': 'input-focus w-full bg-zinc-50 border border-zinc-200 rounded-2xl py-4 pl-11 pr-4 text-base focus:outline-none focus:border-indigo-500',
                                                                                    'id': 'USERNAME',
                                                                                    'placeholder': 'your username',
                                                                                    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-focus w-full bg-zinc-50 border border-zinc-200 rounded-2xl py-4 pl-11 pr-12 text-base focus:outline-none focus:border-indigo-500',
                                                                 'id': 'PASSWORD',
                                                                 'type': 'password',
                                                                 'placeholder': '••••••••'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)