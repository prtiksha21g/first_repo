#from django.contrib import admin
from django.urls import path
from student_info import views
#from student_info  .views import student_fun

urlpatterns = [
    path('student1/',views.student_fun)
]
