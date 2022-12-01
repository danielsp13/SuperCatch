from dataclasses import dataclass

from alumno import *

@dataclass
class Respuesta:

    '''Clase que representa la respuesta propuesta por el alumno'''
    numero: int
    respuesta: str
    calificacion: int

    alumno: Alumno

    def __init__(self, num: int):
        self.numero = num
        self.respuesta = ''
        self.calificacion = 0
        self.alumno = Alumno()

    def __init__(self, num: int, res: str):
        self.numero = num
        self.respuesta = res
        self.calificacion = 0
        self.alumno = Alumno()

    def aniadir_nota(self, nota: int):
        self.calificacion = nota
