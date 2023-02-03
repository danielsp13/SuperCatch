# Contenedor Docker para pruebas

En este documento se especifica el procedimiento para la elección y despliegue de un contenedor de docker para ejecución de tests unitarios sobre la aplicación.

****

### :page_with_curl: Criterios para elección de imagen base:

Lo primero para desplegar un contenedor docker, es una imagen base sobre la que trabajaremos. Todas las imágenes consideradas deberán atender los siguientes criterios:

1. ***Tamaño.*** Es el criterio más importante. Se debe elegir la imagen que tenga *el menor tamaño posible*. El motivo es que no debe contener nada más que lo imprescindible para la ejecución de tests. Como consecuencia inmediata de esto, tendremos entre otras cosas un despliegue rápido del contenedor (aunque notemos que esta operación sólo se realizará una única vez).
1. ***Seguridad.*** En una imagen, existirán diferentes herramientas que vendrán incluidas por defecto. Se debe considerar una que disponga de la menor cantidad de vulnerabilidades importantes que puedan comprometer a la aplicación.

Aunque habrá más cuestiones a contemplar (como se habla justo a continuación), la versión de la imagen seleccionada siempre será la última disponible `latest`, pues el propósito de este contenedor es que sea *para realizar pruebas*.



#### :twisted_rightwards_arrows: Alternativas en la elección

Con estos criterios principales, hay tres alternativas diferentes que podemos tener en cuenta para la elección de la imagen base.

a) **Imágenes oficiales de Python:** Son imágenes publicadas que contienen la última versión de este lenguaje, y generalmente, gran parte de las bibliotecas del mismo.

b) **Imágenes no oficiales de Python:** Son imágenes publicadas por algunas empresas externas, como  [Bitnami](https://hub.docker.com/u/bitnami) [CircleCI](https://hub.docker.com/u/circleci) u [Okteto](https://hub.docker.com/u/okteto), para lenguajes y servicios en GitHub.

c) **Imágenes de Sistemas Operativos:** Son imágenes de sistemas operativos conocidos (Ubuntu, CentOS, etc...). Pueden considerarse como una alternativa a las otras dos, ya sean sus publicaciones oficiales, o alguna modificación de las mismas publicadas por otro usuario.



Contemplando estas alternativas, hay que considerar criterios adicionales:

*En el caso de elegir a) o b)*:

* La **versión de Python** que debe contener es la última disponible (y estable). 
* Disponer de la **utilidad `pip`**. Se debe verificar que dispone de pip, utilidad que permite instalar otras bibliotecas.



*En el caso de tomar c):*

* Disponer de **gestor de paquetes** u **otra utilidad de descarga/instalación** que permita instalar la última versión de Python, pues evidentemente, si no viene con la imagen habrá que instalarlo.
* Disponer de la **utilidad `pip`**.

****

### :star: Características adicionales para elección

Otras cuestiones adicionales utilizadas para la elección de la imagen base será:

