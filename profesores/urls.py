from django.urls import path
from profesores.views import profesores, profesorId
#Llamo la vista para poder visualizar los datos en la web

#Le paso a las urlpattterns la instancia de profesores y ahora debo de representarlo en las views globales
urlpatterns = [
    path('', profesores),
]