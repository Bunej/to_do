from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import CreateTaskForm, TaskStatusForm
from datetime import date


def index(request):
    tasks = Task.objects.order_by('-end_date')
    print(tasks)
    context = {'tasks': tasks, 'date': date.today()}
    return render(request, 'tasks/base.html', context)


def task_detail(request, id):
    task = get_object_or_404(Task, id=id)
    context = {'task': task}
    return render(request, 'tasks/detail.html', context)


@login_required
def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')
    else:
        form = CreateTaskForm()
        context = {'form': form}
        return render(request, 'tasks/task_form.html', context)


@login_required
def user_tasks(request):
    tasks = Task.objects.filter(user=request.user)
    print(tasks)
    context = {'tasks': tasks, 'date': date.today()}
    return render(request, 'tasks/user_tasks.html', context)


@login_required
def change_status(request, id=id):
    obj = get_object_or_404(Task, id=id)
    form = TaskStatusForm(request.POST, instance=obj)
    if obj.user == request.user:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('user_tasks')
        else:
            form = TaskStatusForm()
            context = {'form': form}
            return render(request, 'tasks/change_status.html', context)
    else:
        return redirect('index')


def search(request):
    query = request.GET.get('q')
    tasks = Task.objects.filter(Q(name__icontains=query) | Q(description__icontains=query)
                                | Q(user__username__icontains=query))
    context = {'tasks': tasks, 'date': date.today()}
    return render(request, 'tasks/base.html', context)
