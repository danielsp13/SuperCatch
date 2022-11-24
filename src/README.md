Tal como se contempló en el issue [#11](https://github.com/danielsp13/SuperCatch/issues/11) se ha definido el conjunto de objetos valor y entidades necesarias para llevar a cabo el [M0](https://github.com/danielsp13/SuperCatch/blob/main/docs/milestones.md#checkered_flag-m0-representaci%C3%B3n-inicial-del-modelo-definici%C3%B3n-de-entidades-a-trav%C3%A9s-de-clases):

Clase Pregunta: En este objeto valor inmutable hemos definido la respuesta correcta asociada a una pregunta del examen con un identificador (número de la pregunta), una cadena de caracteres donde se define la respuesta y un listado de palabras clave para facilitar la corrección como vemos en la [HU01](https://github.com/danielsp13/SuperCatch/blob/main/docs/user-stories.md#black_nib-hu01-dolores-quiere-agilizar-la-tarea-de-correcci%C3%B3n-de-ex%C3%A1menes)

Clase Respuesta: Al igual que anteriormente, hemos definido una clase inmutable donde se albergará la respuesta realizada por parte del alumno identificada mediante el número de pregunta con el que aparezca en el examen.

Clase ResolucionExamen: Esta entidad estará destinada a relacionar las preguntas (respuestas correctas) y respuestas por parte de la totalidad de los alumnos con el examen (identificado por un id) que incluya dichas preguntas y respuestas. Aquí se podrá realizar el posterior algoritmo de comparación para valorar la calidad de las respuestas añadiendo métodos básicos como añadir preguntas y respuestas a la lista de las mismas.

Clase Alumno: Esta entidad estará destinada a recoger los datos personales del alumno, además de las calificaciones que vaya obteniendo en los exámenes del curso.
