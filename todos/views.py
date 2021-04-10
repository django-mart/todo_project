from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from .models import Todo

# Create your views here.
def list_todo_items(request: HttpRequest):
    context = {'todo_list': Todo.objects.all()}
    return render(request, 'todos/todo_list.html', context=context)

def insert_todo_item(request: HttpRequest):
    content = request.POST['content']
    todo = Todo(content=content)
    todo.save()
    return redirect('/todos/list/')

def delete_todo_item(request: HttpRequest, todo_id: int):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list/')