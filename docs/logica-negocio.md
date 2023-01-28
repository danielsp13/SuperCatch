# Lógica de Negocio

En este documento se especifican todas las fases del proyecto en cuanto a lógica de negocio: qué fases tiene el proyecto, qué funcionalidades se han implementado, y cómo se ha validado el código escrito.

Las fases del proyecto se pueden consultar en el documento [Milestones](milestones.md). Aquí se nombrarán simplemente para aclarar lo que se ha hecho.

### [M0] : Representación inicial del modelo

Este objetivo no corresponde realmente a la lógica de negocio, pero es la base que sirve para crear todo lo demás.

El problema principal, planteado en uno de los issues en el repositorio, es cómo almacenar las respuestas de los alumnos a las preguntas de los exámenes, así como la respuesta que se considera la correcta, para poder posteriormente comparar ambas aplicando el algoritmo de comparación.

Para ello, se ha creado un *objeto valor* denominado `Respuesta`, que simplemente, contiene el texto de la respuesta considerada.

### [M1] : Implementación de algoritmos y estructuras de Procesamiento del Lenguaje Natural (PLN)

Este primer hito ya sí corresponde con lo que sería la lógica de negocio del proyecto. En un principio, no estaba considerado, pero tras realizar un análisis en lo que se quiere implementar, surgió un problema que da sentido a este objetivo: ***el procesamiento del texto de las respuestas escritas en lenguaje natural***. Esta cuestión, no es trivial de resolver y suele tener unas dimensiones generalmente grandes en otros ámbitos. 

Para solucionar este problema, se ha decidido crear una *entidad* denominada `TokensRespuesta`, que realice el procesamiento de las respuestas y obtenga una estructura (una lista) que pueda ser utilizada por el algoritmo de similitud del coseno, que será el utilizado a posteriori para realizar la comparación.

Las fases consideradas en el procesamiento de las respuestas son:

1. **Realizar análisis léxico sobre el texto:** El primer paso consiste en tener una estructura de datos que sea más manejable, y para ello se realiza un análisis léxico sobre la respuesta en la que:
   1. Se obtienen los tokens del texto.  Un token es un conjunto de caracteres con significado colectivo. La idea es dividir el texto en pequeñas secuencias de caracteres (palabras) y almacenarlas en una lista, de manera que así podamos trabajar más cómodamente.
   2. Se eliminan los tokens que no contienen caracteres. En el lenguaje humano utilizamos símbolos de puntuación que ayudan a la estructuración del discurso y a la lectura: puntos, comas, interrogaciones, exclamaciones. Nosotros sí las necesitamos, pero las máquinas no. Es por ello que debe eliminarse de la lista de tokens anteriormente obtenida.
   3. Se eliminan las mayúsculas. En el ámbito de la programación, las distinción entre mayúsculas y minúsculas ha supuesto un problema desde prácticamente el comienzo. Es por ello, que se decide pasar todos los caracteres mayúsculas a minúsculas.
   4. Se eliminan los acentos. Esto se conoce como *normalización*, y consiste en cambiar entre otras cosas, las vocales que tengan acentos (como à, á, è, é, ...).
2. **Eliminar palabras vacías (stopwords):** Las palabras vacías son aquellas que se encuentran con bastante frecuencia en un texto, pero que tienen poca semántica (como por ejemplo artículos, determinantes, preposiciones, etc.). Es por ello que para el análisis, no será necesario contar con estas palabras, por lo que se deben eliminar de la lista de tokens.

Todavía hay otras fases que deben atenderse, pero se han dejado para otro objetivo más avanzado del proyecto, cuando se esté cerca de realizar la comparación.

La entidad `TokensRespuesta` realiza todas esas fases descritas, realizando diversas funcionalidades que han sido validadas mediante la realización de tests. Aquí se nombran y se especifican qué tests se han realizado para su verificación:

* `eliminarSimbolos()` : elimina todos los símbolos que no son caracteres de los tokens. Para probar esta funcionalidad, se han realizado los siguientes tests:
  * *Comprobar que la lista de tokens no es vacía.* Esto quiere decir que el texto debe contener palabras. En caso contrario, debe lanzarse una **excepción** indicándolo.
* `eliminarTokensNulos()`: se eliminan todos aquellos tokens que no contienen ningún tipo de caracter: ya sean letras o números. Para probar esta funcionalidad, se han realizado los siguientes tests:
  * *Comprobar que la lista de tokens no contiene tokens nulos*. Esto quiere decir que no debe contener tokens cuya secuencia de caracteres tenga longitud 0.
  * *Comprobar que la lista de tokens no es vacía*. Esto quiere decir que el texto debe tener contenido. En caso contrario, se debe lanzar una **excepción** indicándolo.
* `eliminarMinusculas()` : convierte todos los caracteres mayúsculas a minúsculas. Para probar esta funcionalidad, se han realizado los siguientes tests:
  * *Comprobar que la lista no contenga tokens con letras mayúsculas*.
* `eliminarAcentos()` : elimina los acentos de las vocales de los tokens. Para probar esta funcionalidad, se han realizado los siguientes tests:
  * *Comprobar que ningún token tenga una vocal con acentos.*
* `eliminarStopwords()`: elimina todas las palabras vacías de la lista de tokens. Para probar esta funcionalidad, se han realizado los siguientes tests:
  * *Comprobar que la lista no contenga ninguna palabra vacía.*
  * *Comprobar que la lista no es vacía*. En caso contrario, sólo se habrán escrito palabras vacías, por lo que debe lanzarse una **excepción** indicándolo.
