from django.urls import path

from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register('objects', views.ObjectViewSet)
router.register('categories', views.CategoryViewSet)
router.register('locations', views.LocationViewSet)

urlpatterns = router.urls
