from django.shortcuts import render, redirect
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

    context = {'success': success, 'tasks': all_tasks }
    return render(request, "index.html", context)

# def Completedtask(request,task_id):
#     task = Task.objects.get(pk=task_id)
#     C_task = Ctask(Ctasktitle= task.tasktitle , Ctaskdesc = task.taskdesc)
#     C_task.save()
#     task.delete()
#     C_task = Ctask.objects.all()
#     context = {'done' : C_task }
#     return render(request, 'index.html', context)

def del_task(request,task_id):
    task_id = int(task_id)
    try:
        task_sel= Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return redirect('home')
    task_sel.delete()
    return redirect('home')



def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == 'POST':

        task.tasktitle = request.POST['title']
        task.taskdesc = request.POST['desc']
        task.save()
        return redirect('home')
    return redirect('home')


def user(request):
    return render(request, "user.html")

def task(request):
    return render(request, "task.html")