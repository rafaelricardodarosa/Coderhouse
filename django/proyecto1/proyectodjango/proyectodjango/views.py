from django.http import HttpResponse


def mi_primero_view(request):

    return HttpResponse("Hola mundo desde mi primero view, saludos de coder")
