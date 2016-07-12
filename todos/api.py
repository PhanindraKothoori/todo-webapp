from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from todos.models import *
from todos.serializers import ListSerializer,ItemSerializer


@api_view(['GET', 'POST'])
def ToDoListAll(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = ToDoList.objects.all()
        serializer = ListSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ToDoListOne(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = ToDoList.objects.get(pk=pk)
    except ToDoList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ListSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def ToDoItemsAll(request,pk):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = ToDoItem.objects.filter(todolist=pk)
        serializer = ItemSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ToDoItemOne(request, pklist, pkitem):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        snippet = ToDoItem.objects.get(pk=pkitem,todolist=pklist)
    except ToDoItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


