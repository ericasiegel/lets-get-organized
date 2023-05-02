from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
@api_view()
def object_list(request):
    queryset = Object.objects.all()
    serializer = ObjectSerlializer(queryset, many=True)
    return Response(serializer.data)

@api_view()
def object_detail(request, id):
    object = get_object_or_404(Object, pk=id)
    serializer = ObjectSerlializer(object)
    return Response(serializer.data)
