# Dependencias del proyecto

En este documento se especifican las bibliotecas externas utilizadas para el desarrollo del proyecto, necesarias para implementar algunas funcionalidades de la lógica de negocio.

Todas las dependencias del proyecto, tal y como se indica en el README, se instalan con la orden:

~~~bash
$ poe install
~~~

Una vez se ha realizado esta instalación, será necesario instalar los datos de una de las bibliotecas de las que depende el proyecto, `NLTK`, de la que se habla a continuación. Para ello, hay que usar la orden:

~~~bash
$ poe nltk_data
~~~

Esta orden descarga en el directorio HOME del usuario los datos necesarios para algunas de las fases de la lógica de negocio (concretamente, la tokenización y eliminación de stopwords).

****

A continuación, se enumeran las bibliotecas utilizadas:

### :books: **[NLTK : Natural Languaje Toolkit](https://www.nltk.org/)**

Esta biblioteca proporciona funcionalidades y datos para trabajar con el lenguaje natural. En lo que concierne al proyecto, (explicado en detalle en [Lógica de Negocio](logica-negocio.md)) , sirve de ayuda para procesar las respuestas a las preguntas de los exámenes, escritas en castellano.

Se ha utilizado en:

* La fase de *tokenización del texto*, que consiste en realizar una división del texto en diversos tokens (secuencia de caracteres con significado colectivo).
* La fase de *eliminación de palabras vacías*, que consiste en eliminar aquellas palabras que tienen poca semántica y se repiten con elevada frecuencia (artículos, determinantes, preposiciones,...).
* La fase de *segmentación de los tokens*, que consiste en reducir el vocabulario, reduciendo las palabras a una única forma común.

**:bulb: Justificación de la elección:**

Hay otras alternativas que también podrían haber servido para este problema, pero se ha decidido trabajar con esta herramienta por los siguientes motivos:

1. He consultado documentos de proyectos que hablan (o tienen relación) sobre el problema del procesamiento de texto escrito en lenguaje natural , como es el caso de [Análisis automático de textos en español utilizando NLTK](https://riull.ull.es/xmlui/bitstream/handle/915/3082/Analisis%20automatico%20de%20textos%20en%20espanol%20utilizando%20NLTK.pdf?sequence=1&isAllowed=y) : secciones 1.4 y 1.5 del documento.

2. He consultado a personas que han estudiado estos temas y además de aportarme documentación de interés, me han hablado de diversas herramientas, entre ellas, esta para el lenguaje que se está considerando para el proyecto.

### :books: **[Unidecode](https://pypi.org/project/Unidecode/)**

Esta biblioteca permite normalizar el texto, que consiste en eliminar todo tipo de acentos en las palabras de las respuestas del texto, con el objetivo de hacer que la obtención de tokens sea más eficiente.

**:bulb: Justificación de la elección:**

Se ha recurrido a utilizar esta biblioteca mediante el desarrollo de la fase de segmentación (explicado en detalle en [Lógica de Negocio](logica-negocio.md)) , fase en la que testeando el código, se ha detectado el problema de mantener acentos en las palabras.
