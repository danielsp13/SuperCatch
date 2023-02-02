# Lógica de Negocio

En este documento se especifican todas las fases del proyecto en cuanto a lógica de negocio: qué fases tiene el proyecto, qué funcionalidades se han implementado, y cómo se ha validado el código escrito.

Las fases del proyecto se pueden consultar en el documento [Milestones](milestones.md). Aquí se nombrarán simplemente para aclarar lo que se ha hecho.

### [M0] : Representación inicial del modelo

Este objetivo no corresponde realmente a la lógica de negocio, pero es la base que sirve para crear todo lo demás.

El problema principal, planteado en uno de los issues en el repositorio, es cómo almacenar las respuestas de los alumnos a las preguntas de los exámenes, así como la respuesta que se considera la correcta, para poder posteriormente comparar ambas aplicando el algoritmo de comparación.

Para ello, se ha creado un *objeto valor* denominado `Respuesta`, que simplemente, contiene el texto de la respuesta considerada.

A continuación, otras de las cuestiones está en cómo agrupar estas respuestas y cómo almacenar las calificaciones que tienen cada una de ellas. Para ello, se ha creado una entidad, denominada `Examen`, que contiene las respuestas del alumno y las calificaciones obtenidas tras haber corregido el mismo.

Finalmente, hay un matiz importante a considerar, y es que la idea general para la automatización de la tarea de correción de exámenes es comparar un modelo con un examen respondido por un alumno, es por ello por lo que también se define un objeto denominado `Modelo`, que represente el conjunto de respuestas correctas propuestas por el profesor.

### [M1] : Implementación de algoritmos y estructuras de Procesamiento del Lenguaje Natural (PLN)

Este primer hito ya sí corresponde con lo que sería la lógica de negocio del proyecto. En un principio, no estaba considerado, pero tras realizar un análisis en lo que se quiere implementar, surgió un problema que da sentido a este objetivo: ***el procesamiento del texto de las respuestas escritas en lenguaje natural***.

Para solucionar este problema, se ha decidido crear un *módulo* denominado `pln` (nombre debido a "Procesamiento del Lenguaje Natural"), que contiene dos funciones que permiten realizar las fases que se mencionarán después.

Lo que da valor a este módulo es que conseguimos reducir una posible respuesta que contenga cientos de palabras en un conjunto de ellas que tengan cierta relevancia, por lo que el proceso de corrección de exámenes se realizará más rápido, y por supuesto, de forma más efectiva.

Las fases consideradas en el procesamiento de las respuestas son:

1. **Realizar análisis léxico sobre el texto:** El primer paso consiste en tener una estructura de datos que sea más manejable, y para ello se realiza un análisis léxico tal que:
   1. Se eliminan los tokens que no contienen caracteres. En el lenguaje humano utilizamos símbolos de puntuación que ayudan a la estructuración del discurso y a la lectura: puntos, comas, interrogaciones, exclamaciones. Nosotros sí las necesitamos, pero las máquinas no. Es por ello que debe eliminarse del texto de la respuesta todos los símbolos, para no tener ningún carácter que no sea alfanumérico.
   2. Se eliminan las mayúsculas. En el ámbito de la programación, las distinción entre mayúsculas y minúsculas ha supuesto un problema desde prácticamente el comienzo. Es por ello, que se decide pasar todos los caracteres mayúsculas a minúsculas.
   3. Se eliminan los acentos. Esto se conoce como *normalización*, y consiste en cambiar entre otras cosas, las vocales que tengan acentos (como à, á, è, é, ...). Esta cuestión es importante considearla en fases posteriores, concretamente en la comparación, ya que es probable que tener en cuenta los acentos pueda ser un factor que penalice demasiado (aunque lo ideal sería que el alumno escribiera adecuadamente y sin faltas ortográficas).
2. **Eliminar palabras vacías (stopwords):** Las palabras vacías son aquellas que se encuentran con bastante frecuencia en un texto, pero que tienen poca semántica (como por ejemplo artículos, determinantes, preposiciones, etc.). Es por ello que para el análisis, no será necesario contar con estas palabras, por lo que se deben eliminar de la lista de tokens.

El módulo `pnl` dispone de dos funciones que atienden a las dos tareas anteriormente descritas, y se considearán funciones válidas si se verifican los siguientes supuestos:

* *Comprobar que la lista de tokens no es vacía.* Esto quiere decir que el texto debe contener palabras. En caso contrario, debe lanzarse una **excepción** indicándolo.
* *Comprobar que la lista de tokens no contiene tokens nulos*. Esto quiere decir que no debe contener tokens cuya secuencia de caracteres tenga longitud 0.
* *Comprobar que la lista de tokens no es vacía*. Esto quiere decir que el texto debe tener contenido. En caso contrario, se debe lanzar una **excepción** indicándolo.
* *Comprobar que la lista no contenga tokens con letras mayúsculas*.
* *Comprobar que ningún token tenga una vocal con acentos.*
* *Comprobar que la lista no contenga ninguna palabra vacía.*
  * *Comprobar que la lista no es vacía*. En caso contrario, sólo se habrán escrito palabras vacías, por lo que debe lanzarse una **excepción** indicándolo.

### [M2] : Implementación de algoritmo de corrección automática de exámenes (Lógica de Negocio)

