from django.shortcuts import render

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import EstadoCivil, Persona, Solicitud, TipoRequisito, Requisito, Socio

# from .forms import PersonaForm

class PersonaList(ListView): 
    model = Persona
    template_name = 'persona_list.html'
    context_object_name = 'persona_list'
    paginate_by = 3
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            return Persona.objects.filter().order_by('id')
        else:
            if len(query) > 3:
                return Persona.objects.filter( Q(dni__startswith=query) | Q(nombre__startswith=query)).order_by('id')
            else:
                return Persona.objects.filter().order_by('id')

class PersonaDetail(DetailView):
    model = Persona
    template_name = 'persona_detail.html'
    context_object_name = 'persona' 

class PersonaCreate(CreateView):
    model = Persona
    template_name = 'persona_form.html'
    fields = [
        'nombre', 'ape_paterno', 'ape_materno', 'dni',
        'fe_nacimiento', 'id_es_civil', 'sexo', 'telefono',
        'email', 'direccion', 'es_persona',
    ]
    # success_url = reverse_lazy('socios:personalist')
    def get_success_url(self):
        solicitud = Solicitud.objects.create(
            solicitado_por = Persona.objects.get(pk=self.object.pk),
            recibido_por = self.request.user
        )

        tipo_requisitos = TipoRequisito.objects.filter(es_ti_requisito=True)
        for r in tipo_requisitos:
            Requisito.objects.create(id_solicitud=solicitud, ti_requisito_id=r)
        
        return reverse_lazy('socios:personadetail', kwargs={ "pk": self.object.pk })
    
class PersonaUpdate(UpdateView):
    model = Persona
    template_name = 'persona_form.html'
    fields = [
        'nombre', 'ape_paterno', 'ape_materno', 'dni',
        'fe_nacimiento', 'es_civil', 'sexo', 'telefono',
        'email', 'direccion', 'es_persona', 'fa_parentesco',
        # 'parentesco',
    ]
    context_object_name = 'persona'
    # success_url = reverse_lazy('socios:personadetail')

    def get_success_url(self):
           pk = self.kwargs["pk"]
           print(pk)
           return reverse_lazy('socios:personadetail', kwargs={"pk": pk})

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'persona_delete.html'
    context_object_name = 'persona'
    success_url = reverse_lazy('socios:personalist')

class RequisitoUpdate(UpdateView):
    model = Requisito
    template_name = 'requisito_form.html'
    fields = [
        'id_solicitud', 'ti_requisito_id', 'es_requisito',
    ]
    context_object_name = 'requisito'

class SolicitudUpdate(UpdateView):
    model = Solicitud
    template_name = 'solicitud_form.html'
    fields = [
        'solicitado_por', 'recibido_por', 'es_solicitud',
    ]
    context_object_name = 'solicitud'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['second_model'] = Requisito.objects.filter(id_solicitud=self.kwargs['pk'])
        print(Requisito.objects.filter(id_solicitud=self.kwargs['pk']))
        return context

# Socio

class SocioList(ListView):
    model = Socio
    template_name = 'socio_list.html'
    context_object_name = 'socio_list'
    paginate_by = 3

class SocioCreate(CreateView):
    model = Socio
    template_name = 'socio_form.html'
    fields = [
        'persona_id', 'codigo', 'tipo', 
        'categoria', 'es_socio'
    ]
    # success_url = reverse_lazy('socios:sociolist')
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['persona'] = Persona.objects.get(pk=self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        from datetime import date
        d = date.today()
        solicitud = Solicitud.objects.get(solicitado_por=self.kwargs['pk'])
        solicitud.es_solicitud = 'A'
        solicitud.fe_respuesta = d
        solicitud.save()
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('socios:sociodetail',args=(self.object.id,))

class SocioDetail(DetailView):
    model = Socio
    template_name = 'socio_detail.html'
    context_object_name = 'socio'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        socio = Socio.objects.get(pk=self.kwargs['pk'])
        context['solicitud'] = Solicitud.objects.get(solicitado_por=socio.persona_id)
        context['conyugue'] = Persona.objects.get(pk=22)
        return context