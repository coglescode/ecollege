from django import forms
from ecollege.models import Course
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm



class CourseEnrollForm(forms.Form):
  course = forms.ModelChoiceField(queryset=Course.objects.all(), widget=forms.HiddenInput)


class UserRegisterForm(UserCreationForm):
    # group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    
    class Meta:
      model = User 
      fields = ['username', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
      super(UserRegisterForm, self).__init__(*args, **kwargs)

      for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-focus w-full bg-zinc-50 border border-zinc-200 rounded-2xl py-4 pl-11 pr-12 text-base focus:outline-none focus:border-indigo-500'
            