from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']
        
class StorageTypeSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only = True)
    
    class Meta:
        model = StorageType
        fields = ['id', 'name', 'location', 'date_organized']

class ObjectSerlializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    storage_type = StorageTypeSerializer(read_only = True)
    location = LocationSerializer(read_only = True)
    
    class Meta:
        model = Object
        fields = ['id', 'name', 'quantity', 'description', 'category', 'storage_type', 'location', 'last_updated']
    
    