from django.db import models


class Task(models.Model):
    tasktitle = models.TextField(max_length=40)
    taskdesc = models.CharField( max_length=500)
    time = models.DateTimeField( auto_now_add= True)

    def __str__(self):
        return self.tasktitle