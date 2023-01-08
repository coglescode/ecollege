from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseEnrollForm, UserRegisterForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from ecollege.models import Course

from django.contrib.auth.models import User, Group


# Create your views here.

class StudentRegistrationView(CreateView):
  template_name = 'users/student/registration.html'
  form_class = UserRegisterForm
  success_url = reverse_lazy('user_course_list') 

  def form_valid(self, form):
    result = super().form_valid(form)
    cd = form.cleaned_data
    user = authenticate(username=cd['username'], password=cd['password1'])
    # Assing students to Students group for proper persmissions
    user.is_students = True
    user.save()
    group = Group.objects.get(name="Students")
    user.groups.add(group)
    login(self.request, user)
    return result


 
class TeacherRegisterView(CreateView):
  template_name = 'users/teacher/registration.html'
  form_class = UserRegisterForm
  success_url = reverse_lazy('manage_course_list') 

  def form_valid(self, form):
    result = super().form_valid(form)
    cd = form.cleaned_data
    user = authenticate(username=cd['username'], password=cd['password1'])
    # Assing intructors to Instructors group for proper persmissions
    user.is_students = True
    user.save()
    group = Group.objects.get(name="Instructors")
    user.groups.add(group)
    login(self.request, user)
    return result


class StudentEnrollCourseView(LoginRequiredMixin, FormView):
  course = None
  form_class = CourseEnrollForm

  def form_valid(self, form):
      self.course = form.cleaned_data['course']
      self.course.students.add(self.request.user)
      return super().form_valid(form)

  def get_success_url(self):
      return reverse_lazy('user_course_detail', args=[self.course.id])


class StudentCourseListView(LoginRequiredMixin, ListView):
  model = Course
  template_name = 'users/course/list.html'

  def get_queryset(self):
    qs = super().get_queryset()
    return qs.filter(students__in=[self.request.user])  


class StudentCourseDetailView(DetailView):
  model = Course
  template_name = 'users/course/detail.html'

  def get_queryset(self):
    qs =  super().get_queryset()
    return qs.filter(students__in=[self.request.user])

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    course = self.get_object()
    if 'module_id' in self.kwargs:
      context['module'] = course.modules.get(id=self.kwargs['module_id'])
    else: 
      context['module'] = course.modules.all()[0]
    return context 