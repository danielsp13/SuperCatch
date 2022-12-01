from pregunta import *
from respuesta import *

from dataclasses import dataclass

@dataclass
class resolucionExamen:

    '''Clase que representa un examen y su corrección como:
        - Tema asociado al examen como cadena (ej: Tema 4)
        - Tipo de examen: prueba o real
        - Secuencia de preguntas
        - Secuencia de respuestas de todos los alumnos'''
    tema: str
    tipo = ['PRUEBA', 'REAL']
    preguntas: list
    respuestas: list

    def __init__(self, tema_examen: str):
        self.tema = tema_examen
        self.tipo = 0
        self.preguntas = []
        self.respuestas = []

    def __init__(self, tema_examen: str, type: str):
        self.tema = tema_examen
        self.tipo = type
        self.preguntas = []
        self.respuestas = []

    def aniadir_pregunta(self, preg: Pregunta):
        self.preguntas.insert(preg.numero-1, preg)

    def aniadir_respuesta(self, resp: Respuesta):
        self.respuestas.append(resp)
