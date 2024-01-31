from django.shortcuts import render
from Home.models import Task

def index(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        if title and desc:
            ins = Task(tasktitle=title, taskdesc=desc)
            ins.save()
            success = True
        else:
            success = False
    else:
        success = False

    all_tasks = Task.objects.all()
    context = {'success': success, 'tasks': all_tasks}
    return render(request, "index.html", context)

def user(request):
    return render(request, "user.html")

def task(request):
    return render(request, "task.html")