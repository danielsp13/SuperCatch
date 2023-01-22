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

# Respuestas para pruebas (excepciones)
listaRespExc = []

listaRespExc.append(Respuesta(""))
listaRespExc.append(Respuesta("        "))


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
	for tkrE in listaTknRespExc:
		assert_that(calling(tkrE.tokenizarTexto), raises(Exception))

