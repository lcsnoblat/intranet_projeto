import hashlib
class geracao_md5():
	
	def __init__(self):
		senha = "123457"
		nome = "APITESTE"
		self.senha_para_md = nome + senha

	def gerar(self):
		return hashlib.md5(self.senha_para_md).hexdigest()