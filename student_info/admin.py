from django.contrib import admin

# Register your models here.
from student_info.models import student
class studentadmin(admin.ModelAdmin):
    list_display=['username','password']

admin.site.register(student,studentadmin)

