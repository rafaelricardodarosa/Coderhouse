from django.http import HttpResponse
import datetime
from django.template import Template, Context


def mi_primero_view(request):

    return HttpResponse("Hola mundo desde mi primero view, saludos de coder")


def segunda_vista(request):

    with open(r"/Users/rafaeldarosa/Documents/Github/Coderhouse/django/proyecto1/proyectodjango/proyectodjango/index.html") as f:
        plantilla = Template(f.read())

    contexto = Context()
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


def tiempo(request):

    nombre = "Rafael"
    hoy = datetime.datetime.now()
    html = f"""
<html>
    <head></head>
    <body>
        <h1>El tiempo es: <h2>{hoy}</h2></h1>
        Saludos desde django en <b>coder</b>. Soy {nombre}.
    </body>
</html>"""

    return HttpResponse(html)


def nombre(request, name):

    nombre = "Rafael"
    hoy = datetime.datetime.now()
    html = f"""
<html>
    <head></head>
    <body>
        <h1>El tiempo es: <h2>{hoy}</h2></h1>
        Saludos desde django en <b>coder</b>. Soy {nombre}.
    </body>
</html>"""

    return HttpResponse(html)


def calcular_edad(request, edad):

    anio_calcular = 2022
    edad_actual = anio_calcular - edad
    html = f"""
<html>
    <head></head>
    <body>
        <h1>Naciste en: </h1>
        El año de nacimiento fue: {edad_actual}.
    </body>
</html>"""

    return HttpResponse(html)
