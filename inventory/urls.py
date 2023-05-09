from django.urls import path

from rest_framework_nested import routers

from . import views


router = routers.DefaultRouter()
router.register('objects', views.ObjectViewSet)
router.register('categories', views.CategoryViewSet)
router.register('locations', views.LocationViewSet)

locations_router = routers.NestedDefaultRouter(router, r'locations', lookup='location')
locations_router.register(r'storage_types', views.StorageTypeViewSet, basename='location_storage')

# storages_router = routers.NestedDefaultRouter(router, r'storage_types', lookup='storage_types')
# storages_router.register(r'objects', views.ObjectViewSet, basename='objects')

urlpatterns = router.urls + locations_router.urls #+ storages_router
