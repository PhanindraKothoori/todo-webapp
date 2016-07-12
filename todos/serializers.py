from django.contrib.gis import serializers
from rest_framework import serializers

from todos.models import *

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model=ToDoList
        fields=['id','name','created']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=ToDoItem
        fields=['id','desc','due_date','completed']

        