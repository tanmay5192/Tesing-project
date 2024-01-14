from django.contrib import admin
from project.models import student
# Register your models here.
class studentadmin(admin.ModelAdmin):
    list_display=['name','service','email','phone','message']


admin.site.register(student,studentadmin)    