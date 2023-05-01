from django.contrib import admin
from .models import *




@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity', 'category', 'storage_type', 'location', 'last_updated']
    ordering = ['id', 'name', 'category', 'location', 'storage_type', 'last_updated']
    list_editable = ['quantity', 'location', 'storage_type']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id', 'name']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id', 'name']
    
@admin.register(StorageType)
class StorageTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'date_organized']
    ordering = ['id', 'name', 'location', 'date_organized']
