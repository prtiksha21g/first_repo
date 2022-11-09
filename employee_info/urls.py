from django.contrib import admin
from django.urls import path
from employee_info import views
from student_info  .views import student_fun

urlpatterns = [
    path('first/',views.first_fun),

]