from django.contrib.messages import api
from django.shortcuts import render
from estudiantes.models import Estudiante
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from estudiantes.serializers import EstudianteSerializer
# Create your views here.


#Decorador es api view
@api_view(['GET', 'POST'])
def estudiantes(request):
    if request.method == 'GET':
        estudiantes = Estudiante.objects.all()
        #Serializo las editoriales
        serialized = EstudianteSerializer(estudiantes, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
    print("Aqui empieza el error 1"),
    if request.method == 'POST':
        estudiante = EstudianteSerializer(data=request.data)
        if estudiante.is_valid():
            estudiante.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=estudiante.errors)
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def estudiante(request, estudiante_id):

    try:
        estudiante = Estudiante.objects.get(id=estudiante_id)
    except Estudiante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialized = EstudianteSerializer(estudiante)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
        #serializo los datos
    if request.method == 'DELETE':
        estudiante.delete()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response({'No se ha podido eliminar la clase '}, status=status.HTTP_400_BAD_REQUEST)








# def get_estudiante(request, estudiante_id):
#     estudiante = Estudiante.objects.get(id=estudiante_id)
#     return render(request, 'estudiantes/estudiante_id.html', {'estudiante': estudiante})


