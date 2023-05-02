from django.contrib import admin
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.urls import reverse
from django.utils.html import format_html, urlencode

from .models import *


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'category', 'storage_type', 'location', 'last_updated']
    list_prefetch_related = ['category', 'storage_type', 'location']
    list_editable = ['quantity', 'location', 'storage_type']
    list_per_page = 10
    search_fields = ['name__istartswith']
    list_filter = ['storage_type', 'location', 'last_updated']

    # def location_name(self, object):
    #     return object.location.name if object.location else None

    # def storage_name(self, object):
    #     return object.storage_type.name if object.storage_type else None
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('category', 'storage_type', 'location')
        return queryset
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'objects_count']
    
    def objects_count(self, category):
        url = (
            reverse('admin:inventory_object_changelist')
            + '?'
            + urlencode({
                'category__id': str(category.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, category.objects_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            objects_count = Count('objects')
        )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'objects_count']
    
    def objects_count(self, storagetype):
        url = (
            reverse('admin:inventory_object_changelist')
            + '?'
            + urlencode({
                'location__id': str(storagetype.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, storagetype.objects_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            objects_count = Count('objects')
        )
   
    
@admin.register(StorageType)
class StorageTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'objects_count', 'date_organized']

    def objects_count(self, storage_type):
        url = (
            reverse('admin:inventory_object_changelist')
            + '?'
            + urlencode({
                'storage_type__id': str(storage_type.id)
            })
        )
        return format_html('<a href="{}">{}</a>', url, storage_type.objects_count)
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            objects_count = Count('objects')
        )