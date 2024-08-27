from django.urls import path
from . import views

urlpatterns = [
    path('inicio/',views.index),
    path('inicio2/',views.index2),#Es lo que se abre despues del // en la pagina del servidor
]