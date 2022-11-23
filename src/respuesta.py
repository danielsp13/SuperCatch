from dataclasses import dataclass

@dataclass
class Respuesta:

    numero: int
    respuesta: str

    def __init__(self, num: int):
        self.numero = num
        self.respuesta = ''

    def __init__(self, num: int, res: str):
        self.numero = num
        self.respuesta = res
    
    def get_numero(self):
        return self.numero

    def get_respuesta(self):
        return self.respuesta
