from supercatch.respuesta import Respuesta

from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from unidecode import unidecode

class TokensRespuesta:
	Tokens: list
	
	def __init__(self,resp):
		self.Tokens = resp.texto.split()
		
	def getTokens(self):
		return self.Tokens

	def tokenizarTexto(self):
	
		unhandled_symbols = ['.','¡','¿']
		textoFormateado = self.Respuesta.texto.replace('·','')
		for symbol in unhandled_symbols:
			textoFormateado = textoFormateado.replace(symbol,'')
		
		textoNormalizado = unidecode(textoFormateado)
		
		tokens = word_tokenize(textoNormalizado)
		
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

	
	def tokensMinusculas(self):
		
		self.Tokens = [tk.lower() for tk in self.Tokens]
		
	def eliminarStopwords(self):
		
		stopWords = set(stopwords.words('spanish'))

		tokens = [tk for tk in self.Tokens if tk not in stopWords]
		
		if len(tokens) > 0:
			self.Tokens = tokens
			
		else:
			raise Exception("El texto sólo contiene palabras vacías.")
		
