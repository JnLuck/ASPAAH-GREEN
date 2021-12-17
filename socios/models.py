from django.db import models
from django.contrib.auth.models import User

class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    SEXO = [
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
    ]

    nombre = models.CharField(max_length=50)
    ape_paterno = models.CharField(max_length=50)
    ape_materno = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    fe_nacimiento = models.DateField()
    id_es_civil = models.ForeignKey('EstadoCivil', on_delete=models.CASCADE, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO, default='M')
    telefono = models.CharField(max_length=9, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    es_persona = models.BooleanField(default=False)

    class Meta:
        verbose_name = ("Persona")
        verbose_name_plural = ("Personas")

    def __str__(self):
        return self.nombre + ' ' + self.ape_paterno + ' ' + self.ape_materno

class TipoRequisito(models.Model):
    nombre = models.CharField(max_length=255)
    es_ti_requisito = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    ESTADO_SOLICITUD = [
        ('R', 'Rechazado'),
        ('A', 'Aceptado'),
        ('E', 'En Espera'),
    ]
    solicitado_por = models.ForeignKey(
        'Persona', on_delete=models.CASCADE,
        related_name="r_solicitado_pors",
        related_query_name="r_solicitado_por",
        )
    recibido_por = models.ForeignKey(User, on_delete=models.CASCADE)
    fe_recibido = models.DateField(auto_now_add=True, blank=True)
    es_solicitud = models.CharField(max_length=1, choices=ESTADO_SOLICITUD, default='E')
    fe_respuesta = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.solicitado_por.nombre + ' | ' + str(self.fe_recibido)

class Requisito(models.Model):
    id_solicitud = models.ForeignKey(
        'Solicitud',on_delete=models.CASCADE,
        related_name="r_id_solicituds",
        related_query_name="r_id_solicitud",
    )
    ti_requisito_id = models.ForeignKey('TipoRequisito', on_delete=models.CASCADE,)
    es_requisito = models.BooleanField(default=False)

    def __str__(self):
        return self.id_solicitud.solicitado_por.nombre + ' | ' + self.ti_requisito_id.nombre

# class Socio(models.Model):

#     TIPO_SOCIO = [
#         ('AGP', 'Agropecuario'),
#         ('AGA', 'Agroalimentario'),
#         ('HDR', 'Hidrobiologico'),
#     ]

#     CATEGORIA_SOCIO = [
#         ('PL', 'Profesional'),
#         ('PR', 'Productor'),
#         ('JR', 'Junior'),
#     ]
    
#     persona_id = models.ForeignKey(
#         'Persona', on_delete=models.CASCADE, 
#         related_name="r_personas",
#         related_query_name="r_persona",
#     )
#     codigo = models.CharField(max_length=10)
#     tipo = models.CharField(max_length=3, choices=TIPO_SOCIO, default='AGP')
#     categoria = models.CharField(max_length=2, choices=CATEGORIA_SOCIO, default='JR')
#     es_socio = models.BooleanField(default=False)
    

#     class Meta:
#         verbose_name = ("Socio")
#         verbose_name_plural = ("Socios")

#     def __str__(self):
#         return self.persona_id.nombre

# class Parentesco(models.Model):

#     nombre = models.CharField(max_length=50)
#     es_parentesco = models.BooleanField(default=False)

#     class Meta:
#         verbose_name = ("Parentesco")
#         verbose_name_plural = ("Parentescos")

#     def __str__(self):
#         return self.nombre

# class Familiar(models.Model):

#     familiar_id = models.ForeignKey(
#         'Persona', on_delete=models.CASCADE,
#         related_name="r_familias",
#         related_query_name="r_familia",
#     )
#     persona_id = models.ForeignKey(
#         'Persona', on_delete=models.CASCADE,
#         related_name="r_socios",
#         related_query_name="r_socio",
#     )
#     parentesco_id = models.ForeignKey(
#         'Parentesco', on_delete=models.CASCADE,
#         related_name="r_parentescos",
#         related_query_name="r_parentesco",
#     )
#     es_familiar = models.BooleanField(default=False)

#     class Meta:
#         verbose_name = ("Familiar")
#         verbose_name_plural = ("Familiars")

#     def __str__(self):
#         return self.familiar_id