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


