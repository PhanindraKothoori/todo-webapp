from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ToDoList(models.Model):
    name=models.CharField(max_length=100)
    created=models.DateTimeField()
    user=models.ForeignKey(User,default=None)
    def __unicode__(self):
        return self.name

class ToDoItem(models.Model):
    desc = models.CharField(max_length=250)
    due_date = models.DateField()
    completed = models.BooleanField()
    todolist=models.ForeignKey(ToDoList)

    def __unicode__(self):
        return self.desc
