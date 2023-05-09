from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

# Create your views here.

class ObjectViewSet(ModelViewSet):
    queryset = Object.objects.select_related('category', 'location', 'storage_type').all()
    serializer_class = ObjectSerlializer
    
    def get_queryset(self):
        return Object.objects.filter(storage_type_id=self.kwargs['storage_type_pk'])
    
    def get_serializer_context(self):
        return {'request': self.request}
    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
    
class StorageTypeViewSet(ModelViewSet):
    queryset = StorageType.objects.all()
    serializer_class = StorageTypeSerializer
    
    def get_queryset(self):
        return StorageType.objects.filter(location_id=self.kwargs['location_pk'])
    
    def get_serializer_context(self):
        return {'location_id': self.kwargs['location_pk']}
    
