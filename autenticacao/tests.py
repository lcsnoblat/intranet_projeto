from django.test import TestCase
from django.test import Client

from .views import home

class TesteViews(TestCase):

	
	def setUp(self):
		self.cliente = Client()

	def teste_chama_view_home(self):
		resposta = self.cliente.get('/')
		self.assertEqual(resposta.status_code, 200)
		self.assertTemplateUsed(resposta, 'home.html')