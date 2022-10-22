# MODELO DE SOLUCIÓN



### Infraestructura Virtual (2022/23)

****

*Autor: danielsp13 (Daniel Pérez Ruiz)*. Este documento lo he creado para desarrollar un primer modelo orientativo para la solución que propongo, en el que reflejaré con más detalle que en el readme algunas cuestiones que son importantes y necesarias para validar, principalmente, la lógica de negocio que hay detrás de la aplicación.

****

#### Fase 1: ¿Quiénes son los usuarios reales de la aplicación? ¿Y clientes?

Usando la metodología de "personas":

> Dolores Cabrera, 52 años, profesora de Historia en un instituto de la ESO. Tras varios años impartiendo clase en el instituto ha comprobado que, a medida que pasa el tiempo, sus alumnos no estudian adecuadamente los contenidos de su asignatura. Para ello, considera de utilidad realizar controles / exámenes de prueba, pero el tiempo que se invierte en diseñarlos, y posteriormente corregirlos y obtener conclusiones generales es una tarea en la que se pierde mucho tiempo. Le gustaría una solución que le permitiera automatizar esta tarea, y recibir una estimación acerca de la situación de la clase en conjunto.



***Nuestro cliente serán profesores como Lola, que esperan una solución informatizada que permita atender a otras necesidades de mayor interés, liberandole de la tarea de corrección de los exámenes.***

Los usuarios de la plataforma son: *el profesor*, y *los alumnos*.

****

#### Fase 2: ¿Qué datos se necesitan para la solución? ¿Quiénes los proporcionan? 

Para la aplicación se requieren los siguientes datos:

* *Plantilla de preguntas y resultados del profesor: Proporcionado por el profesor. Esta será la base para la comparación con las respuestas otorgadas por los alumnos* 
* *Resolución del examen: Proporcionado por los alumnos.* 

****

#### Fase 3: ¿Qué lógica de negocio hay detrás de la aplicación?

Se requiere la utilización de algoritmos de similitud de textos, concretamente, optaré por el *algoritmo de similitud del coseno*. La idea consiste en tratar el texto de la respuesta (tanto del profesor como del alumno) como un vector normalizado, y comprobar cómo de cerca se encuentran, teniendo en cuenta el ángulo que formarían dichos vectores. *Ejemplo: un ángulo pequeño, implicaría una respuesta más acertada de acuerdo a lo escrito por el profesor.*

Una vez se haya realizado esto, será necesario establecer una calificación en un formato más humano. No presenta demasiado problema, pues sólo sería necesario llevar el resultado de similitud (intervalo [0, $\pi$/2]) al intervalo [0,10].

Lo anterior, sería la verdadera lógica de negocio que hay detrás. Sin embargo, de manera adicional sería interesante obtener conclusiones acerca del rendimiento general de todos los alumnos, haciendo cálculos estadísticos sencillos con las calificaciones. 



****

****



#### Comprobación de items de proyecto

En esta última sección, se verifica que el modelo de solución planteada al problema analizado en el apartado de ***[Desing Thinking](design-thinking.md)*** es correcta y resuelve al menos las cuestiones esenciales:

* [x] ***¿Se trata de un problema real del que se tenga conocimiento personal?***

  Sí. Obviamente, yo no soy profesor de ninguna asignatura (al menos por ahora), pero durante la etapa de la ESO siempre he sido muy cercano con los profesores, y he percibido en primera persona la cantidad de tiempo que tardan en corregir ciertos exámenes en los que se necesita concentración y una cierta interpretación debido a la complejidad de la respuesta que se pide (por ejemplo en Historia). Además, dichos profesores me han comentado en varias ocasiones esta situación.

  

* [x] ***¿Se trata de un problema que para solucionar requiera el despliegue de una aplicación en la nube?***

  Por supusto. Es el lugar idóneo para el mismo, por la construcción de la solución en sí. Se necesita un acceso de varios usuarios y lo ideal es que se pueda realizar desde cualquier parte: en la misma clase, en casa de los alumnos / profesor.



* [x] ***¿La solución requiere una cierta cantidad de lógica de negocio, en vez solucionarse sólo almacenando y buscando?***

  Sí. Explicado en la **Fase 3**.



* [x] ***¿Tienes todos los datos necesarios para poder resolver el problema, o vas a requerir que el usuario los introduzca?***

  Por parte del alumno, se requiere que realice el examen propuesto por el profesor.
