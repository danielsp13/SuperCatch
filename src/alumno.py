from dataclasses import dataclass

@dataclass(frozen=True)
class Alumno:

    '''Clase que representa un alumno que realiza el examen'''
    dni: int
    nombre: str
    apellidos: str
    curso: int

    def __init__(self, id: int):
        object.__setattr__(self, "dni", id)
        object.__setattr__(self, "nombre", '')
        object.__setattr__(self, "apellidos", '')
        object.__setattr__(self, "curso", 0)
    
    
    
