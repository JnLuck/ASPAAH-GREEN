from django.contrib import admin
from .models import EstadoCivil, Persona, TipoRequisito, Solicitud, Requisito
from .models import TipoSocio, CategoriaSocio, Socio


# Register your models here.

admin.site.register(EstadoCivil)
admin.site.register(Persona)
admin.site.register(TipoRequisito)
admin.site.register(Solicitud)
admin.site.register(Requisito)

admin.site.register(Socio)
admin.site.register(CategoriaSocio)
admin.site.register(TipoSocio)
# admin.site.register(Parentesco)
# admin.site.register(Familiar)
