from supercatch.respuesta import Respuesta

from nltk.tokenize import word_tokenize

class TokensRespuesta:
	Respuesta: Respuesta
	Tokens: list
	
	def __init__(self,resp):
		self.Respuesta = resp
		self.Tokens = []
		
		
	def getRespuesta(self):
		return self.Respuesta
		
	def getTokens(self):
		return self.Tokens
		
	def tokenizarTexto(self):
		tokens = word_tokenize(self.Respuesta.texto.replace('¿','').replace('¡',''))
		
		if len(tokens) > 0:
			self.Tokens = tokens
			
		else:
			raise Exception("No hay contenido en la respuesta proporcionada.")
