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
		self.__eliminarAcentos()
		self.__eliminarStopwords()
		
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
		
	def __eliminarStopwords(self):
		UNHANDLED_STOPWORDS = ['unas']
		STOPWORDS = list(stopwords.words('spanish')) + UNHANDLED_STOPWORDS

		tokens = list(filter(lambda tk: tk not in STOPWORDS,self.Tokens))
		
		if len(tokens) == 0:
			raise Exception("El texto sólo contiene palabras vacías.")
			
		else:
			self.Tokens = tokens
			
	def __eliminarAcentos(self):
		ACCENTS = {'a':'([àá]+)', 'e':'([èé]+)', 'i':'([ìí]+)', 'o':'([òó]+)', 'u':'([ùú]+)'}
		PATTERN = re.compile('|'.join(ACCENTS.values()))
		
		def conversor(match):
			if match.group(1) is not None:
				return list(ACCENTS.keys())[0]
			if match.group(2) is not None:
				return list(ACCENTS.keys())[1]
			if match.group(3) is not None:
				return list(ACCENTS.keys())[2]
			if match.group(4) is not None:
				return list(ACCENTS.keys())[3]
			if match.group(5) is not None:
				return list(ACCENTS.keys())[4]
		
		self.Tokens = list(map(lambda tk: re.sub(PATTERN,conversor,tk), self.Tokens))
