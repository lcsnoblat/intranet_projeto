from django import forms

from .models import Chamado, Interacao
from django.contrib.auth.models import User

class ChamadoForm(forms.Form):


    tipo = forms.IntegerField(required=True)
    descricao = forms.CharField(required=True)

class InteracaoForm(forms.Form):

    # tipo = forms.IntegerField(required=True)
    descricao = forms.CharField(required=True)

    def is_valid(self):
        valid = True
        if not super(InteracaoForm, self).is_valid():
            valid = False
        return valid
