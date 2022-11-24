class Alumno:

    dni: int
    nombre: str
    apellidos: str
    calificaciones: list

    def __init__(self, id:int):
        self.dni = id
        self.nombre = ''
        self.apellidos = ''
        self.calificaciones = []

    def get_dni(self):
        return self.dni

    def get_nombre(self):
        return self.nombre
    
    def get_apellidos(self):
        return self.apellidos

    def aniadir_nota(self, nota:int):
        self.calificaciones.append(nota)
    
    
