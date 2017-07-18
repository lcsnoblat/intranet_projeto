from django.db import models
from django.contrib.auth.models import User


class TipoManual(models.Model):

	nome = models.CharField(max_length=50)
	descricao = models.CharField(max_length=255)
	material_comercial = models.BooleanField()
	material_gente_e_gestao = models.BooleanField()

	def __str__(self):
		return self.nome


class Manual(models.Model):

	def get_upload_path(instance, filename):
		name, ext = filename.split('.')
		file_path = '{categoria}/{usuario}/{nome}.{ext}'.format(usuario = instance.usuario_criador, categoria=instance.tipo ,nome=name, ext=ext)
		return file_path

	nome = models.CharField(max_length=50)
	descricao = models.CharField(max_length=255)
	usuario_criador = models.ForeignKey(User, verbose_name='Usuário que realizou o upload')
	arquivo =  models.FileField(upload_to=get_upload_path)
	tipo = models.ForeignKey(TipoManual, verbose_name='Tipo de manual')

	def __str__(self):
		return self.nome

	def file_link(self):
		if self.arquivo.url:
			link =  "<a href='{}'>Download</a>".format(self.arquivo.url)
			return link
		else:
			return 'Sem arquivo'

	file_link.allow_tags=True
