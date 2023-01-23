# Lógica de Negocio

En este documento se especifican todas las fases del proyecto en cuanto a lógica de negocio: qué fases tiene el proyecto, qué funcionalidades se han implementado, y cómo se ha validado el código escrito.

Las fases del proyecto se pueden consultar en el documento [Milestones](milestones.md). Aquí se nombrarán simplemente para aclarar lo que se ha hecho.

### [M0] : Representación inicial del modelo

Este objetivo no corresponde realmente a la lógica de negocio, pero es la base que sirve para crear todo lo demás.

El problema principal, planteado en uno de los issues en el repositorio, es cómo almacenar las respuestas de los alumnos a las preguntas de los exámenes, así como la respuesta que se considera la correcta, para poder posteriormente comparar ambas aplicando el algoritmo de comparación.

Para ello, se ha creado un *objeto valor* denominado `Respuesta`, que simplemente, contiene el texto de la respuesta considerada.

