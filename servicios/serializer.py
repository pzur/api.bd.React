from rest_framework import serializers, viewsets
from .models import Cliente


class ClientesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nombre','apellido','direccion','telefono')
