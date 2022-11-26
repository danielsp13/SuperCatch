from dataclasses import dataclass

@dataclass(frozen=True)
class Pregunta:

    '''Clase que representa la respuesta correcta a una pregunta'''
    numero: int
    respuesta: str
    palabras_clave: list

    def __init__(self, num: int):
        self.numero = num
        self.respuesta = ''
        self.palabras_clave = []

    def __init__(self, num: int, res: str):
        self.numero = num
        self.respuesta = res
        self.palabras_clave = []

    def get_palabra_clave(self, posicion: int):
        return self.palabras_clave[posicion]

    def aniadir_palabra_clave(self, palabra: str):
        self.palabras_clave.append(palabra)
