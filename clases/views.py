from django.shortcuts import render
from clases.models import Clase
from estudiantes.models import Estudiante


# Create your views here.

# en la vista es donde creo la funcion de la logica para visualizar los datos
def clases(request):

    clases = Clase.objects.all()
                            #Ruta del archivo          datos a mostrar mediante js
    return render(request, 'clases/lista.html', {'clases': clases})

def get_clases(request, id):

    # studentsIn = Estudiante.objects.all().filter(id=id)
    # studentsIn = Clase.estudiante.objects.filter(id=id
    studentsIn = Estudiante.objects.filter(Clase=id)
    for estudianteEn in studentsIn:
        print(estudianteEn)
    return render(request, 'clases/studentsIn.html', {'studentsIn': studentsIn})
