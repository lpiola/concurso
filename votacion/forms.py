from django import forms
from django.forms import fields
from votacion.models import Votacion

class VotacionForm(forms.ModelForm):

    class Meta:
        model = Votacion     
        fields = '__all__'

        
