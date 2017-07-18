import hashlib
class geracao_md5():

	def gerar(self):
		has = hashlib.md5()
		has.update(b"APITESTE123457")
		return has.hexdigest()