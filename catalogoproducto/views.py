

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("catalogo de productos.")   


def lista_productos(request):
    productos = producto.objects.all()
    return HttpResponse(
        "<br>".join([f"{producto.nombre} - {producto.categoria.nombre} - {producto.precio} - {producto.stock}" for producto in productos])
    )   