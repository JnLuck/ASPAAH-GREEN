from django.contrib import admin
from .models import EstadoCivil, Persona, TipoRequisito, Solicitud, Requisito


# Register your models here.

admin.site.register(EstadoCivil)
admin.site.register(Persona)
admin.site.register(TipoRequisito)
admin.site.register(Solicitud)
admin.site.register(Requisito)

# admin.site.register(Socio)
# admin.site.register(Parentesco)
# admin.site.register(Familiar)