El siguiente hito tras haber conseguido la reducción del texto de las respuestas, es definir el algoritmo de corrección de exámenes que permitirá uno de los objetivos fundamentales en base a las historias de usuario consideradas: *corrección automática de exámenes*. 

Para cubrir este milestone se utilizará el algoritmo de similitud del coseno, que es totalmente aplicable a este problema. Consiste en medir cómo de parecidos son dos vectores, dependiendo de la amplitud del ángulo que forman. Cuanto menor sea el ángulo formado, mayor será la semejanza entre los dos vectores. Puedes consultar más información al respecto en [Similitud del Coseno](https://hmong.es/wiki/Cosine_similarity).

El resultado de este algoritmo (normalizado) produce valores de entre 0 y 1, por lo que se transformarán los valores de este intervalo a un rango que sea más usual cuando se trata de otorgar calificaciones (consideraré de 0 a 10, redondeando a dos cifras decimales).

Sin embargo, este algoritmo sólo se puede aplicar a vectores numéricos, y hasta ahora, lo único próximo a un vector es la lista de tokens de una respuesta. Es por ello por lo que será necesario definir algún mecanismo que permita traducir estos tokens en números.

Hay que tener en cuenta que siempre se está comparando una respuesta modelo (escrita por el profesor, y la teóricamente correcta), con la del alumno, y **esta será la base para todo lo explicado anteriormente**. En definitiva, para resolver este asunto se ha definido un módulo llamado `corrector`, que dispone de una serie de funciones que permiten hacer las siguientes tareas:

1. **Ponderar los términos en función de las respuestas**: Un término es un token que corresponde a alguna de las dos respuestas a comparar. La idea es disponer todos los términos obtenidos a través de los tokens de sendas respuestas en una lista, y a continuación se establece un criterio para definir dos vectores numéricos. Esto se conoce como *ponderar*, y hay varias formas de hacerlo. La que se ha considerado de forma inicial (y actual), es la ponderación binaria, que especifica la presencia (con un 1) o ausencia (con un 0) de un término en una respuesta.

   El resultado de realizar esta tarea es la obtención de dos vectores que representen la aparición de los términos en cada respuesta respectivamente.

2. **Calificar una respuesta**: Llegó el momento importante. Dadas dos respuestas, y tras obtener la ponderación con el criterio fijado, se aplica el algoritmo del coseno que permitirá obtener una calificación de 0 a 10 en función de la similitud de los vectores de ponderación.

Para testear estas funciones, se han definido dos objetos: uno es el *Modelo* de respuestas correctas proporcionado por el profesor, y otro *Examen*, con las respuestas del alumno en cuestión.

Supongamos que el escenario real es el siguiente:

* *Pregunta 1: ¿Cuál es el apodo y nombre del escritor español de apellido "Alas"? ¿Qué importante libro escribió?*

  * *Respuesta modelo:* 'Clarín', es el apodo de Leopoldo Alas y escribió 'La Regenta'.

  * *Respuesta alumno:* "  La  RegenTa la escRibio leoPoLdó alas    y su   apodo fue Clarin.  "

    

  * **Calificación esperada: 10**. La respuesta responde a lo que se pide, y en cuanto a las palabras más relevantes, están todas (en términos del algoritmo, cos(VA;VB) = 1, un ángulo de 0º). No debe importar la forma de redacción en cuanto a mayúsculas y minúsculas, espacios, y acentos incorrectos en vocales (de ahí la importancia de eliminarlos en el anterior objetivo). El orden de la expresión utilizada por el alumno para responder a la pregunta tampoco es importante, sólo el contenido.

    

* *Pregunta 2: ¿Cuál es el nombre de una de las leyes más importantes de la corona de españa en 1713 que supuso un cambio en la forma de reinar? ¿Quién la hizo y en qué consistía?* 

  * *Respuesta modelo:* La 'ley sálica' la redactó Felipe V y permitió acceder al trono a las mujeres.

  * *Respuesta alumno:* Felipe IV redacto la ley salica y sirve para el acceso al trono a las mujeres.

    

  * **Calificación esperada: entre 6 y 8.** La respuesta se parece, pero el alumno no ha determinado correctamente el rey que escribió la ley. Se espera una calificación cercana a la mitad del intervalo, pero no una que implique el suspenso de esta respuesta, ni tampoco la excelencia.

  

* *Pregunta 3: ¿De qué partículas está constituda la materia? ¿De qué están formadas?*

  * *Respuesta modelo:* La matería está constituida por átomos que están formados por protones, electrones y neutrones.

  * *Respuesta alumno*: La materia está constituida por moléculas que sólo tienen protones.

    

  * **Calificación esperada: menor que 5.** La respuesta no contiene algunas de las palabras que se esperan en el modelo, como son "átomos, electrones y neutrones", por lo que no se puede considerar aprobar esta respuesta.



* *Pregunta 4: ¿A qué temperatura funde el acero?*

  * *Respuesta modelo:*  El acero se funde a 1250 grados.

  * *Respuesta alumno:* Respuesta que no tiene nada que ver con lo que se pide.

    

  * **Calificación esperada: 0.** La respuesta no tiene nada que ver con la que se supone correcta (en términos del algoritmo, cos(VA,VB) = 0, un ángulo de 90º). 
