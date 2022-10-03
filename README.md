# SUPERCATCH



### Infraestructura Virtual (2022/23)

****

*Autor: danielsp13 (Daniel Pérez Ruiz)*. Repositorio para el proyecto de la asignatura Infraestructura Virtual del Grado de Ingeniería Informática de la Universidad de Granada.

****



### Problema a resolver

En el deporte, la disciplina y el entrenamiento son dos máximas que se deben cumplir si se quieren conseguir unos determinados objetivos. Por supuesto, todos queremos evolucionar a una versión mejor de nosotros mismos, y eso es un factor clave en los deportes individuales/grupales, pero a veces nos cuesta seguir una hoja de ruta para ello. En el ámbito del fútbol (en cualquier categoría), gestionar este caso a toda una plantilla puede no ser una tarea tan sencilla, especialmente teniendo características de jugadores tan variadas. Es por tanto que el problema a resolver, puede ser expresada de la siguiente forma: ¿cómo puede un entrenador elegir adecuadamente los ejercicios de entrenamiento para una sesión, mejorando las debilidades y que ayude a conseguir efectos de mejoría en la plantilla?

### Solución propuesta

Se plantea una solución al problema de la optimización y planificación de entrenamientos en forma de aplicación desplegada en la nube tal que:

* Con los datos de los atributos de los jugadores y una lista de ejercicios de entrenamiento, analizar las características de la plantilla y decidir una planificación de una sesión diaría de entrenamiento equilibrada y acorde con las necesidades de la plantilla.
* Permitir calificar a los jugadores observando una tendencia evolutiva en ellos, generando informes para cada uno en caso de que el entrenador lo requiera.
* Sugerir un 11 titular en función de los resultados y de la mejora de los atributos.

****

### Proceso de Creación

Recomiendo leer los siguientes documentos para tener una información más expandida acerca de cómo se ha abordado el problema y cómo se ha ido definiendo una posible solución.

* [Design Thinking](docs/obj0/design-thinking.md) : Especifica el proceso de design-thinking que he seguido acorde con las notas proporcionadas en la asignatura.
* [Modelo](docs/obj0/modelo.md) : Conceptualización más extendida del modelo de solución.

****

### Lista de comprobación inicial

Finalmente, una vez se ha desarrollado la motivación de la aplicación, se realiza la comprobación de items del proyecto:

* [x] ***¿Se trata de un problema real del que se tenga conocimiento personal?***

    No es un problema que me involucre a mi personalmente ni directamente. Sin embargo, además de obtener testimonios a través de uno de mis mejores amigos de toda la vida (que es jugador de fútbol en un equipo regional), también he podido comprobar de primera mano cuando le he acompañado en alguna que otra ocasión, cómo se realizaban dichos entrenamientos. Ahí fue cuando pensé en esta solución para optimizar las rutinas que hacían diariamente, con el objetivo de ayudar al cuerpo técnico a un posible mejor rendimiento. 

    También considero que esta solución podría ser extrapolable al ámbito personal, pues todos siempre hemos tenido la necesidad de organizarnos adecuadamente una rutina de ejercicio que garantice que sea equilibrada, efectiva, y atendiendo a nuestros propios atributos.

    

* [x] ***¿Se trata de un problema que para solucionar requiera el despliegue de una aplicación en la nube?***
   
   Por supuesto. Se requiere de un volumen de datos considerable (fichas, atributos de jugadores, listado de entrenamientos,..) además de determinados cálculos que hacen que la nube sea el lugar idóneo para esta solución. También hay que tener en cuenta que el equipo no tiene por qué entrenar siempre en el mismo lugar, por ejemplo si juega de visitante es posible que acuda a otras instalaciones, por tanto es esencial que se garantice el acceso desde cualquier parte.
   
   
   
* [x] ***¿La solución requiere una cierta cantidad de lógica de negocio, en vez solucionarse sólo almacenando y buscando?***
    
    Sí. *En primer lugar, como prerrequisito se requiere el acceso a las fichas de los jugadores y sus atributos, datos que debe proporcional la sección deportiva del club (léase sección de "modelo"), así como que el cuerpo técnico proporcione una lista con todos los ejercicios de entrenamiento que considere. ¿Esto último de los ejercicios también es necesario? Sí, es necesario a pesar de que se pueda pensar que son muchas inserciones, pero la aplicación debe ser flexible atendiendo a las ideas de dicho cuepo técnico (ejemplo: estaríamos muy limitados si los ejercicios son por defecto impuesto por nosotros / acceso a API, y de repente se produce un cambio de entrenador y ve que no le convencen los ejercicios de nuestra aplicación).*
    
    Con los datos anteriores se realizarán diversos cálculos como medias, desviaciones, varianzas, comparaciones estadísticas en general, con el objetivo de decidir los ejercicios finales de la sesión. También hay que tener en cuenta que hay que establecer algoritmos de decisión sobre la planificación: valorar que jugadores lesionados no pueden participar en las rutinas, o que un mismo jugador no debería participar en subgrupos con una dificultad/carga de ejercicio excesiva, y por supuesto, *debería haber un equilibrio en el orden de cómo estos se realizan*.
    
    Esta es la lógica de negocio que hay detrás. De lo único que se tiene que encargar el entrenador es de recibir la decisión de la aplicación, y posteriormente otorgar calificación a los jugadores para comprobar su evolución.
    
    

* [x] ***¿Se ha incluído la configuración del repositorio y se ha enlazado desde el `README`?***

    Sí, para ello acuda al apartado de este readme: *Secciones de Interés*.



****

### Secciones de interés

Para más información adicional referente al repositorio, puede consultar los siguientes enlaces:

* [Configuración del repositorio GIT](repo-res/objetivo0-gitconfig.md)
* [Estructura del repositorio GIT](repo-res/objetivo0-gitstructure.md)