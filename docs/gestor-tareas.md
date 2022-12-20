# Gestor de tareas

En este documento se especifican los criterios para la elección de un gestor de tareas, 

****

### :page_with_curl: Criterios para elección de gestor de dependencias:

Cualquier herramienta que considere como potencial para usarla en el proyecto, debe cumplimentar sí o sí:

1. ***Herramienta activa.*** Para no aumentar la deuda técnica, se debe considerar una herramienta que tenga un mantenimiento activo con lanzamiento de actualizaciones más o menos frecuente y con soporte.

****

### :dart: Candidatos considerados

Los gestores de tareas considerados atendiendo a los criterios citados son:

A1. **[poethepoet](https://github.com/nat-n/poethepoet)** : última versión v0.16.5 (Noviembre 2022). :heavy_check_mark:

A2. **[pypyr](https://pypyr.io/)** : última versión v5.7.1 (Octubre 2022). :heavy_check_mark:

A3. **[invoke](https://www.pyinvoke.org/)** : última versión v1.7.3 (Septiembre 2022). Se espera un lanzamiento de una nueva versión próximamente. :heavy_check_mark:



****

### :star: Características adicionales para elección

El criterio de que sea una herramienta activa, no es suficiente para la elección de un gestor frente a otro, por lo que se valorará a continuación las características más significativas de cada uno:

* ***poethepoet***:
  * :warning: Utiliza el fichero `pyproject.toml` para la definición de tareas. (Ventajas: Sencillez, Reducción del uso de ficheros). [poethepoet readme](https://github.com/nat-n/poethepoet/blob/main/README.rst)
  * :warning: Utiliza un ejecutor específico para tareas dentro del entorno manejado por poetry. [poethepoet executor type](https://github.com/nat-n/poethepoet#change-the-executor-type).
  * :warning: Es una herramienta bastante popular.

* ***pypyr***:
  * :warning:  Utiliza un fichero de extensión `.yaml` para definir las tareas. (Ventajas: Sencillez, Fácil comprensión) [pypyr 1st pipeline](https://pypyr.io/docs/getting-started/run-your-first-pipeline/#write-your-first-pipeline)
  * :warning: No es tan popular como las otras herramientas.
* ***invoke:***
  * :warning: Inspirado en `make`. (Ventajas: Fácil adaptación y aprendizaje si se ha trabajado con make anteriormente.)
  * :warning: Utiliza un fichero script de python `tasks.py`. (Ventajas: invocación de múltiples tareas en una única llamada) [What is invoke](https://www.pyinvoke.org/#what-is-invoke).
  * :warning: Es una herramienta muy popular. Además, es de los más utilizados actualmente.

****

### :bulb: Elección

**poethepoet** es el gestor de tareas que utilizaré para mi proyecto. De las tres propuestas, es la que ha recibido una última actualización más frecuente, además de que el hecho de que aproveche el fichero `pyproject.toml` para definir también las tareas, e incluso que disponga de opciones específicas para poetry, hace que sea idóneo para el proyecto.
