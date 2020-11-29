from django.urls import path
from estudiantes.views import estudiantes, get_estudiante

urlpatterns = [
    path('', estudiantes)

]


# urlpatterns = [
#     path('', estudiantes, name='List' ),
#     path('<estudiante_id>/', get_estudiante, name='detail'),
# ]


