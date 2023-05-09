from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class LocationNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id','name']
        
class StorageNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageType
        fields = ['id','name']
        
class ObjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ['id','name', 'description']

class StorageTypeSerializer(serializers.ModelSerializer):
    location = LocationNameSerializer(read_only=True)
    objects = ObjectNameSerializer(many=True, read_only=True)
    
    class Meta:
        model = StorageType
        fields = ['id', 'name', 'location', 'date_organized', 'objects']
        
    def create(self, validated_data):
        location_id = self.context['location_id']
        return StorageType.objects.create(location_id=location_id, **validated_data)
    

class LocationSerializer(serializers.ModelSerializer):
    storage_type = StorageNameSerializer(read_only=True, many=True)
    
    class Meta:
        model = Location
        fields = ['id', 'name', 'storage_type']
        
class ObjectSerlializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only = True)
    storage_type = StorageTypeSerializer(read_only = True)
    location = LocationSerializer(read_only = True)
    
    class Meta:
        model = Object
        fields = ['id', 'name', 'quantity', 'description', 'category', 'storage_type', 'location', 'last_updated']
    
    