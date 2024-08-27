from django.shortcuts import render
from django.http import HttpResponse # Responde un html de vuelta para ser desplegado en el navegador

# Create your views here.

def index(request): #request informacion que viene desde cliente o usuario siempre vuelta
    html="""<h1>Hola soy el index de tu vista</h1>
            <h2>Hola soy el index de tu vista numero 2</h2>
            
    """
    return HttpResponse(html)

def index2(request): #request informacion que viene desde cliente o usuario siempre vuelta
    html="""<h1 style="color:blue">Probando funcion 2</h1>
            <h2>Todo salio bien</h2>
            
    """
    return HttpResponse(html)
    

