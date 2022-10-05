# SuperCatch



### Infraestructura Virtual (2022/23)

****

*Autor: danielsp13 (Daniel Pérez Ruiz)*. Repositorio para el proyecto de la asignatura Infraestructura Virtual del Grado de Ingeniería Informática de la Universidad de Granada.

****



### Problema a resolver

En la ESO / Bachillerato, se realizan muchos exámenes para comprobar que el alumnado entiende los contenidos que se imparten en las asignaturas. Sin embargo, no todas ellas se pueden realizar en un formato tipo test con opciones, si no que se requiere respuestas complejas en lenguaje natural, como puede ser el caso de Historia. El problema reside en que la corrección de dichos exámenes es una tarea en la que se tarda mucho tiempo, ya que no es una tarea puramente objetiva, lo que impide que el profesor se pueda dedicar a otras tareas, o que realice controles / tareas de seguimiento de la clase de forma más periódica para poder ayudar a sus alumnos en su fase de aprendizaje.

### Solución propuesta

Se propone una solución en forma de plataforma residente en la nube con el objetivo de:

1. Automatizar la tarea de corrección de exámenes / controles que requieren respuestas en lenguaje natural.
2. Deducir el rendimiento general de la clase a través de los resultados de dichos controles.

****

### Proceso de Creación

Recomiendo leer los siguientes documentos para tener una información más expandida acerca de cómo se ha abordado el problema y cómo se ha ido definiendo una posible solución.

* [Design Thinking](docs/obj0/design-thinking.md) : Especifica el proceso de design-thinking que he seguido acorde con las notas proporcionadas en la asignatura.
* [Modelo](docs/obj0/modelo.md) : Conceptualización más extendida del modelo de solución.

****

### Lista de comprobación inicial

Finalmente, una vez se ha desarrollado la motivación de la aplicación, se realiza la comprobación de items del proyecto:

* [x] ***¿Se trata de un problema real del que se tenga conocimiento personal?***

    Sí. Obviamente, yo no soy profesor de ninguna asignatura (al menos por ahora), pero durante la etapa de la ESO siempre he sido muy cercano con los profesores, y he percibido en primera persona la cantidad de tiempo que tardan en corregir ciertos exámenes en los que se necesita concentración y una cierta interpretación debido a la complejidad de la respuesta que se pide (por ejemplo en Historia). Además, dichos profesores me han comentado en varias ocasiones esta situación.

    

* [x] ***¿Se trata de un problema que para solucionar requiera el despliegue de una aplicación en la nube?***
  
   Por supusto. Es el lugar idóneo para el mismo, por la construcción de la solución en sí. Se necesita un acceso de varios usuarios y lo ideal es que se pueda realizar desde cualquier parte: en la misma clase, en casa de los alumnos / profesor.
   
   
   
* [x] ***¿La solución requiere una cierta cantidad de lógica de negocio, en vez solucionarse sólo almacenando y buscando?***
  
    Sí. Se requiere de un algoritmo de similitud de textos para la comparación de la respuesta otorgada por el alumno, con la propuesta del profesor. En mi caso he optado por la *similitud del coseno*. Tratando los textos a modo de vector, se calcularía la proximidad de estos vectores con el ángulo que forman, lo que permitiría estimar cómo de cerca ha estado el alumno de la respuesta del profesor. Después, sería necesario transformar el resultado del ángulo en una calificación de 0 a 10 (un formato más entendible por los humanos). Finalmente, el profesor puede estar interesado en el rendimiento general de la clase, y para ello se realizarán cálculos estadísticos que no requieren de demasiado esfuerzo.
    
    
    
* [x] ***¿Se ha incluído la configuración del repositorio y se ha enlazado desde el `README`?***

    Sí, para ello acuda al apartado de este readme: *Secciones de Interés*.

    

* [ ]  ***¿Tienes todos los datos necesarios para poder resolver el problema, o vas a requerir que el usuario los introduzca?***

    Se requiere por parte del profesor, que introduzca una plantilla de preguntas y respuestas propuestas. Y por parte del alumno, se requiere que realice el examen propuesto.

****

### Secciones de interés

Para más información adicional referente al repositorio, puede consultar los siguientes enlaces:

* [Configuración del repositorio GIT](repo-res/objetivo0-gitconfig.md)
* [Estructura del repositorio GIT](repo-res/objetivo0-gitstructure.md)