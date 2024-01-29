from django.contrib import admin
from Home.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display= ('tasktitle','time')

# Register your models here.
admin.site.register(Task,TaskAdmin)