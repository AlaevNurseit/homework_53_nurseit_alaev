from django.http import  HttpResponseNotFound
from django.shortcuts import render
from articles.models import ToDolist
from django.shortcuts import redirect


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
    if request.method == 'GET':
        status_choices = ToDolist.STATUS_CHOICES
        return render(request, 'todolist_create.html', {'status_choices': status_choices})
    elif request.method == 'POST':
        ToDolist.objects.create(
            description=request.POST.get("description"),
            more_detailed_description = request.POST.get("more_detailed_description"),
            status=request.POST.get("status"),
            execution_date=request.POST.get("execution_date") or None,
        )
        return redirect("/todolist/")