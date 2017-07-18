from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Manual, TipoManual
from django.views.generic import View
from django.utils.decorators import method_decorator


@login_required
def home(request):
	usuario = request.user
	if usuario.groups.count() > 0:
		if usuario.groups.first().name == 'representante' or usuario.groups.first().name == 'inspiradora':
	 		return redirect('home')
	manuais = Manual.objects.all()
	tipos = TipoManual.objects.filter(material_comercial = False, material_gente_e_gestao = False)
	return render(request, 'manuais.html', {'usuario': usuario, 'manuais' : manuais, 'tipos' : tipos})

@login_required
def material(request):
	usuario = request.user
	manuais = Manual.objects.all()
	if request.path.split('/')[2] == 'material':
		tipos = TipoManual.objects.filter(material_comercial = True, material_gente_e_gestao = False)
	return render(request, 'manuais.html', {'usuario': usuario, 'manuais' : manuais, 'tipos' : tipos})

@login_required
def gente_e_gestao(request):
	usuario = request.user
	manuais = Manual.objects.all()
	if request.path.split('/')[2] == 'gente_e_gestao':
		tipos = TipoManual.objects.filter(material_gente_e_gestao = True, material_comercial = False)
	return render(request, 'manuais.html', {'usuario': usuario, 'manuais' : manuais, 'tipos' : tipos})

@login_required
def faq(request):
	usuario = request.user
	if usuario.groups.count() > 0:
		if usuario.groups.first().name == 'representante':
			return redirect('home')
	usuario = request.user
	return render(request, 'faq.html', {'usuario':usuario})
