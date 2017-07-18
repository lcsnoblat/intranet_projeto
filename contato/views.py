from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contato, TipoContato

@login_required
def contato(request):
	usuario = request.user
	tipos = TipoContato.objects.order_by('nome')
	contatos = Contato.objects.order_by('nome')
	return render(request, 'contato.html', {'usuario': usuario, 'contatos' : contatos, 'tipos':tipos})

