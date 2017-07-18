from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .import forms
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.models import User
from help.enviar_email import EnviarEmail
import string, random
from django.conf import settings


def home(request):
	context = RequestContext(request,
                           {'request': request,
                            'user': request.user,
                            'usuario': request.user})
	if request.user.is_anonymous():
		return render(request, 'login.html')
	return render_to_response('home.html',
                             context_instance=context)

def login_user(request):
	if request.method =="POST":
	    username = request.POST['username']
	    password = request.POST['password']
	    username = username.lower()
	    user = authenticate(username=username, password=password)
	    form = forms.UserForm()
	    if user is not None:
	        if user.is_active:
	            login(request, user)
	            return render(request, 'home.html' ,{'usuario':request.user})
	        else:
	        	return render(request, 'login.html', {'error':True})
	    else:
	    	return render(request, 'login.html', {'error':True})
	else:
		return render(request, 'login.html')

def logout_user(request):
	logout(request)
	return render(request, 'login.html')

def change_password(request):
	if request.method == "POST":
		email = request.POST['email']
		try:
			user = User.objects.get(email=email)
			password = string.ascii_uppercase + string.digits + string.ascii_lowercase
			password = ''.join(random.choice(password) for _ in range(8))
			user.set_password(password)
			user.save()
			EnviarEmail("Sua nova senha do Yenzah Atende", "A sua nova senha é: {}".format(password),settings.EMAIL_YENZAH,[user.email] )
			return render(request, 'esqueci_senha.html', {'enviado':True})
		except:
			return render(request, 'esqueci_senha.html', {'erro':True})
	else:
		return render(request, 'esqueci_senha.html', {'erro':False})

@login_required
def change_password_to_old(request):
	context = RequestContext(request,
                           {'request': request,
                            'user': request.user,
                            'usuario': request.user})
	if request.method == "POST":
		password_new = request.POST['password_new']
		password_new2 = request.POST['password_new_2']
		if password_new == password_new2:
			user = request.user
			user.set_password(password_new)
			user.save()
			user = authenticate(username=user.username, password=password_new)
			login(request, user)
			return render(request, 'alterar_senha.html', {'alterado':True, 'usuario':request.user, 'user' : request.user})
		else:
			return render(request, 'alterar_senha.html', {'erro':True})
	else:
		return render(request, 'alterar_senha.html', {'erro':False, 'usuario':request.user, 'user' : request.user})



@login_required
def change_email(request):
	context = RequestContext(request,
							{'request': request,
							 'user': request.user,
							 'usuario': request.user})
	if request.method == "POST":
		user = request.user
		email = request.POST['email']
		email_uso = User.objects.filter(email = email)
		if email_uso.count() < 1:
			user.email = email
			user.save()
			return render(request, 'alterar_email.html', {'alterado':True, 'usuario':request.user, 'user' : request.user })
		else:
			return render(request, 'alterar_email.html', {'erro':True})
	else:
		return render(request, 'alterar_email.html', {'erro':False, 'usuario':request.user, 'user' : request.user})
