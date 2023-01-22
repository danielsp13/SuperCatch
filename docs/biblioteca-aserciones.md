# Biblioteca de aserciones

En este documento se especifican los criterios para la elección de una biblioteca de aserciones para la escritura de los tests.

****

### :page_with_curl: Criterios para elección de biblioteca de aserciones:

Cualquier herramienta que considere como potencial para usarla en el proyecto, debe cumplimentar:

1. ***Herramienta activa***. Debe considerarse una herramienta que tenga actualizaciones con relativa frecuencia y un soporte continuado y activo.

****

### :star: Otros criterios o características adicionales para elección

Los tres gestores de dependencias especificados, son totalmente válidos para su uso en el proyecto, no obstante, se tendrán en consideración algunas cuestiones ya de caracter secundario y/o subjetivo, como:

* :warning: ***Popularidad***: A través de artículos y otros lugares de la comunidad, se estudiará qué opinión y valoración dan las personas que utilizan dichas herramientas. Se tendrá en cuenta las recomendaciones oportunas.
* :warning: ***Sencillez de uso***. Si dos bibliotecas pueden ser potencialmente candidatas a su elección, se considerará aquella que permita trabajar con mayor comodidad, en cuestiones por ejemplo como una sintaxis sencilla. No obstante, nunca será una prioridad si hay una herramienta que pueda ofrecer mejores prestaciones.

****

### :dart: Candidatos considerados

Las bibliotecas de aserciones consideradas atendiendo a los criterios citados son:

A1. **[unittest](https://docs.python.org/3/library/unittest.html)** : 
* (1) Herramienta activa: :heavy_check_mark: . 
* (2) Información acerca de la herramienta: :heavy_check_mark: 
  * Biblioteca nativa del lenguaje python.
  * Entre las diferentes funciones de aserción que tiene, se encuentra la de aserciones para excepciones. [unittest : assertRaises](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises)
  * De forma adicional, dispone de clases que permiten crear tests, además de ejecutarlos de forma independiente sin utilización de runner.
* (op1) Popularidad de la herramienta: :heavy_check_mark: 
  * Al ser una herramienta nativa, suele ser recomendada por bastantes usuarios, debido a que no requiere instalación de otras herramientas de terceros.

A2. **[PyHamcrest](https://github.com/hamcrest/PyHamcrest)** : 
* (1) Herramienta activa: Último  (27-07-2022) :heavy_check_mark: . 
  * (En su github, tiene contribuciones recientes, a pesar de haber lanzado la última versión registrada hace más de medio año.)
* (2) Información acerca de la herramienta:
  * Dispone de múltiples funciones de aserción, entre ellas, referida a excepciones. [PyHamcrest : matchers](https://github.com/hamcrest/PyHamcrest#predefined-matchers)
  * La escritura de los tests se realiza de forma más entendible posible para su lectura, como por ejemplo comentan en [PyHamcrest : Syntactic Sugar](https://github.com/hamcrest/PyHamcrest#syntactic-sugar)
* (op1) Popularidad de la herramienta: :heavy_check_mark: 
  * Es de las herramientas más populares entre la comunidad, además de ser influyente en gran cantidad de proyectos.
  * No se han detectado problemas, bugs o fallos de seguridad recientes que rechacen su uso.

A3. **[Hypothesis](https://hypothesis.readthedocs.io/en/latest/)** : 
* (1) Herramienta activa: Último  (14-01-2023) :heavy_check_mark: . 
  * (En su github [HypothesisWorks/hypothesis_pyhton](https://github.com/HypothesisWorks/hypothesis/tree/master/hypothesis-python), tiene contribuciones recientes, además, de haber sacado una última versión en este nuevo año)
* (2) Información acerca de la herramienta:
  * Permite la creación de tests unitarios de forma más simple que otras bibliotecas.
  * Además, permite escribir tests bajo el paradigma de testeo basado en propiedades.
  * Trabaja con datos/estructuras generados mediante estrategias.
  * La ejecución de los tests escritos se pueden realizar explícitamente por nosotros mismos, pero funciona muy bien con tests runners (como el elegido, `pytest`). [Hypothesis : Running tests](https://hypothesis.readthedocs.io/en/latest/quickstart.html#running-tests)
* (op1) Popularidad de la herramienta: :heavy_check_mark: 
  * Está muy bien valorada entre los usuarios. También, se considera una herramienta influyente en gran cantidad de proyectos.
  * No se han detectado problemas, bugs o fallos de seguridad recientes que rechacen su uso.

****

### :bulb: Elección

Considero que las herramientas que pueden ser útiles para el proyecto son `PyHamcrest` e `Hypothesis`. 

`PyHamcrest` tiene una sintaxis y una forma de uso que personalmente, creo que es mejor sobre `Hypothesis`. El problema es que el ritmo de contribuciones (que al menos signifiquen algo) en el repositorio de desarrollo de herramienta, no es particularmente alto, y puede suponer un problema si esta tendencia conduce a un abandono de la herramienta.

`Hypothesis` tiene una presencia importante en el mundo Python, se combina bien con `pytest` como aseguran los propios desarrolladores, y la última versión es de este año 2023. La sintaxis no es tan complicada de comprender, aunque no es una prioridad para esta herramienta el que sea entendible por las personas (aunque en cualquier test escrito con cualquier heramienta que se elija es evidente que habrá que explicar en qué consiste y qué prueba). Habrá que utilizar comentarios descriptivos de lo que se está haciendo.



**PyHamcrest**  es la biblioteca de aserciones elegida. En un principio, se había decidido trabajar con *Hypothesis*, ya que tiene actualizaciones más recientes y trabaja bien con el test runner pytest. El motivo del cambio de elección reside en que en la práctica se está haciendo un uso nulo de la biblioteca, ya que uno de sus puntos más fuertes, la generación de datos para las pruebas, no se puede usar para el proyecto, pues en este caso se necesita definir textos en español, y esta cuestión no es capaz de hacerla. Además, tampoco dispone de funcionalidades de testeo de excepciones.
