from django.urls import path
from .views import PersonaList, PersonaDetail, PersonaCreate, PersonaUpdate, PersonaDelete
from .views import RequisitoUpdate, SolicitudUpdate

from .views import SocioList, SocioCreate, SocioDetail

app_name = 'socios'
urlpatterns = [
    path('persona/', PersonaList.as_view(), name='personalist'),
    path('persona/detail/<str:pk>/', PersonaDetail.as_view(), name='personadetail'),
    path('persona/create/', PersonaCreate.as_view(), name='personacreate'),
    path('persona/update/<str:pk>/', PersonaUpdate.as_view(), name='personaupdate'),
    path('persona/delete/<str:pk>/', PersonaDelete.as_view(), name='personadelete'),

    path('persona/requisitos/<str:pk>/', RequisitoUpdate.as_view(), name='requisitoupdate'),
    path('persona/solicitud/<str:pk>/', SolicitudUpdate.as_view(), name='solicitudupdate'),

    # Socio
    path('socio/', SocioList.as_view(), name='sociolist'),
    path('socio/<str:pk>/aditional/', SocioCreate.as_view(), name='sociocreate'),
    path('socio/detail/<str:pk>/', SocioDetail.as_view(), name='sociodetail'),
]