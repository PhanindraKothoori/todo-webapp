from django import views
from django.contrib.auth import authenticate, login, views, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory
from django.shortcuts import render, redirect
from django.template import loader

from ToDo import settings
from todos.forms import TodoListForm,  TodoItemForm
from todos.models import *
from django.http import HttpResponse
from django.db.models import Count
# Create your views here.


def display_lists(request):
    current = request.user

    lists=ToDoList.objects.filter(user=current).order_by('created')
    # print lists

    dicts=dict((each,ToDoItem.objects.filter(todolist=each)) for each in lists)
    # print dicts

    print (current.username)

    return HttpResponse(render(request,'todolist.html',context={'user':request.user,'lists':lists,'clears':sorted(dicts.items(),key=lambda x:x[0].created,reverse=True)}))

def index(request):
    template=loader.get_template('todos/index.html')
    context={
        'welcome':'Hey there! Welcome to todos web app.'
    }
    return HttpResponse(template.render(context,request))

def createlist(request,list_pk=None):
    user=request.user
    if list_pk:
        templist=ToDoList.objects.get(id=list_pk)
    else:
        templist=ToDoList()
        tempitem=ToDoItem()
    TodoItemFormSet = inlineformset_factory(ToDoList, ToDoItem, form=TodoItemForm, fk_name='todolist')
    if request.method=='POST':
        form=TodoListForm(request.POST,instance=templist)
        formset=TodoItemFormSet(request.POST,instance=tempitem)
        form.instance.user=request.user
        form.full_clean()
        list=form.save()
        try:
            formset=ToDoItem(request.POST['id'])
        except ValidationError:
            return

        formset.full_clean()

        # if formset.data['completed']=='on':
        #     formset.data['completed']=True
        # else:
        #     formset.data['completed']=False
        formset.save()
    else:
        form=TodoListForm(instance=templist)
        formset=TodoItemForm(instance=templist)

    return HttpResponse(render(request,'todos/myform.html',context={'form':form,'formset':formset}))

def logoutuser(request):
    logout(request)
    return redirect('/login/')

