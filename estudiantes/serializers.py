from rest_framework import serializers
from estudiantes.models import Estudiante


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        #fields son los datos que queremos mostrar en la peticion desde los views
        fields = ('id', 'firstName', 'email', 'approved', 'age')

    class AllStudentsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Estudiante
            fields = '__all__'