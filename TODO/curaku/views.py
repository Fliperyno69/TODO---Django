from django.shortcuts import get_object_or_404
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from .forms import TaskForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in
            return redirect('home')  # Redirect to the task list or another appropriate view
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def home(request):
    # Assuming the 'home' view should also display tasks
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})


# mrdka zbytecna fr fr
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'home.html', {'tasks': tasks})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user  # Assign the logged-in user to the task
            task.save()
            return redirect('home')
        else:
            print(form.errors)  # Display form errors in the console
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})


@login_required
def task_update(request, id):
    task = get_object_or_404(Task, user=request.user, pk=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})


@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, user=request.user, pk=id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'task_confirm_delete.html', {'task': task})


@login_required
def task_complete(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)  # Make sure you're filtering by the logged-in user.
    task.completed = True
    task.save()
    return redirect('tasks')
