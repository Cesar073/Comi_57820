from datetime import datetime as dt

# Agregamos al encabezado del archivo el import de Template y de Context
from django.template import Template, Context
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola mundo!, hola Coder! buenas noches comi 57820")

def alejandro(request):
    texto = "Soy Alejandro Ramírez<br>Cursando Python"
    return HttpResponse(texto)

def dia_de_hoy(request, dia_personalizado):
    dia = dt.now()
    dia = dia.strftime("%Y-%m-%d")
    dia = dia[:-2] + dia_personalizado
    texto = f"Hoy es:<br>{dia}"
    return HttpResponse(texto)


def probando_template(request):

    # Abrimos el archivo html
    mi_html = open('./Clases_Coder/plantillas/index.html')

    # Creamos el template haciendo uso de la clase Template
    plantilla = Template(mi_html.read())

    # Cerramos el archivo previamente abierto, ya que lo tenemos cargado en la variable plantilla
    mi_html.close()

    # Creamos un contexto, más adelante vamos a aprender a usarlo, ahora lo necesitamos aunque sea vacío para que funcione
    mi_contexto = Context()

    # Terminamos de construír el template renderizándolo con su contexto
    documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)