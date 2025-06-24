from django.contrib import admin
from core.models import Pais, PoliticaClimatica, AcuerdoInternacional
from core.models import PaisAcuerdo, SectorEconomico, Emision, AlertaEmision

# Register your models here.
admin.site.register(Pais)
admin.site.register(PoliticaClimatica)
admin.site.register(AcuerdoInternacional)
admin.site.register(PaisAcuerdo)
admin.site.register(SectorEconomico)
admin.site.register(Emision)
admin.site.register(AlertaEmision)


