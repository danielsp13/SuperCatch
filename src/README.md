Tal como se contempló en el issue [#11](https://github.com/danielsp13/SuperCatch/issues/11) se ha definido el conjunto de objetos valor y entidades necesarias para llevar a cabo el [M0](https://github.com/danielsp13/SuperCatch/blob/main/docs/milestones.md#checkered_flag-m0-representaci%C3%B3n-inicial-del-modelo-definici%C3%B3n-de-entidades-a-trav%C3%A9s-de-clases):

Clase Pregunta: En este objeto valor inmutable hemos definido la respuesta correcta asociada a una pregunta del examen con un identificador (número de la pregunta), una cadena de caracteres donde se define la respuesta y un listado de palabras clave para facilitar la corrección como vemos en la [HU01](https://github.com/danielsp13/SuperCatch/blob/main/docs/user-stories.md#black_nib-hu01-dolores-quiere-agilizar-la-tarea-de-correcci%C3%B3n-de-ex%C3%A1menes)

Clase Respuesta: Al igual que anteriormente, hemos definido una clase inmutable donde se albergará la respuesta realizada por parte del alumno identificada mediante el número de pregunta con el que aparezca en el examen.

Clase ResolucionExamen: Esta entidad estará destinada a relacionar las preguntas (respuestas correctas) y respuestas por parte de la totalidad de los alumnos con el examen (identificado por un id) que incluya dichas preguntas y respuestas. Aquí se podrá realizar el posterior algoritmo de comparación para valorar la calidad de las respuestas añadiendo métodos básicos como añadir preguntas y respuestas a la lista de las mismas.

Clase Alumno: Esta entidad estará destinada a recoger los datos personales del alumno, además de las calificaciones que vaya obteniendo en los exámenes del curso.

De acuerdo a las historias de usuario [HUO1](https://github.com/danielsp13/SuperCatch/blob/main/docs/user-stories.md#black_nib-hu01-dolores-quiere-agilizar-la-tarea-de-correcci%C3%B3n-de-ex%C3%A1menes) y [HU03](https://github.com/danielsp13/SuperCatch/blob/main/docs/user-stories.md#black_nib-hu03-irene-necesita-entrenar-para-sus-ex%C3%A1menes), se han definido cuatro PMVs que definen las peticiones necesarias para satisfacer el [M0](https://github.com/danielsp13/SuperCatch/blob/main/docs/milestones.md#checkered_flag-m0-representaci%C3%B3n-inicial-del-modelo-definici%C3%B3n-de-entidades-a-trav%C3%A9s-de-clases):

## PREGUNTA:
Se define un **objeto valor** que define la respuesta correcta asociada a una pregunta del examen propuesta. Para agilizar la corrección de acuerdo con la [HU01](https://github.com/danielsp13/SuperCatch/blob/main/docs/user-stories.md#black_nib-hu01-dolores-quiere-agilizar-la-tarea-de-correcci%C3%B3n-de-ex%C3%A1menes) hemos definido tres campos: *número* de la pregunta, *texto* asociado a la respuesta correcta y lista de *palabras clave* que permiten obtener las palabras más importantes.

## RESPUESTA:
Se define como una **entidad** que define la respuesta propuesta por el alumno a una pregunta del examen. Teniendo en cuenta que se ha de facilitar la corrección, se propone la definición de varios campos necesarios como: *número* de la pregunta respondida, *texto* escrito por el alumno, *calificacion* que se obtiene de esa respuesta y *alumno* que responde esa pregunta.

## ALUMNO:
Se define otro **objeto valor** que corresponde al alumno que realiza el examen. Con el fin de modelar este alumno únicamente hemos definido campos personales del mismo como: *dni* para identificarlo, *nombre* y *apellidos*, y *curso* en el que se encuentra.

## RESOLUCIONEXAMEN:
Se define otra **entidad** que va a dar formato a la unión de preguntas y respuestas del alumnado a un examen en concreto. Según la [HU03](https://github.com/danielsp13/SuperCatch/blob/main/docs/user-stories.md#black_nib-hu03-irene-necesita-entrenar-para-sus-ex%C3%A1menes), hemos de tener en cuenta que se puede practicar en casa por lo que definiremos dos tipos de examen quedando así la estructura de la entidad: *tipo* de examen (prueba o real), lista de *preguntas* que se proponen a resolver y lista de *respuestas* de la totalidad de los alumnos.
