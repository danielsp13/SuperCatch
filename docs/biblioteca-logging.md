# Biblioteca de registros (logging)

En este documento se especifican los criterios para la elección de una biblioteca de logging para el registro de actividades en la aplicación.

****

### :page_with_curl: Criterios para elección de biblioteca de logging:

Para obtener los criterios se han tenido en cuenta algunas buenas prácticas como las que hay en los siguientes enlaces:

* **[9 best practice for application logging that you must know.](https://www.atatus.com/blog/9-best-practice-for-application-logging-that-you-must-know/#Have-a-Consistent-Structure-Across-All-Logs)**
* **[What Is Structured Logging and Why Developers Need It](https://stackify.com/what-is-structured-logging-and-why-developers-need-it/)**

La herramienta considerada por tanto, debe cumplir los siguientes criterios:

1. ***Herramienta activa***. Debe considerarse una herramienta que tenga actualizaciones con relativa frecuencia y un soporte continuado y activo.
2. ***Ausencia de problemas de seguridad.*** La herramienta no debe tener brechas de seguridad que puedan comprometer a la aplicación.
3. ***Realizar registro de niveles estructurado.*** El objetivo es poder almacenar (por ejemplo utilizando diccionarios) y posteriormente recuperar la información del registro de una forma más sencilla. Además debe poder configurarse de forma que se pueda incluir diversos campos como *Nivel*, *Fecha y Hora*, *Mensaje*, y eventualmente otras cuestiones como asignar un identificador.
4. ***Elección en el formato de salida de los logs.*** Lo ideal es disponer de una herramienta versátil que nos permita elegir entre mostrar el registro por pantalla o en ficheros.
5. ***Popularidad.*** Se considerará una herramienta que tenga influencia en otros proyectos de Python, además de otras recomendaciones.

Se utilizará además la herramienta [Snyk.io Advisor](https://snyk.io/advisor/python) para algunos de los criterios como (1), (2) y (5).

****

### :dart: Candidatos considerados

Las bibliotecas de aserciones consideradas atendiendo a los criterios citados son:

A1. **[logging](https://docs.python.org/3/library/logging.html)** : (Biblioteca incluida en el lenguaje)
* (1) Herramienta activa: :heavy_check_mark: . 
* (2) Ausencia de problemas de seguridad: :heavy_check_mark:
* (3) Realizar registro de niveles estructurado: :warning: Se puede hacer, pero requiere definirlo explícitamente. [logging: implementing structured logging](https://docs.python.org/2/howto/logging-cookbook.html#implementing-structured-logging).
* (4) Elección de formato de salida de los logs: :heavy_check_mark: [Logging cookbook: logging to multiple destinations](https://docs.python.org/3/howto/logging-cookbook.html#logging-to-multiple-destinations)
* (5) Popularidad: :heavy_check_mark: 

A2. **[loguru](https://github.com/Delgan/loguru)** : [Puntuación en [Snyk - Loguru](https://snyk.io/advisor/python/loguru) : 80]
* (1) Herramienta activa: :warning: Última versión 0.6.0  (29-01-2022). Aunque tiene actividad reciente en su repositorio.
* (2) Ausencia de problemas de seguridad: :heavy_check_mark: 
* (3) Realizar registro de niveles estructurado: :heavy_check_mark:. [loguru: structured logging as needed](https://github.com/Delgan/loguru#structured-logging-as-needed)
* (4) Elección de formato de salida de los logs: :heavy_check_mark: [loguru: ready to use out the box without boilerplate](https://github.com/Delgan/loguru#ready-to-use-out-of-the-box-without-boilerplate), [loguru: easier file logging](https://github.com/Delgan/loguru#easier-file-logging-with-rotation--retention--compression) 
* (5) Popularidad: :heavy_check_mark:

A3. **[structlog](https://www.structlog.org/en/22.3.0/)** : [Puntuación en [Snyk - structlog](https://snyk.io/advisor/python/structlog) : 91]
* (1) Herramienta activa: Última versión 22.3.0 (24-11-2022) :heavy_check_mark: . 
* (2) Seguridad: :heavy_check_mark:.
* (3) Realizar registro de niveles estructurado: :heavy_check_mark: [struct log: Manipulating Log Entries in Flight](https://www.structlog.org/en/22.3.0/getting-started.html#manipulating-log-entries-in-flight)
* (4) Elección de formato de salida de los logs: :heavy_check_mark: [struct log: Output](https://www.structlog.org/en/22.3.0/bound-loggers.html#output)
* (5) Popularidad: :heavy_check_mark:

****

### :bulb: Elección

Tanto `loguru` como `structlog` son mejores elecciones que considerar la biblioteca que viene con Python. `structlog` es una herramienta muy bien valorada, con múltiples opciones y configuraciones, mientras que `loguru` a pesar de tener su última versión lanzada hace un año (teniendo en cuenta que se siguen realizando contribuciones y que hay soporte), también permite realizar las mismas configuraciones que la otra biblioteca, añadiendo un factor extra que es la sencillez en la forma de utilizarlo, como indica en el readme del repositorio.

Es por esta cuestión que se decide tomar **loguru** como biblioteca de registros.
