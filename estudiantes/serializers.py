from rest_framework import serializers
from estudiantes.models import Estudiante


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        # fields = ('firstName', 'email', 'city')
        # #fields son los datos que queremos mostrar en la peticion desde los views
        fields = '__all__'

