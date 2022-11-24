from pregunta import *
from respuesta import *
from alumno import *

class resolucionExamen:

    id_examen: int
    preguntas: list
    respuestas: list

    def __init__(self):
        self.id_examen = 0
        self.preguntas = []
        self.respuestas = []

    def __init__(self, id):
        self.id_examen = id
        self.preguntas = []
        self.respuestas = []

    def get_id(self):
        return self.id_examen

    def aniadir_pregunta(self, preg:Pregunta):
        self.preguntas.insert(preg.get_numero-1, preg)

    def aniadir_respuesta(self, resp:Respuesta):
        self.respuestas.append(resp)
