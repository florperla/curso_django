from django. http import HttpResponse

import datetime


def saludo(request): #Esto es una vista

    texto1 = """<html>
    <body>
    <h1>
    Hola mundo!
    <h1>
    <body>
    <html>"""

    return HttpResponse(texto1)


def fecha_y_hora(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h2>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)


def cuerpo(request):

    return HttpResponse("Ésta página la hice para aprender conceptos de Django")


def despedida(request):

    return HttpResponse("Gracias, chau!")


def calcula_edad(request, edad, anio):

    #edadActual=27
    periodo=anio-2022
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendrás %s años" %(anio, edadFutura)

    return HttpResponse(documento)