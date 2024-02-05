from django.shortcuts import render, redirect
from django.contrib import messages


from .forms import TodoForm
from .models import Todo


# Create your views here.
def index(request):
    item_list=Todo.objects.order_by("-title")
    if request.method=="POST":
        form = TodoForm(request.POST)
        form.save()
        return redirect("todo")
    form =TodoForm()
    page ={
        "forms":form,
        "list":item_list,
    "title":"Todo List",
    }
    return render(request,'todo/index.html',page)

def remove(request, item_id):
    print(item_id)
    item = Todo.objects.get(title=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')

def add(request):
    item_list=Todo.objects.order_by("-title")


    return render(request, 'todo/list.html',{'title':"All Todo","list":item_list})
    