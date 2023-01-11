from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ApiModel
from .serializers import ApiSerializers

# Create your views here.


@api_view(['GET', 'POST'])
def api_list(request):
    "Posting the List of Items"
    if request.method == 'GET':
        viewapi = ApiModel.objects.all()
        serializer = ApiSerializers(viewapi,many=True)
        return Response(serializer.data)


    elif request.method =='POST':
        serializer = ApiSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def api_detail(request,pk):
    try:
        showApi = ApiModel.objects.get(pk=pk)

    except ApiModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serialiser = ApiSerializers(showApi)
        return Response(serialiser.data)
    
    elif request.method == 'PUT':
        serialiser = ApiSerializers(showApi,data=request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        showApi.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
        