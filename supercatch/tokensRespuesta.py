from supercatch.respuesta import Respuesta

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
		CHARACTER_SPLIT = ' '
		NULL_TOKEN = ""
		
		textoSplit = self.Respuesta.texto.split(CHARACTER_SPLIT)
		tokens = list(filter(lambda t: t != NULL_TOKEN, textoSplit))
		
		if len(tokens) > 0:
			self.Tokens = tokens
			
		else:
			raise Exception("El texto introducido, no tiene contenido válido")
