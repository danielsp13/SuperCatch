from dataclasses import dataclass

@dataclass(frozen=True)
class Alumno:

    '''Clase que representa un alumno que realiza el examen'''
    dni: int
    nombre: str
    apellidos: str
    curso: int

    def __init__(self, id: int):
        self.dni = id
        self.nombre = ''
        self.apellidos = ''
        self.curso = 0
    
    
    
