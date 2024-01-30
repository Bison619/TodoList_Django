from django.shortcuts import render
from Home.models import Task

def index(request):
    alltask = Task.objects.all()
    context = {'success': False , 'tasks' : alltask  }
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(tasktitle=title, taskdesc=desc)
        ins.save()
        context = {'success': True }
    return render(request,"index.html" , context)
