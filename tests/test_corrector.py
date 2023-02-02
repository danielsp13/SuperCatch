from hamcrest import *

from supercatch.corrector import *
from supercatch.respuesta import Respuesta
from supercatch.examen import Modelo, Examen

#=====================================================================

# Modelo de examen
modelo = Modelo()

modelo.addRespuesta(Respuesta("'Clarín', es el apodo de Leopoldo Alas y escribió 'La Regenta'."))
modelo.addRespuesta(Respuesta("La 'ley sálica' la redactó Felipe V y permitió acceder al trono a las mujeres."))
modelo.addRespuesta(Respuesta("La matería está constituida por átomos que están formados por protones, electrones y neutrones."))
modelo.addRespuesta(Respuesta("El acero se funde a 1250 grados."))

# Respuestas de alumnos
examen = Examen()

examen.addRespuesta(Respuesta(" La  RegenTa la escRibio leoPoLdó alas    y su   apodo fue Clarin.  "))
examen.addRespuesta(Respuesta("Felipe IV redacto la ley salica y sirve para el acceso al trono a las mujeres."))
examen.addRespuesta(Respuesta("La materia está constituida por moléculas que sólo tienen protones."))
examen.addRespuesta(Respuesta("Respuesta que no tiene nada que ver con lo que se pide."))


#=====================================================================

calificarExamen(examen,modelo)
calificaciones = examen.getCalificaciones()


#=====================================================================


def test_calificaciones():
	assert_that(calificaciones[0], equal_to(10.0))
	assert_that(calificaciones[1], close_to(7.0,0.5))
	assert_that(calificaciones[2], less_than(5))
	assert_that(calificaciones[3], close_to(0,0.5))
