from dataclasses import dataclass

@dataclass(frozen=True)
class Respuesta:
	texto: str

	def __init__(self,texto):
		object.__setattr__(self,'texto',texto)
