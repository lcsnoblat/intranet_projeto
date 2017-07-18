from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	nome = models.CharField(max_length=255, null=False)
	ultimo_nome = models.CharField(max_length=255, null=False)
	usuario = models.OneToOneField(User, related_name='perfil')

	@property
	def email():
		return self.usuario.email


