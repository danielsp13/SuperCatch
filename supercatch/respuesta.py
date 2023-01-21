from dataclasses import dataclass

@dataclass(frozen=True)
class Respuesta:
    texto: str

    def __init__(self,texto):
        self.texto = texto