from django.urls import path
from estudiantes.views import estudiantes, estudiante

urlpatterns = [
    path('', estudiantes),
    path('<estudiante_id>/', estudiante),

] 


# urlpatterns = [
#     path('', estudiantes, name='List' ),
#     path('<estudiante_id>/', get_estudiante, name='detail'),
# ]


