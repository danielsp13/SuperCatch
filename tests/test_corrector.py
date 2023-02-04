from hamcrest import *

try:
	from supercatch.corrector import *
	from supercatch.examen import Modelo, Examen
except:
	from corrector import *
	from examen import Modelo, Examen

#=====================================================================

# Modelo de examen
respModelo = ["'Clarín', es el apodo de Leopoldo Alas y escribió 'La Regenta'.",
"La 'ley sálica' la redactó Felipe V y permitió acceder al trono a las mujeres.",
"La matería está constituida por átomos que están formados por protones, electrones y neutrones.",
"El acero se funde a 1250 grados."]

modelo = Modelo(respModelo)

# Respuestas de alumnos

respExamen = [" La  RegenTa la escRibio leoPoLdó alas    y su   apodo fue Clarin.  ",
"Felipe IV redacto la ley salica y sirve para el acceso al trono a las mujeres.",
"La materia está constituida por moléculas que sólo tienen protones.",
"Respuesta que no tiene nada que ver con lo que se pide."]

examen = Examen(respExamen)

#=====================================================================

calificarExamen(examen,modelo)
calificaciones = examen.getCalificaciones()


#=====================================================================


def test_calificaciones():
	assert_that(calificaciones[0], equal_to(10.0))
	assert_that(calificaciones[1], close_to(7.0,0.5))
	assert_that(calificaciones[2], less_than(5))
	assert_that(calificaciones[3], close_to(0,0.5))
