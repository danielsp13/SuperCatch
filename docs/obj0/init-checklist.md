# LISTA DE COMPROBACIÓN INICIAL



### Infraestructura Virtual (2022/23)

****

*Autor: danielsp13 (Daniel Pérez Ruiz)*. Este documento recoge, una vez se ha desarrollado la motivación de la aplicación, la comprobación de items del proyecto:

****

* [x] ***¿Se trata de un problema real del que se tenga conocimiento personal?***

  Sí. Obviamente, yo no soy profesor de ninguna asignatura (al menos por ahora), pero durante la etapa de la ESO siempre he sido muy cercano con los profesores, y he percibido en primera persona la cantidad de tiempo que tardan en corregir ciertos exámenes en los que se necesita concentración y una cierta interpretación debido a la complejidad de la respuesta que se pide (por ejemplo en Historia). Además, dichos profesores me han comentado en varias ocasiones esta situación.

  

* [x] ***¿Se trata de un problema que para solucionar requiera el despliegue de una aplicación en la nube?***

  Por supusto. Es el lugar idóneo para el mismo, por la construcción de la solución en sí. Se necesita un acceso de varios usuarios y lo ideal es que se pueda realizar desde cualquier parte: en la misma clase, en casa de los alumnos / profesor.

  

* [x] ***¿La solución requiere una cierta cantidad de lógica de negocio, en vez solucionarse sólo almacenando y buscando?***

  Sí. Se requiere de un algoritmo de similitud de textos para la comparación de la respuesta otorgada por el alumno, con la propuesta del profesor. En mi caso he optado por la *similitud del coseno*. Tratando los textos a modo de vector, se calcularía la proximidad de estos vectores con el ángulo que forman, lo que permitiría estimar cómo de cerca ha estado el alumno de la respuesta del profesor. Después, sería necesario transformar el resultado del ángulo en una calificación de 0 a 10 (un formato más entendible por los humanos). Finalmente, el profesor puede estar interesado en el rendimiento general de la clase, y para ello se realizarán cálculos estadísticos que no requieren de demasiado esfuerzo.

  

* [x] ***¿Se ha incluído la configuración del repositorio y se ha enlazado desde el `README`?***

  Sí, para ello acuda al apartado de este readme: *Secciones de Interés*.

  

* [x] ***¿Tienes todos los datos necesarios para poder resolver el problema, o vas a requerir que el usuario los introduzca?***

  Por parte del alumno, se requiere que realice el examen propuesto por el profesor.