from django.http import HttpResponse

from inventario.models import producto
# Create your views here.

def index(request):
    return HttpResponse("inventario.")

def productos_list(request):
    productos = producto.objects.all()
    return HttpResponse(
        "<br>".join([f"{producto.nombre} - {producto.categoria.nombre} - {producto.precio} - {producto.stock}" for producto in productos])
    )