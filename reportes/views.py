from pickle import FALSE
from django.http import HttpResponse

from reportes.models import reportesadmin
# Create your views here.

def index(request):
    return HttpResponse("reportes.")

def lista_reportes(request):
    reportes = reportesadmin.objects.all()
    return HttpResponse(
        "<br>".join([f"{reporte.nombre}: {reporte.descripcion}" for reporte in reportes]), safe=FALSE 
    )