from hamcrest import *

from supercatch.respuesta import Respuesta
from supercatch.tokensRespuesta import TokensRespuesta

#=====================================================================

NULL_TOKEN = '' 

# Respuestas para pruebas
listaResp = []

listaResp.append(Respuesta("Esta es una respusta de ejemplo."))
listaResp.append(Respuesta("   Esta   es   otra   respuesta    . "))
listaResp.append(Respuesta("¿Qué se supone    que debo responder aquí?"))
listaResp.append(Respuesta("   - 'A quién madruga,   Dios   le ayuda' -, dijo alguien alguna vez."))

# Respuestas para pruebas (excepciones)
listaRespExc = []

listaRespExc.append(Respuesta(""))
listaRespExc.append(Respuesta("        "))
listaRespExc.append(Respuesta("?!;.-·¡.;!/,¿"))
listaRespExc.append(Respuesta(" ¿?! !' ?  ! ; . - ·¡ .;! /,¿"))

listaTknResp = []

for resp in listaResp:
	listaTknResp.append(TokensRespuesta(resp))
	
listaTknRespExc = []

for resp in listaRespExc:
	listaTknRespExc.append(TokensRespuesta(resp))

#=====================================================================


def test_get_tokens_is_a_list():    
	for tkr in listaTknResp:
	    assert_that(tkr.getTokens(), instance_of(list))

def test_list_tokens_not_have_null_tokens():
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
		tkr.tokenizarTexto(); tkr.eliminarSimbolos()
		
		assert_that(tkr.getTokens(), is_not(has_length(0)))
		
def test_exception_list_tokens_without_punctuation():
	for i in range(2,4):
		listaTknRespExc[i].tokenizarTexto()
		assert_that(calling(listaTknRespExc[i].eliminarSimbolos), raises(Exception))

