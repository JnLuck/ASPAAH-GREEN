from django import template
from ..models import Persona
  
register = template.Library()
  
@register.filter()
def selectedOption(value_selected, value_raw):
    r = ''
    if value_selected == value_raw:
        r = 'selected'
    return r

@register.filter()
def spaceTrim(value_trim):
    return value_trim.strip()

@register.filter()
def checkedValue(value_bool):
    r = ''
    if value_bool == True:
        r = 'checked'
    return r

@register.filter()
def personMode(value_bool):
    r = 'Inactive'
    if value_bool == True:
        r = 'Active'
    return r

@register.filter()
def personList(value_list):
    value_list.pop(0)
    return value_list

@register.filter()
def nextList(value_list):
    iter_list = iter(value_list)
    next(iter_list)
    return iter_list

@register.filter()
def typeForm(value_type):
    r = 'Edit'
    if value_type == None:
        r = 'New'
    return r

@register.filter()
def socioCheck(value_id):
    r = False
    if Persona.objects.filter(r_persona__id=value_id).exists():
        r = True
    return r

