from django.http import  HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from articles.models import ToDolist
from django.shortcuts import redirect
from articles.validators import validate_todolist
from articles.forms import TodolistForm
from django.urls import reverse


def todolist_list(request):
    todolists = ToDolist.objects.all()
    context = {'todolists': todolists}
    return render(request, "index.html", context)


def todolist_detail(request, pk):
    try:
        todolist = ToDolist.objects.get(id=pk)
        context = {'todolist': todolist}
        return render(request, "todolist_view.html", context)
    except ToDolist.DoesNotExist:
        return HttpResponseNotFound()


def todolist_create(request):
    form = TodolistForm()
    if request.method == 'GET':
        status_choices = ToDolist.STATUS_CHOICES
        return render(request, 'todolist_create.html', {'form': form, 'status_choices': status_choices})
    elif request.method == 'POST':
        form = TodolistForm(request.POST)
        if form.is_valid():
            todolist = ToDolist(
                description=request.POST.get("description"),
                more_detailed_description=request.POST.get("more_detailed_description"),
                status=request.POST.get("status"),
                execution_date=request.POST.get("execution_date") or None,
            )
            todolist.save()
            return redirect("todolist_list",pk=todolist.pk)
        else:
             return render(request, 'todolist_create.html', {'form': form})


def todolist_update(request, pk, *args, **kwargs):
    todolist = get_object_or_404(ToDolist, pk=pk)
    form = TodolistForm(initial={
        'description': todolist.description,
        'status': todolist.status,
        'execution_date': todolist.execution_date,
        'more_detailed_description': todolist.more_detailed_description,
    })
    context = {'form': form}

    if request.method == 'GET':
        context['action'] = reverse('todolist_update', kwargs={'pk': todolist.pk})
        return render(request, 'todolist_update.html', context)
    elif request.method == 'POST':
        form = TodolistForm(request.POST, instance=todolist)
        if form.is_valid():
            todolist.description = request.POST.get("description")
            todolist.more_detailed_description = request.POST.get("more_detailed_description")
            todolist.status = request.POST.get("status")
            todolist.execution_date = request.POST.get("execution_date") or None
            todolist.save()
            return redirect('todolist_detail', pk=todolist.pk)
        return render(request, 'todolist_update.html', {'form': form})

def todolist_delete(request, pk, *args, **kwargs):
    if request.method == 'POST':
        todolist = get_object_or_404(ToDolist, pk=pk)
        todolist.delete()
    return redirect('todolist_list')