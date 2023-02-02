from respuesta import Respuesta

class Modelo:
	respuestas: list
	
	def __init__(self,resp = []):
		self.respuestas = resp
		
	def addRespuesta(self, resp: Respuesta):
		self.respuestas.append(resp)
		
	def getRespuestas(self):
		return self.respuestas

class Examen(Modelo):
	calificaciones: list
	
	def __init__(self, resp = []):
		super().__init__(resp)
		self.calificaciones = []
		
	def addCalificacion(self, nota: float):
		self.calificaciones.append(nota)
		
	def getCalificaciones(self):
		return self.calificaciones
