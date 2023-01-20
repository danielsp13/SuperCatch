# Gestor de depencias

En este documento se especifican los criterios para la elección de un gestor de dependencias, herramienta que permitirá automatizar instalación y configuración de dependencias, especificando además las versiones exactas de las mismas.

****

### :page_with_curl: Criterios para elección de gestor de dependencias:

Se han determinado tres bloques con los criterios que deben seguirse. Cualquier herramienta que considere como potencial para usarla en el proyecto, debe cumplimentar sí o sí:

1. ***Seguir el estándar*** para lenguaje Python.
   1.1 En [PEP518](https://peps.python.org/pep-0518/#file-format), se define el formato estándar del fichero en el que tienen que escribirse las dependencias: `pyproject.toml`.
2. Seguir las mejores prácticas. Debe permitir:
   ***2.1 Gestión de entornos virtuales*** para aislar la instalación de dependencias del proyecto con las que puedan existir de manera global en el SO de trabajo, con el objetivo de evitar problemas entre versiones o instalaciones "sucias".
   ***2.2 Creación de un fichero que liste las dependencias y la versión exacta que se requiere instalar de las mismas, bloqueando el uso de esas bibliotecas y paquetes concretos (\*).*** Se denomina *lock file*, con extensión `.lock` en la mayoría de casos. El objetivo es facilitar la reproductividad de la aplicación, dejando fijas las dependencias y especificando de forma exacta la configuración del proyecto, para cualquier persona que trabaje sobre él o simplemente, lo utilice.
3. ***Herramienta activa.*** Para no aumentar la deuda técnica, se debe considerar una herramienta que tenga un mantenimiento activo con lanzamiento de actualizaciones más o menos frecuente y con soporte.

(*) Con respecto al criterio 2.2, me he documentado a partir de [PEP665](https://peps.python.org/pep-0665/#specification). Como se indica, se descartó como PEP, pero es una buena práctica disponible para este lenguaje, así como existe para otros lenguajes como JavaScript (npm).

****

### :dart: Candidatos considerados

Los gestores de dependencias considerados atendiendo a los criterios citados son:

A1. **[poetry](https://python-poetry.org/)** :

* (1.1): Trabaja con `pyproject.toml`. :heavy_check_mark: [Poetry : Project setup](https://python-poetry.org/docs/basic-usage/#project-setup)
* (2.1): Permite trabajar con entornos virtuales. :heavy_check_mark: [Poetry : Using venv](https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment)
* (2.2): Genera fichero `.lock`de fijación de dependencias. :heavy_check_mark: [Poetry : Installing dependencies](https://python-poetry.org/docs/basic-usage/#installing-dependencies)
* (3): Herramienta activa. :heavy_check_mark: [Poetry : 1.3.0 2022-12-09 History](https://python-poetry.org/history/)

A2. **[pdm](https://pdm.fming.dev/latest/)**:

* (1.1): Trabaja con `pyproject.toml`. :heavy_check_mark: [Pdm : Manage Dependencies](https://pdm.fming.dev/2.3/usage/dependency/)
* (2.1): Permite trabajar con entornos virtuales. :heavy_check_mark: [Pdm : Using venv](https://pdm.fming.dev/2.3/usage/venv/)
  * Además, trabaja con [PEP558](https://www.python.org/dev/peps/pep-0582/) como alternativa. [Pdm: Using PEP582](https://pdm.fming.dev/2.3/usage/pep582/)
* (2.2): Genera fichero `.lock`de fijación de dependencias. :heavy_check_mark:  [Pdm : Add Dependencies](https://pdm.fming.dev/latest/usage/dependency/#add-dependencies)
* (3): Herramienta activa. :heavy_check_mark: [Pdm : 2.3.3 2022-12-15](https://pdm.fming.dev/2.3/dev/changelog/)

A3. **[hatch](https://hatch.pypa.io/dev/)** :

* (1.1): Trabaja con `pyproject.toml`. :heavy_check_mark: [Hatch : Configuration](https://hatch.pypa.io/1.6/intro/#configuration)
* (2.1): Permite trabajar con entornos virtuales. :heavy_check_mark: [Hatch : Using venv](https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment)
* (2.2): Genera fichero `.lock`de fijación de dependencias. :heavy_check_mark: [Poetry : FAQ lockfile](https://hatch.pypa.io/latest/meta/faq/#libraries-vs-applications)
* (3): Herramienta activa. :heavy_check_mark: [Hatch : 1.6 October 19,2022 History](https://hatch.pypa.io/1.6/)

****

### :star: Otros criterios o características adicionales para elección

Los tres gestores de dependencias especificados, son totalmente válidos para su uso en el proyecto, no obstante, se tendrán en consideración algunas cuestiones ya de caracter secundario y/o subjetivo, como:

* :warning: ***Dependency hell***: La resolución de las dependencias no es una cuestión trivial. Se estudiará cómo aborda este problema las diversas herramientas y con qué frecuencia se producen fallos.

* :warning: ***Popularidad***: A través de artículos y otros lugares de la comunidad, se estudiará qué opinión y valoración dan las personas que utilizan dichas herramientas. Se tendrá en cuenta las recomendaciones oportunas.
* :x: ***Rendimiento***: Aunque en determinados proyectos es un tema importante. En mi caso, no considero que el volumen de dependencias sea excesivamente alto, por lo que diferencias poco significativas en rendimiento, no se tendrán en cuenta.

****

### :bulb: Elección

Con respecto a los criterios adicionales:

1. Con respecto a la resolución sin fallos de dependencias, Poetry y PDM, normalmente las resuelven bien, aunque ha habido casos en los que se han producido problemas en ambos ([Python PDM First Look](https://jasoncausey.net/post/python-pdm-first-look/)). De Hatch, no se ha encontrado información.
2. Se recomienda prinicipalmente Poetry como gestor de dependencias, valorando también PDM como segunda alternativa.
3. El rendimiento entre Poetry, PDM y Hatch es similiar.



La herramienta elegida por tanto, es **poetry**.
