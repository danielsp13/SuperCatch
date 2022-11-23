from dataclasses import dataclass

@dataclass
class Pregunta:

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
    
    def get_numero(self):
        return self.numero

    def get_respuesta(self):
        return self.respuesta

    def get_palabra_clave(self, posicion: int):
        return self.palabras_clave[posicion]
    
    def get_posicion_palabra(self, palabra: str):
        return self.palabras_clave.index(palabra)

    def aniadir_palabra_clave(self, palabra: str):
        self.palabras_clave.append(palabra)
