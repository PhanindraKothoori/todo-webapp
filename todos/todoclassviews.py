from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse_lazy, reverse
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from ToDo import settings
from todos.models import ToDoList, ToDoItem
from .forms import Userform



@method_decorator(login_required,'dispatch')
class CreateToDoListView(CreateView):
    model = ToDoList
    fields = ['name','created']
    success_url = '/todo/createitem/'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(CreateToDoListView, self).form_valid(form)

    def get_success_url(self):
        successurl=self.success_url+str(self.object.id)+'/'
        return successurl


@method_decorator(login_required,'dispatch')
class UpdateToDoListView(UpdateView):
    model = ToDoList
    fields = ['name', 'created']
    success_url = reverse_lazy('todolist')

    def get_queryset(self):
        user=self.request.user
        return ToDoList.objects.filter(user=user)

    def get_object(self, queryset=None):
        obj = ToDoList.objects.get(id=self.kwargs.get('pk'))
        if obj.user != self.request.user:
            raise Http404  # maybe you'll need to write a middleware to catch 403's same way
        return obj


@method_decorator(login_required,'dispatch')
class DeleteToDoListView(DeleteView):
    model = ToDoList
    success_url = reverse_lazy('todolist')

    def get_object(self, queryset=None):
        obj=ToDoList.objects.get(id=self.kwargs.get('pk'))
        if obj.user!=self.request.user:
            raise Http404
        return obj


@method_decorator(login_required,'dispatch')
class CreateToDoItemView(CreateView):
    model = ToDoItem
    fields = ['desc','due_date','completed','todolist']
    todolist=None
    def get_success_url(self):
        return reverse_lazy('todolist')

    def get_context_data(self, **kwargs):
        self.todolist=self.kwargs['pk']
        return super(CreateToDoItemView, self).get_context_data(**kwargs)

    def get_form(self, form_class=None):
        form = super(CreateToDoItemView, self).get_form(form_class)
        form.fields['todolist'].queryset=ToDoList.objects.filter(user_id=self.request.user.id,id=self.todolist)
        return form



    def form_valid(self, form):

        return super(CreateToDoItemView, self).form_valid(form)


@method_decorator(login_required,'dispatch')
class DeleteToDoItemView(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse_lazy('todolist')

@method_decorator(login_required,'dispatch')
class UpdateToDoItemView(UpdateView):
    model = ToDoItem
    fields = ['desc', 'due_date', 'completed', 'todolist']

    def get_success_url(self):
        return reverse_lazy('todolist')




class UserformView(View):
    form_class=Userform
    template_name='registration/signup.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,template_name=self.template_name,context={'form':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)

            #clean the data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            firstname=form.cleaned_data['first_name']
            lastname=form.cleaned_data['last_name']
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('/todo/todolists')

        return render(request,self.template_name,{'form':form})


