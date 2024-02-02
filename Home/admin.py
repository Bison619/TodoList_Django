from django.contrib import admin
from Home.models import Task , Ctask

class TaskAdmin(admin.ModelAdmin):
    list_display= ('tasktitle','time')

class CtaskAdmin(admin.ModelAdmin):
    list_display= ('Ctasktitle','Ctaskdesc')

# Register your models here.
admin.site.register(Task,TaskAdmin)
admin.site.register(Ctask,CtaskAdmin)