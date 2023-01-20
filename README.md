# SuperCatch



### Infraestructura Virtual (2022/23)

****

*Autor: danielsp13 (Daniel Pérez Ruiz)*. Repositorio para el proyecto de la asignatura Infraestructura Virtual del Grado de Ingeniería Informática de la Universidad de Granada.

****

###  :question: Problema a resolver

En la ESO / Bachillerato, se realizan muchos exámenes para comprobar que el alumnado entiende los contenidos que se imparten en las asignaturas. Sin embargo, no todas ellas se pueden realizar en un formato tipo test con opciones, si no que se requiere respuestas complejas en lenguaje natural, como puede ser el caso de Historia. El problema reside en que la corrección de dichos exámenes es una tarea en la que se tarda mucho tiempo, ya que no es una tarea puramente objetiva, lo que impide que el profesor se pueda dedicar a otras tareas, o que realice controles / tareas de seguimiento de la clase de forma más periódica para poder ayudar a sus alumnos en su fase de aprendizaje.

###  :bulb:  Solución propuesta

Se propone una solución en forma de plataforma residente en la nube con el objetivo de:

1. Automatizar la tarea de corrección de exámenes / controles que requieren respuestas en lenguaje natural.
2. Deducir el rendimiento general de la clase a través de los resultados de dichos controles.

****

### :page_with_curl: Documentación del Proyecto

Todo lo que se necesita saber acerca del proyecto se encuentra en las siguientes secciones:

* :thinking: [Design Thinking](docs/design-thinking.md) : Especifica el proceso de design-thinking que he seguido para modelar el problema y encontrar la solución.
* :spiral_notepad: [Modelo](docs/modelo.md) : Conceptualización extendida del modelo de solución.



* :busts_in_silhouette: [Usuarios](docs/users.md) : Se especifican los tipos de usuarios que utilizarán nuestra solución.
* :notebook: [Historias de Usuario](docs/user-stories.md) : Se especifican las historias de usuario, útiles para especificar adecuadamente las fases del proyecto y el desarrollo de la solución.
* :checkered_flag: [Milestones](docs/milestones.md) : Se especifican los hitos a conseguir durante el desarrollo del proyecto.
* :gear: [Gestor dependencias](docs/gestor-dependencias.md) : Se especifican los criterios establecidos para la elección del gestor de tareas. **poetry**.
* :runner: [Gestor tareas](docs/gestor-tareas.md) : Se especifican los criterios establecidos para la elección del gestor de tareas. **poethepoet**.

****

### :shell: Órdenes de instalación y verificación

Para instalar el gestor de dependencias y de tareas, en un ámbito global al usuario:

~~~bash
$ pip install -r requirements.txt
~~~



Para instalar las dependencias del proyecto:

~~~bash
$ poe install
~~~

*Se creará un entorno virtual para la instalación de las dependencias utilizadas de forma aislada.*



Para comprobar la sintaxis de las fuentes:

~~~bash
$ poe check
~~~



****

###  Secciones de interés

Para más información adicional referente al repositorio, puede consultar los siguientes enlaces:

* [Configuración del repositorio GIT](repo-res/gitconfig.md)
* [Estructura del repositorio GIT](repo-res/gitstructure.md)