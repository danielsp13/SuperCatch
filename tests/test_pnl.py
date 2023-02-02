from hamcrest import *

import re
from supercatch.tokensRespuesta import *
from supercatch.respuesta import Respuesta
from nltk.corpus import stopwords

#=====================================================================

# Respuestas para pruebas
listaResp = []

listaResp.append(Respuesta("Esta es una respusta de ejemplo."))
listaResp.append(Respuesta("   Esta   es   otra   respuesta    . "))
listaResp.append(Respuesta("¿Qué se supone    que debo responder aquí?"))
listaResp.append(Respuesta("   - 'A quién madruga,   Dios   le ayuda' -, dijo alguien alguna vez."))
listaResp.append(Respuesta("eStA eS   uNA   RESPuesTA MuY DIFÍCIL de leeR. ¿Sí?"))
listaResp.append(Respuesta("dEntRO de un AÑO, será 2024."))

# Respuestas para pruebas (excepciones)
listaRespExc = []

listaRespExc.append(Respuesta(""))
listaRespExc.append(Respuesta("        "))
listaRespExc.append(Respuesta("?!;.-·¡.;!/,¿"))
listaRespExc.append(Respuesta(" ¿?! !' ?  ! ; . - ·¡ .;! /,¿"))
listaRespExc.append(Respuesta("el, los las unas de para   sobre durante en."))

#=====================================================================

tokensResp = list(map(lambda resp: obtenerTokens(resp), listaResp))

#=====================================================================


"""
Bloque de tests que verifican el funcionamiento del analisis lexico.
Prueban que la lista de tokens es una lista no vacia, que no contiene
tokens nulos, ni tampoco sin caracteres; y si contienen letras, estas
solo sean minusculas
"""

def test_get_tokens_is_a_list():    
	for tokens in tokensResp:
		assert_that(tokens, instance_of(list))

def test_list_tokens_not_have_null_tokens():
	NULL_TOKEN = ''
	for tokens in tokensResp:
		assert_that(tokens.count(NULL_TOKEN),equal_to(0))

def test_list_tokens_not_empty():
	for tokens in tokensResp:
		assert_that(tokens, is_not(has_length(0)))
	
def test_exception_list_tokens_not_empty():
	assert_that(calling(obtenerTokens).with_args(listaRespExc[0]), raises(Exception))
	assert_that(calling(obtenerTokens).with_args(listaRespExc[1]), raises(Exception))
		
def test_list_tokens_without_punctuation():
	PATTERN = r'[¿¡·!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]+'

	for tokens in tokensResp:
		assert_that(list(filter(lambda tk: re.findall(PATTERN,tk),tokens)) ,has_length(0))
		
def test_exception_list_tokens_without_punctuation():
	assert_that(calling(obtenerTokens).with_args(listaRespExc[2]), raises(Exception))
	assert_that(calling(obtenerTokens).with_args(listaRespExc[3]), raises(Exception))

def test_normalized_tokens():
	PATTERN = r'[àáèéìíòóùú]+'

	for tokens in tokensResp:
		assert_that(list(filter(lambda tk: re.findall(PATTERN,tk), tokens)), has_length(0))

def test_list_tokens_without_capital_letters():
	PATTERN = r'[A-Z]+'	
	
	for tokens in tokensResp:
		assert_that(list(filter(lambda tk: re.search(PATTERN,tk), tokens)), has_length(0))
		
#=====================================================================

"""
Bloque de tests que verifican el funcionamiento de la eliminacion
de palabras vacias. Prueba que la lista de tokens no sea vacia, ni
tampoco contenga ninguna stopword
"""

def test_list_tokens_without_stopwords():
	STOPWORDS = set(stopwords.words('spanish'))
	for tokens in tokensResp:
		assert_that(list(filter(lambda tk : tk in STOPWORDS,tokens)), has_length(0))
		
def test_exception_tokens_without_stopwords():
	assert_that(calling(obtenerTokens).with_args(listaRespExc[4]), raises(Exception))
