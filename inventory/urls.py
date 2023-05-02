from django.urls import path
from . import views


urlpatterns = [
    path('objects/', views.object_list)
]
