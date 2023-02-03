# Test Runner

En este documento se especifican los criterios para la elección de un test runner, herramienta que permitirá ejecutar los tests para realizar pruebas sobre el código.

****

### :page_with_curl: Criterios para elección de test runner:

Cualquier herramienta que considere como potencial para usarla en el proyecto, debe cumplimentar:

1. ***Herramienta activa***. Debe considerarse una herramienta que tenga actualizaciones con relativa frecuencia y un soporte continuado y activo.
2. ***Rendimiento***. Debe ejecutar todos los tests que se realicen en el menor tiempo posible. El objetivo que se debe alcanzar es facilitar la validación de las funcionalidades implementadas, ejecutando dichos tests en múltiples ocasiones.
2. ***Ausencia de problemas de seguridad.*** La herramienta no debe tener brechas de seguridad que puedan comprometer a la aplicación.

****

### :star: Otros criterios o características adicionales para elección

Se tendrán en consideración algunas cuestiones de carácter secundario y/o subjetivo, como:

* :warning: ***Popularidad***: A través de artículos y otros lugares de la comunidad, se estudiará qué opinión y valoración dan las personas que utilizan dichas herramientas. Se tendrá en cuenta las recomendaciones oportunas.

****

Para medir todos los criterios se ha utilizado la herramienta [Snyk Advisor](https://snyk.io/advisor/python/) , que examina módulos de Python según una serie de criterios (como los que se han mencionado) y otorga una puntuación en un rango de 0 a 100.

****

### :dart: Candidatos considerados

Los test runner considerados atendiendo a los criterios citados son:

A1. **[nose2](https://docs.nose2.io/en/latest/)** : [Puntuación en [Snyk - Nose2](https://snyk.io/advisor/python/nose2) : 78]
* (1) Herramienta activa: [nose2_changelog](https://docs.nose2.io/en/latest/changelog.html) (16-07-2022) :heavy_check_mark: . 
  * (En [github:nose-devs/nose2](https://github.com/nose-devs/nose2), hay actividad reciente a pesar de no haber más cambios oficiales indicados en su web.)
* (2) Seguridad: :heavy_check_mark:
  * No se han detectado problemas de seguridad importantes.

* (3) Información sobre rendimiento: :heavy_check_mark: 
  * Basado en `unittest`.
  * Permite ejecución paralela de tests. [Nose2: Running tests in parallel](https://docs.nose2.io/en/latest/plugins/mp.html)
  * Dispone de un mecanismo de detección automática de tests. [Nose2: Loader: Test discovery](https://docs.nose2.io/en/latest/plugins/discovery.html)
* (op1) Popularidad de la herramienta: :heavy_check_mark: 
  * Está bien considerada por la comunidad, siendo influyente en bastantes proyectos de Python.
  * No se han detectado problemas, bugs notificados por usuarios que rechacen su uso.
  * Los propios desarrolladores de esta herramienta, también recomiendan tener en cuenta **pytest**, como una alternativa. [Nose2: nose2_vs_pytest](https://docs.nose2.io/en/latest/#nose2-vs-pytest).

A2. **[pytest](https://docs.pytest.org/en/7.2.x/)** : [Puntuación en [Snyk - Pytest](https://snyk.io/advisor/python/pytest) : 97]
* (1) Herramienta activa: [pytest_changelog](https://docs.pytest.org/en/7.2.x/changelog.html) (13-01-2023) :heavy_check_mark: . 
  * (En [github:pytest-dev/pytest](https://github.com/pytest-dev/pytest), hay actividad muy reciente. No hay más que tener en cuenta el lanzamiento reciente de una nueva versión.)
* (2) Seguridad: :heavy_check_mark:
  * No se han detectado problemas de seguridad importantes.
* (3) Información sobre rendimiento (extraido de [pytest_features](https://github.com/pytest-dev/pytest#features)): :heavy_check_mark: 
  * Puede ejecutar tests escritos en `nose` (ojo, [distinto](https://docs.nose2.io/en/latest/differences.html#nose2-is-not-nose) de `nose2` ), y de `unittest`.
  * Proporciona información detallada sobre aserciones fallidas.
  * Fixtures modulares para el manejo de tests. [Pytest: Fixtures](https://docs.pytest.org/en/stable/explanation/fixtures.html)
  * Dispone de un mecanismo de detección automática de tests. [Pytest: Test discovery](https://docs.pytest.org/en/stable/explanation/goodpractices.html#python-test-discovery)
* (op1) Popularidad de la herramienta: :heavy_check_mark: 
  * Es de las herramientas más populares entre la comunidad, además de ser influyente en gran cantidad de proyectos.
  * No se han detectado problemas, bugs o fallos de seguridad recientes que rechacen su uso.

:warning: Se han considerado otros test runners, pero no entran en esta lista por no verificar la condición de herramientas activas, por tanto, ni siquiera se nombrarán.

****

### :bulb: Elección

Ambos test runner elegidos, pueden ser totalmente válidos para el proyecto. Por las propias recomendaciones de la comunidad, y ser una herramienta más influyente frente a otra (además de tener una versión más reciente), **pytest** es la mejor opción.
