from rest_framework import serializers
from clases.models import Clase

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        #Represento el modelo con el que vamos a trabajar
        model = Clase
        fields = ('asignature', 'period', 'date', 'profesor')
        #Definimos los campos que queremos mostrar en el api
        #Debo de asignar una coma al final si solo deseamos representar un dato, de lo contrario nos va a dar error
        # en la solicitud


class AllClasesSerializer(serializers.ModelSerializer):
    #Esta clase esta representando todos los campos visibles del modelo Clase
    class Meta:
        model = Clase
        fields = '__all__'