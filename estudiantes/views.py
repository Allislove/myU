from django.contrib.messages import api
from django.shortcuts import render
from estudiantes.models import Estudiante
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from estudiantes.serializers import EstudianteSerializer
# Create your views here.


#Decorador es api view
@api_view(['GET', 'POST', 'DELETE', 'PUT'])
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
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=estudiante.errors)
        # print("Aqui empieza el error"),
        # Estudiante.objects.create(
            # # print("Aqui empieza el error"),
            # firstName = 'firstName' in request.POST,
            # lastName ='firstName' in request.POST,
            # email ='firstName' in request.POST,
            # age ='firstName' in request.POST,
            # idNumber ='firstName' in request.POST,
            # city ='firstName' in request.POST,
            # score ='firstName' in request.POST,
            # approved ='firstName' in request.POST,
            # desde aqui me acepta la solicitud pero me da puros errores false

            # firstName=request.POST['firstName'],
            # lastName=request.POST['lastName'],
            # email=request.POST['email'],
            # age=request.POST['age'],
            # idNumber=request.POST['idNumber'],
            # city=request.POST['city'],
            # score=request.POST['score'],
            # approved=request.POST['approved']

        # )

        return Response(status=status.HTTP_201_CREATED)
    if request.method == 'DELETE':
        borrar_estudiante = Estudiante.objects.get(id=id).delete()
        return Response({'message': '{} Se ha borrado el estudiante con exito!'}, status=status.HTTP_204_NO_CONTENT)



# def estudiantes(request):
#     estudiantes = Estudiante.objects.all()
#
#     return render(request, 'estudiantes/lista.html', {'estudiantes': estudiantes})


def get_estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    return render(request, 'estudiantes/estudiante_id.html', {'estudiante': estudiante})


