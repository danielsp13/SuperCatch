from pregunta import *
from respuesta import *

from dataclasses import dataclass

@dataclass
class resolucionExamen:

    '''Clase que representa un examen y su corrección como:
        - Tipo de examen: prueba o real
        - Secuencia de preguntas
        - Secuencia de respuestas de todos los alumnos'''
    tipo = ['PRUEBA', 'REAL']
    preguntas: list
    respuestas: list

    def __init__(self):
        self.tipo = 0
        self.preguntas = []
        self.respuestas = []

    def __init__(self, type: str):
        self.tipo = type
        self.preguntas = []
        self.respuestas = []
