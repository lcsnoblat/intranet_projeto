from django.db import models
from django.contrib.auth.decorators import login_required

# Create your models here.

class TipoContato(models.Model):
	nome = models.CharField(max_length=50)

	def __str__(self):
		return self.nome


class Contato(models.Model):

	def path_arquivo(instance, filename):
		name, ext = filename.split('.')
		file_path = 'contato/{nome}.{ext}'.format(nome=name, ext=ext)
		return file_path

	nome = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	cargo = models.CharField(max_length=50)
	telefone = models.BigIntegerField()
	departamento = models.CharField(max_length=50, null=True)
	regiao = models.CharField(max_length=50, null=True)
	tipo_contato = models.ForeignKey(TipoContato, verbose_name='Tipo de Contato')

	def __str__(self):
		return self.nome