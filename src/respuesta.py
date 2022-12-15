from dataclasses import dataclass

@dataclass
class Respuesta:

    '''Clase que representa la respuesta propuesta por el alumno'''
    numero: int
    respuesta: str
    calificacion: int

    def __init__(self, num: int):
        self.numero = num
        self.respuesta = ''
        self.calificacion = 0

    def __init__(self, num: int, res: str):
        self.numero = num
        self.respuesta = res
        self.calificacion = 0
