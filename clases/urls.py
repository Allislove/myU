from django.urls import path
from clases.views import clases, clase

urlpatterns = [
    path('', clases),
    #Aqui le pasamos el parametro que estamos obteniendo en la vista
    path('<class_id>/', clase),



]







# from django.urls import path
#
# from clases.views import clases, get_clases
#
# app_name = "clases"
# urlpatterns = [
#     path('', clases, name='lista'),
#     path('<int:id>/', get_clases, name='detail')
# ]

