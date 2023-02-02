from supercatch.respuesta import Respuesta
from supercatch.examen import Examen, Modelo
from supercatch.pln import *
from math import sqrt

def obtenerPonderacionTerminos(respAlumno: Respuesta, respModelo: Respuesta):
	TOKENS_ALUMNO = obtenerTokens(respAlumno)
	TOKENS_MODELO = obtenerTokens(respModelo)

	TERMINOS = sorted(list(set(TOKENS_ALUMNO + TOKENS_MODELO)))
	ponderacion = [[],[]]
			
	for termino in TERMINOS:
		if termino in TOKENS_ALUMNO:
			ponderacion[0].append(1)
		else:
			ponderacion[0].append(0)
			
		if termino in TOKENS_MODELO:
			ponderacion[1].append(1)
		else:
			ponderacion[1].append(0)
	
	return ponderacion

	
def calificarRespuesta(respAlumno: Respuesta, respModelo: Respuesta):
	PONDERACIONES = obtenerPonderacionTerminos(respAlumno,respModelo)
	V_ALUMNO = PONDERACIONES[0]; V_MODELO = PONDERACIONES[1]
	FACTOR = 10
	
	def cdot(vectA, vectM):
		cdot = 0
		for i in range(0,len(vectM)):
			cdot += vectA[i]*vectM[i]
			
		return cdot
	
	def module(vect):
		return sqrt(sum(list(map(lambda comp: comp*comp,vect))))
	
	prodEscalar = cdot(V_ALUMNO,V_MODELO)
	modVA = module(V_ALUMNO)
	modVM = module(V_MODELO)
	
	similitud = prodEscalar / (modVA * modVM)
	
	return round(similitud * FACTOR,2)
	
	
def calificarExamen(examenAlumno: Examen, examenModelo: Modelo):
	RESP_MODELO = examenModelo.getRespuestas()
	RESP_ALUMNO = examenAlumno.getRespuestas()
	
	for i in range(0,len(RESP_ALUMNO)):
		examenAlumno.addCalificacion(calificarRespuesta(RESP_ALUMNO[i],RESP_MODELO[i]))

