from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import TaskSerializer 
from .models import Task

# Create your views here.
@api_view(['GET'])
def apiOverView(request):
    api_urls = {
        'list': 'here we are'
    }

    return Response(api_urls) 


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_details(request, pk):
    task = Task.objects.get(pk=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def task_update(request, pk):
    task = Task.objects.get(pk=pk)

    serializer = TaskSerializer(instance=task, data=request.data) 
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data) 

@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return Response('Task deleted successfully')