from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from clases.serializers import ClaseSerializer, AllClasesSerializer
from clases.models import Clase
from estudiantes.models import Estudiante
from rest_framework.parsers import JSONParser
import json



# Create your views here.


#Decorador es api view
@api_view(['GET', 'POST'])
def clases(request):
    #Ahora hacemos un try/except o en otros lenguajes try/catch  si existen traelos de lo contrario manda un error
    #De que no existen
    try:
        clases = Clase.objects.all()
    except Clase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        #Serializo las clases
        serialized = ClaseSerializer(clases, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    if request.method == 'POST':
        clase = ClaseSerializer(data=request.data)
        if clase.is_valid():
            #Si es valido entonces creemos la clase en la base de datos
            clase.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=clase.errors)


@api_view(['GET', 'DELETE', 'PUT'])
def clase(request, class_id):

    try:
        clase = Clase.objects.get(id=class_id)
    except Clase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        try:
            clase = Clase.objects.get(id=class_id)
            #Cual es la instancia que va a editar
            serializer = ClaseSerializer(instance=clase, data=request.data)
            # context
            data = {}
            if serializer.is_valid():
                serializer.save()
                data["Actualizado!"] = "Se ha actualizado con  exito"
                return Response(data=data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Clase.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = AllClasesSerializer(clase)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    if request.method == 'DELETE':
        clase.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response({'No se ha podido eliminar la clase '}, status=status.HTTP_400_BAD_REQUEST)





