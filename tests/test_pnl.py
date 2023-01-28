from hamcrest import *

import re
from supercatch.respuesta import Respuesta
from supercatch.tokensRespuesta import TokensRespuesta
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

listaTknsResp = list(map(lambda resp: TokensRespuesta(resp),listaResp))

for tkr in listaTknsResp:
	tkr.procesar()

listaTknsRespExc = list(map(lambda respExcep: TokensRespuesta(respExcep), listaRespExc))

#=====================================================================

#Este bloque de tests verifican el funcionamiento del análisis léxico.
# Prueban que la lista de tokens es una lista no vacía, que no contiene
# tokens vacíos, ni tampoco sin caracteres; y si contienen letras,
# estas solo sean minusculas

def test_get_tokens_is_a_list():    
	for tkr in listaTknsResp:
		assert_that(tkr.getTokens(), instance_of(list))

def test_list_tokens_not_have_null_tokens():
	NULL_TOKEN = ''
	for tkr in listaTknsResp:
		assert_that(tkr.getTokens().count(NULL_TOKEN),equal_to(0))

def test_list_tokens_not_empty():
	for tkr in listaTknsResp:
		assert_that(tkr.getTokens(), is_not(has_length(0)))
	
def test_exception_list_tokens_not_empty():
	assert_that(calling(listaTknsRespExc[0].procesar), raises(Exception))
	assert_that(calling(listaTknsRespExc[1].procesar), raises(Exception))
		
def test_list_tokens_without_punctuation():
	for tkr in listaTknsResp:
		assert_that(list(filter(lambda tk: re.findall(r'[¿¡·!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]+',tk),tkr.getTokens())) ,has_length(0))
		
def test_exception_list_tokens_without_punctuation():
	assert_that(calling(listaTknsRespExc[2].procesar), raises(Exception))
	assert_that(calling(listaTknsRespExc[3].procesar), raises(Exception))

def test_normalized_tokens():
	for tkr in listaTknsResp:
		assert_that(list(filter(lambda tk: re.findall(r'[àáèéìíòóùú]+',tk), tkr.getTokens())), has_length(0))

def test_list_tokens_without_capital_letters():
	for tkr in listaTknsResp:
		assert_that(list(filter(lambda tk: re.search("[A-Z]+",tk), tkr.getTokens())), has_length(0))
		
#=====================================================================

# Este bloque de tests verifican el funcionamiento de la eliminacion
# de palabras vacias. Prueba que la lista de tokens no sea vacia,
# ni tampoco contenga ninguna stopword

def test_list_tokens_without_stopwords():
	STOPWORDS = set(stopwords.words('spanish'))
	for tkr in listaTknsResp:
		assert_that(list(filter(lambda tk : tk in STOPWORDS,tkr.getTokens())), has_length(0))
		
def test_exception_tokens_without_stopwords():
	assert_that(calling(listaTknsRespExc[4].procesar), raises(Exception))
