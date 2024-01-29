from django.shortcuts import render
from Home.models import Task

def index(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(tasktitle=title, taskdesc=desc)
        ins.save()
    return render(request,"index.html")
