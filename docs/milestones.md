# Hitos de Proyecto (Milestones)



### Infraestructura Virtual (2022/23)

****

*Autor: danielsp13 (Daniel Pérez Ruiz)*. En este documento se especifican los hitos a conseguir durante el transcurso del proyecto.

****

### :checkered_flag: [M0] Representación inicial del modelo. Definición de entidades a través de clases

Se deben definir clases que modelen adecuadamente a las entidades de: usuarios, examen propuesto (incluyendo sus preguntas y respuestas), y las relaciones entre todos ellos.

*Historias de Usuario identificadas con este milestone:*

* *[HU01]: Dolores quiere agilizar la tarea de corrección de exámenes*.

****

### :checkered_flag: [M1] Implementación de algoritmos y estructuras de Procesamiento del Lenguaje Natural (Lógica de Negocio)

Se debe definir un módulo en el que se implementen algoritmos que permitan procesar los textos de las respuestas, obteniendo estructuras que puedan ser utilizadas para la posterior implementación del algoritmo de corrección.

****

### :checkered_flag: [M2] Implementación de algoritmo de corrección automática de exámenes (Lógica de negocio)

Se debe definir un módulo en el que se implemente el algoritmo de comparación entre la respuesta correcta y la otorgada por el alumno. Se utilizará para la corrección del examen planteado y se otorgará una calificación a cada pregunta del mismo.

****

### :checkered_flag: [M3] Habilitar análisis de resultados e informes (Lógica de negocio)

Se debe recolectar debidamente toda la información asociada a los exámenes planteados por el profesor y generar informe general con el resultado colectivo. Información a considerar: calificaciones, preguntas mejor contestadas, preguntas peor contestadas. 

Se requiere previamente haber implementado el módulo de corrección automática de exámenes.

*Historias de Usuario identificadas con este milestone:*

* *[HU02] Carolina quiere evaluar el rendimiento de sus alumnos*.
