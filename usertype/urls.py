from django.urls import path
from .import views

urlpatterns=[
  path('student/register/', views.StudentRegistrationView.as_view(), name='student_registration'),
  path('teacher/register/', views.TeacherRegisterView.as_view(), name='teacher_registration'),
  
  path('enroll-course/', views.StudentEnrollCourseView.as_view(), name='user_enroll_course'),
  path('courses/', views.StudentCourseListView.as_view(), name='user_course_list'),
  path('course/<pk>/', views.StudentCourseDetailView.as_view(), name='user_course_detail'),
  path('course/<pk>/<module_id>', views.StudentCourseDetailView.as_view(), name='user_course_detail_module'),

]