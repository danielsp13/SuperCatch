from supercatch.respuesta import Respuesta

from string import punctuation
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
		unhandled_symbols = ['.','¡','¿']
		tokensFormateados = self.Respuesta.texto.replace('·','')
		for symbol in unhandled_symbols:
			tokensFormateados = tokensFormateados.replace(symbol,'')
		
		tokens = word_tokenize(tokensFormateados)
		
		if len(tokens) > 0:
			self.Tokens = tokens
			
		else:
			raise Exception("No hay contenido en la respuesta proporcionada.")
			
	
	def eliminarSimbolos(self):
		tokens = [tk for tk in self.Tokens if tk not in punctuation]
		
		if len(tokens) > 0:
			self.Tokens = tokens
			
		else:
			raise Exception("El texto no contiene palabras.")

	
