from django.shortcuts import render, redirect, get_object_or_404
from Home.models import Task
from Home.models import Ctask


def index(request):
    all_tasks = Ctask.objects.all()
    print(all_tasks)
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
    done_tasks = Ctask.objects.all()
    context = {'success': success, 'tasks': all_tasks,'Ctasks' : done_tasks }
    return render(request, "index.html", context)

def task(request):
    done_tasks = Ctask.objects.all()
    context = {'Ctasks' : done_tasks }
    return render(request, "task.html" , context)

def Completedtask(request,task_id):
    task = get_object_or_404(Task, pk=task_id)
    C_task = Ctask(Ctasktitle=task.tasktitle, Ctaskdesc=task.taskdesc)
    C_task.save()
    task.delete()
    return redirect('home')

def del_task(request,task_id):
    task_id = int(task_id)
    try:
        task_sel= Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('home')
    task_sel.delete()
    return redirect('home')

def del_ctask(request,task_id):
    task = get_object_or_404(Ctask, id=task_id)
    task.delete()
    return redirect('task')

def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':

        task.tasktitle = request.POST['title']
        task.taskdesc = request.POST['desc']
        task.save()
        return redirect('home')
    return redirect('home')




