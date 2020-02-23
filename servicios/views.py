from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Cliente
from .serializer import ClientesSerializer
from rest_framework import viewsets


# def list_all_servicios_json(request):
#     lista_servicios=serializers.serialize('json',)


class ClienteList(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer





# Create your views here.
