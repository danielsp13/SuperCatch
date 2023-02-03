import re
from nltk.corpus import stopwords

"""
Función que realiza análisis léxico sobre el texto de una respuesta. 
Convierte las mayúsculas a minúsculas, elimina símbolos y acentos, devolviendo
la lista de palabras que conforman el texto
"""
def procesarTexto(resp: str):
	SYMBOLS = '([¿¡!·"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]+)'
	
	ACCENTS = {'a':'([àá]+)', 'e':'([èé]+)', 'i':'([ìí]+)', 'o':'([òó]+)', 'u':'([ùú]+)'}
	DIACRITICS = '|'.join(ACCENTS.values())
	
	PATTERN = re.compile('|'.join([SYMBOLS,DIACRITICS]))
	
	def conversor(match):
		#Coincidencias con simbolos
		if match.group(1) is not None:
			return ''
		
		#Coincidencias con diacriticas
		if match.group(2) is not None:
			return list(ACCENTS.keys())[0]
		if match.group(3) is not None:
			return list(ACCENTS.keys())[1]
		if match.group(4) is not None:
			return list(ACCENTS.keys())[2]
		if match.group(5) is not None:
			return list(ACCENTS.keys())[3]
		if match.group(6) is not None:
			return list(ACCENTS.keys())[4]
	
	return re.sub(PATTERN,conversor,resp.lower())
	
"""
Función que obtiene los tokens de una respuesta y elimina las
palabras vacias.
"""
def obtenerTokens(resp: str):
	NULL_TOKEN = ''
	
	UNHANDLED_STOPWORDS = ['unas']
	STOPWORDS = list(stopwords.words('spanish')) + UNHANDLED_STOPWORDS
	
	tokens = procesarTexto(resp).split()
	
	if not tokens:
		raise Exception("No hay contenido en la respuesta proporcionada.")
			
	tokens = list(filter(lambda tk: tk not in STOPWORDS,tokens))
	
	if len(tokens) == 0:
			raise Exception("El texto sólo contiene palabras vacías.")
	
	return tokens

