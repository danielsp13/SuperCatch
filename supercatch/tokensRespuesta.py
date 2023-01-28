from supercatch.respuesta import Respuesta

import re
from nltk.corpus import stopwords

class TokensRespuesta:
	Tokens: list
	
	def __init__(self,resp):
		self.Tokens = resp.texto.split()
		
	def getTokens(self):
		return self.Tokens
		
	def procesar(self):
		self.__eliminarSimbolos()
		self.__eliminarTokensNulos()
		self.__eliminarMayusculas()
		
	def __eliminarSimbolos(self):
		PATTERN = r'[¿¡!·"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]+'
		REPLACE_SYMBOL = ''
	
		tokens = list(map(lambda tk: re.sub(PATTERN,REPLACE_SYMBOL,tk), self.Tokens))
		
		if tokens.count(REPLACE_SYMBOL) == len(tokens):
			raise Exception("El texto no contiene palabras.")
			
		else:
			self.Tokens = tokens

	def __eliminarTokensNulos(self):
		NULL_TOKEN = ''
		tokens = list(filter(lambda tk: tk != NULL_TOKEN, self.Tokens))
		
		if len(tokens) == 0:
			raise Exception("No hay contenido en la respuesta proporcionada.")
			
		else:
			self.Tokens = tokens
	
	def __eliminarMayusculas(self):
		self.Tokens = list(map(lambda tk: tk.lower(), self.Tokens))
		
	def eliminarStopwords(self):
		STOPWORDS = list(stopwords.words('spanish'))

		tokens = [tk for tk in self.Tokens if tk not in STOPWORDS]
		
		if len(tokens) > 0:
			self.Tokens = tokens
			
		else:
			raise Exception("El texto sólo contiene palabras vacías.")
