from supercatch.respuesta import Respuesta

from string import punctuation
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from unidecode import unidecode

#Entidad que procesa el texto de las respuestas obteniendo los tokens
# que lo identifican
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
		"""
		Normaliza y particiona una respuesta, obteniendo sus tokens
		"""
	
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
		"""
		Elimina los tokens que no contienen caracteres
		"""
		
		tokens = [tk for tk in self.Tokens if tk not in punctuation]
		
		if len(tokens) > 0:
			self.Tokens = tokens
			
		else:
			raise Exception("El texto no contiene palabras.")

	
	def tokensMinusculas(self):
		"""
		Transforma los caracteres que contienen mayusculas
		a minusculas
		"""
		
		self.Tokens = [tk.lower() for tk in self.Tokens]
		
	def eliminarStopwords(self):
		"""
		Elimina los tokens que son palabras vacias
		"""
		
		stopWords = set(stopwords.words('spanish'))

		tokens = [tk for tk in self.Tokens if tk not in stopWords]
		
		if len(tokens) > 0:
			self.Tokens = tokens
			
		else:
			raise Exception("El texto sólo contiene palabras vacías.")
			
	def segmentarTokens(self):
		"""
		Calcula los stem de los tokens
		"""
		
		stemmer = SnowballStemmer('spanish')
		
		self.Tokens = [stemmer.stem(tk) for tk in self.Tokens]
		
