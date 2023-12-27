# apps / cargajson / forms.py 
from import_export import resources
from django import forms
from django.urls import path
from apps.cargajson.models import CargajsonImg

class CargajsonImgResource(resources.ModelResource):
    class Meta:
        model = CargajsonImg
        exclude = []
