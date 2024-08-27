from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('pagina1/',views.pagina),#Es lo que se abre despues del // en la pagina del servidor
]