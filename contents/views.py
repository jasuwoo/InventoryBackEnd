from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Content
from .serializers import ContentSerializer

# Create your views here.
class ContentView(APIView):
    def get(self, request, format=None):
        contents = Content.objects.all()
        serializer = ContentSerializer(contents , many=True)
        return Response({'ok': True , 'data': serializer.data}, status=200)
    
    def post(self, request, format=None):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data}, status=200)
        return Response({'ok': False , 'data': serializer.errors})
    
    def patch(self, request, format=None):
    
        content_instance = Content.objects.get(id=request.data['id'])
        serializer = ContentSerializer(content_instance, data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True , 'data': serializer.data, 'msg': 'Update Success!'})
        return Response({'ok': False , 'errors': serializer.errors})
    
    def delete(self, request, format=None):
        content_instance = Content.objects.get(id=request.data['id'])

        content_instance.delete()
        return Response("Deleted")
    