1. Se utilizará la herramienta [Snyk Advisor : Docker](https://snyk.io/advisor/docker), para poder contemplar algunas características que puedan ser interesantes para tomar una decisión, como por ejemplo en el ámbito de seguridad, ya que analiza estas imágenes y muestra resultados de vulnerabilidades clasificadas por riesgo. *Nota: este supuesto sólo es para imágenes oficiales de Docker.*
2. Se tendrán en cuenta las mejores prácticas y recomendaciones en cuanto al despliegue de aplicaciones Python en contenedores virtuales, como por ejemplo se indican en:
   * *[Best practices for containerizing Python applications with Docker](https://snyk.io/blog/best-practices-containerizing-python-docker/)*.
   * *[Docker Best Practices for Python Developers](https://testdriven.io/blog/docker-best-practices/)*.
   * *[3 Simple Tips on Making Your Python Docker Images More Robust, Lighter Weight, and More Secure](https://python.plainenglish.io/3-simple-tips-on-making-your-python-docker-images-more-robust-lighter-weight-and-more-secure-61876bcdc257)*.



****

### :cd: Imágenes candidatas

En vista de las alternativas contempladas, se han considerado las siguientes imágenes candidatas, en lugares como [Docker Hub](https://hub.docker.com/). :heavy_check_mark:  APTA, :x:  NO APTA, :warning:  RIESGO DE USO.             

**Imágenes oficiales de [Python](https://hub.docker.com/_/python):**

O.1: **[python:<version\>](https://hub.docker.com/layers/library/python/latest/images/sha256-7efc1ae7e6e9c5263d87845cb00f6ab7f6b27670cae29c9d93fa7910d6ab12c0?context=explore)** :x:

* **Descripción:** Imagen por defecto. Se suele elegir cuando no se tiene claro qué necesidades se tienen.
* **SO:** Debian 11.
* **(1) Tamaño:** 339.1 MB. :x: Tamaño excesivo.
* **(2) Seguridad:** [Snyk Docker: Python:latest](https://snyk.io/advisor/docker/python/latest). :x: Esta versión contiene muchas vulnerabilidades, debido a que contiene una gran base de bibliotecas por defecto.

O.2: **[python:<version\>-slim](https://hub.docker.com/layers/library/python/3.8-slim/images/sha256-dd13c1d6433ecfa15dcf774d8fcce87cf790f0f85f96d21d2e81b31ad2e42e13?context=explore)** :heavy_check_mark:  

* **Descripción:** Contiene los paquetes mínimos necesarios para ejecutar python. 
* **SO:** Debian 11.
* **(1) Tamaño:** 44.81 MB. :heavy_check_mark:
* **(2) Seguridad:** [Snyk Docker: Python:slim](https://snyk.io/advisor/docker/python/slim). :heavy_check_mark: No contiene vulnerabilidades graves.

O.3: **[python:<version\>-alpine](https://hub.docker.com/layers/library/python/alpine/images/sha256-8deb76496a68d1bba8353767492235b26e45e6ddc571dbb3a487633144a4fbd4?context=explore)** :warning:

* **Descripción:** Basada en [Alpine Linux Project](https://alpinelinux.org/). Útil si el único factor importante es el tamaño de la imagen.
* **SO:** Alpine 3.17.1. 
* **(1) Tamaño:** 19 MB. :heavy_check_mark:
* **(2) Seguridad:** [Snyk Docker: Python:alpine](https://snyk.io/advisor/docker/python/alpine). :heavy_check_mark: No se han detectado vulnerabilidades.
* :warning: **Advertencias:** Se informa que esta imagen utiliza `musl libc`en vez de `glibc y derivados`, con la consecuencia de que puede que se produzcan problemas dependiendo del grado de profundidad en la dependencia con `libc`. Como tendremos que realizar instalaciones de otras dependencias, deberíamos <u>descartar</u> el uso de esta imagen.



**Imágenes no oficiales de Python:**

UO.1: **[circleci/python:latest](https://hub.docker.com/r/circleci/python)** :x:

* **Descripción:** Imagen no oficial que dispone de herramientas adicionales para el desarrollo, como `git`, `ssh`, etc. Además viene con usuario no-root por defecto. 
* **SO:** Sin especificar.
* **(1) Tamaño:** 534.04 MB. :x: Tamaño excesivo.
* **(2) Seguridad: ** :grey_question:. No hay información al respecto.

UO.2: **[bitnami/python:latest](https://hub.docker.com/layers/bitnami/python/latest/images/sha256-b245f31d366f6e7af4d270e0ba7980e1113e8c8ce3ceb276e50738fe95bfdd65?context=explore)** :x:

* **Descripción:** Dispone de un ciclo de actualizaciones bastante alto, además de corrección de bugs y otros errores de forma rápida y eficaz. Basado en [Minideb](https://github.com/bitnami/minideb).
* **SO:** Minideb. Una imagen minimalista basada en Debian.
* **(1) Tamaño:** 217.56 MB. :x: Tamaño excesivo.
* **(2) Seguridad:** :grey_question:. No hay información al respecto.

UO.3: **[okteto/python:3](https://hub.docker.com/layers/okteto/python/3/images/sha256-2de227fc1951a0ed86c7703776674f8052dbf975673356c66bf05d0f2df83484?context=explore)** :x:

* **Descripción:** Contiene un entorno de desarrollo para Python para ser utilizada por el [Cliente de Okteto](https://github.com/okteto/okteto).
* **SO:** Sin especificar.
* **(1) Tamaño:** 352.44 MB. :x: Tamaño excesivo.
* **(2) Seguridad:** :grey_question:. No hay información al respecto.



**Imágenes de Sistemas Operativos:**

SO.1: **[ubuntu:latest](https://hub.docker.com/layers/library/ubuntu/latest/images/sha256-c985bc3f77946b8e92c9a3648c6f31751a7dd972e06604785e47303f4ad47c4c?context=explore)** :warning: 

* **Descripción:** Contiene paquetes mínimos para el correcto funcionamiento de ubuntu.
* **SO:** Ubuntu 22.04 LTS.
* **(1) Tamaño:** 29.95 MB. :heavy_check_mark: 
* **(2) Seguridad:** [Snyk Docker: ubuntu:latest](https://snyk.io/advisor/docker/ubuntu). :warning:  Se han detectado 2 vulnerabilidades de riesgo medio.

SO.2 (a): **[debian:latest](https://hub.docker.com/layers/library/debian/latest/images/sha256-640e07a7971e0c13eb14214421cf3d75407e0965b84430e08ec90c336537a2cf?context=explore)** :heavy_check_mark:

* **Descripción:** Contiene paquetes mínimos para el correcto funcionamiento de debian.
* **SO:** Debian 11.
* **(1) Tamaño:** 52.48 MB. :heavy_check_mark:
* **(2) Seguridad:** [Snyk Docker: debian:latest](https://snyk.io/advisor/docker/debian). :heavy_check_mark:. No se han detectado vulnerabilidades.

SO.2 (b): **[debian:stable-slim](https://hub.docker.com/layers/library/debian/stable-slim/images/sha256-9554f6caf2cafc99ad9873a822e1aafbb29d40608fe7ebe6569365b80fa5a422?context=explore)** :heavy_check_mark:

* **Descripción:** Versión aún más reducida de la imagen latest.
* **SO:** Debian 11.
* **(1) Tamaño:** 29.94 MB. :heavy_check_mark:
* **(2) Seguridad:** [Snyk Docker: debian:stable-slim](https://snyk.io/advisor/docker/debian/stable-slim). :heavy_check_mark:. No se han detectado vulnerabilidades.

SO.3: **[fedora:latest](https://hub.docker.com/_/fedora)** :heavy_check_mark:

* **Descripción:** Contiene paquetes mínimos para el correcto funcionamiento de fedora.
* **SO:** Fedora 37.
* **(1) Tamaño:** 63.03 MB. :heavy_check_mark:.
* **(2) Seguridad:** [Snyk Docker: fedora:latest](https://snyk.io/advisor/docker/fedora). :heavy_check_mark: . No se han detectado vulnerabilidades.

****

### :bulb: Elección

Las imágenes que pueden ser válidas para el proyecto son:`python-slim`, `debian-latest`, `debian-stable-slim`, y `fedora-latest`. Para determinar definitivamente la elegida, se tendrá en cuenta que:

* En `python-slim`, ya disponemos de Python `versión 3.11.1` instalado y con la utilidad `pip`para instalar más dependencias. 
  * Tamaño de la imagen descomprimida: 128 MB.
* En `debian-latest`, no disponemos de Python ni de `pip`, y la instalación manual de ambas requiere de un espacio adicional de aproximadamente +500 MB, ya que `pip` necesita de muchos paquetes adicionales para su correcta instalación.
  * Tamaño de la imagen descomprimida: 124 MB.
* En `debian-stable-slim`, sucede exactamente lo mismo que en la versión latest.
  * Tamaño de la imagen descomprimida: 80.5 MB.
* En `fedora-latest`, sí disponemos de Python  `versión 3.11.0`, pero no disponemos de la utilidad `pip`, por lo que hay que instalarla, requiriendo un espacio adicional aproximado de +7MB.
  * Tamaño de la imagen descomprimida: 184 MB.



En definitiva, las únicas imágenes candidatas son `python-slim`, y `fedora-latest`. Sin embargo, siguiendo el principio del primer criterio, se elige como imagen candidata la versión `python-slim`, ya que de las dos es la que tiene menor tamaño, y contiene los útiles básicos para cubrir otras necesidades como instalación de dependencias.
