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

listaTknResp = []

for resp in listaResp:
	listaTknResp.append(TokensRespuesta(resp))
	
listaTknRespExc = []

for resp in listaRespExc:
	listaTknRespExc.append(TokensRespuesta(resp))

#=====================================================================

#Este bloque de tests verifican el funcionamiento del análisis léxico.
# Prueban que la lista de tokens es una lista no vacía, que no contiene
# tokens vacíos, ni tampoco sin caracteres; y si contienen letras,
# estas solo sean minusculas

def test_get_tokens_is_a_list():    
	for tkr in listaTknResp:
	    assert_that(tkr.getTokens(), instance_of(list))

def test_list_tokens_not_have_null_tokens():
	NULL_TOKEN = ''
	for tkr in listaTknResp:
		assert_that(tkr.getTokens().count(NULL_TOKEN),equal_to(0))

def test_list_tokens_not_empty():
	for tkr in listaTknResp:
		tkr.tokenizarTexto()
		
		assert_that(tkr.getTokens(), is_not(has_length(0)))
	
def test_exception_list_tokens_not_empty():
	for i in range(0,2):
		assert_that(calling(listaTknRespExc[i].tokenizarTexto), raises(Exception))
		
def test_list_tokens_without_punctuation():
	for tkr in listaTknResp:
		tkr.eliminarSimbolos()
		
		assert_that(tkr.getTokens(), is_not(has_length(0)))
		
def test_exception_list_tokens_without_punctuation():
	for i in range(2,4):
		assert_that(calling(listaTknRespExc[i].eliminarSimbolos), raises(Exception))

def test_list_tokens_without_capital_letters():
	for tkr in listaTknResp:
		tkr.tokensMinusculas()
		
		assert_that([tk for tk in tkr.getTokens() if re.search("[A-Z]+",tk)], has_length(0))
		
#=====================================================================

# Este bloque de tests verifican el funcionamiento de la eliminacion
# de palabras vacias. Prueba que la lista de tokens no sea vacia,
# ni tampoco contenga ninguna stopword

def test_list_tokens_without_stopwords():
	stopWords = set(stopwords.words('spanish'))	
	
	for tkr in listaTknResp:
		tkr.eliminarStopwords()
		
		assert_that([tk for tk in tkr.getTokens() if tk in stopWords], has_length(0))
		
def test_exception_tokens_without_stopwords():
	tkr = listaTknRespExc[4]
	assert_that(calling(tkr.eliminarStopwords), raises(Exception))

#=====================================================================
	
# Este test verifica el funcionamiento de la segmentacion. Prueba
# que la lista de tokens es irreducible

def test_stemming_tokens():
	for tkr in listaTknResp:
		
		tkr.segmentarTokens()
		tokensCopy = tkr.getTokens()
		tkr.segmentarTokens()
		
		assert_that(tkr.getTokens(), equal_to(tokensCopy))
	
