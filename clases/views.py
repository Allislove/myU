from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from clases.serializers import ClaseSerializer, AllClases
from clases.models import Clase
from estudiantes.models import Estudiante


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
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=clase.errors)
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



@api_view(['PUT'])
def clases(request, id):
    try:
        clase = Clase.objects.create(id=id)
    except Clase.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        print("Aqui surge un error al intentar obtener la data")
        serializer = AllClases(clase, many=True, data=request.data)
        #Sera un diccionario
        data = {}
        print("Aqui surge un error 2 al intentar obtener la data")
        if serializer.is_valid():
            serializer.save()
            data["succes"] = "Se ha actualizado con exito"
            #Retornamos la respuesta de la data
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @api_view(['DELETE'])
# def clases(request, classId):
#     try:
#         clase = Clase.objects.get(id=classId)
#     except Clase.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'DELETE':
#         clase.delete()
#     return Response({'Se ha borrado la clase con exito'}, {'clase': clase}, status=status.HTTP_200_OK)




# en la vista es donde creo la funcion de la logica para visualizar los datos
# def clases(request):
#
#     clases = Clase.objects.all()
#                             #Ruta del archivo          datos a mostrar mediante js
#     return render(request, 'clases/lista.html', {'clases': clases})

def get_clases(request, id):

    # studentsIn = Estudiante.objects.all().filter(id=id)
    # studentsIn = Clase.estudiante.objects.filter(id=id
    #Busco en el modelo clase el id
    studentsIn = Estudiante.objects.filter(Clase=id)
    for estudianteEn in studentsIn:
        print(estudianteEn)
    return render(request, 'clases/studentsIn.html', {'studentsIn': studentsIn})
