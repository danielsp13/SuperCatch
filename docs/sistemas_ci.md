# Sistemas de Integración Continua (CI)

En este documento se especifica el procedimiento para la elección de sistemas de Integración Continua que nos permita la ejecución de tests cuando se realicen cambios en el repositorio.

****

### :page_with_curl: Criterios para elección de CI:

1. ***Sistema gratuito:*** Para proyectos públicos como el caso de este repositorio, lo más conveniente es usar un sistema que podamos utilizar libremente.
2. ***Compatible con [Github Checks](https://docs.github.com/en/rest/checks?apiVersion=2022-11-28):*** Para poder realizar comprobaciones contra los cambios de código en el repositorio.
3. ***Trabajar con Docker:*** Es decir, para testear el contenedor con la imagen base elegida en [imagen docker](docker.md).

****

### :star: Características adicionales para elección



****

 ### :desktop_computer: Candidatos a la elección:

CI.1 **[Github Actions](https://github.com/features/actions)**: :heavy_check_mark:

1. **Sistema gratuito** (para sistemas públicos): :heavy_check_mark:
2. **Compatible con Github Checks**: [Github Actions : ckecks-action](https://github.com/marketplace/actions/github-checks) :heavy_check_mark:
3. **Trabajar con Docker**: :heavy_check_mark:

CI.2 **[Circle CI](https://circleci.com/docs/getting-started/)**: :heavy_check_mark:

1. **Sistema gratuito:** :heavy_check_mark:
2. **Compatible con Github Checks**: [Circle CI : Enable Github Checks](https://circleci.com/docs/enable-checks/) :heavy_check_mark:
3. **Trabajar con Docker**: [Circle CI: Running Docker Commands](https://circleci.com/docs/building-docker-images/) :heavy_check_mark:

CI.3 **[Semaphore CI](https://docs.semaphoreci.com/)**: :warning:

1.  **Sistema gratuito**: [Semaphore CI: Connecting GitHub with Semaphore](https://docs.semaphoreci.com/account-management/connecting-github-and-semaphore/) :heavy_check_mark:
2. **Compatible con Github Checks:** :warning: habrá que configurarlo para que lo use, ya que Semaphore envía statuses, no checks [Github: about statuses](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks).
3. **Trabajar con Docker:** [Semaphore CI: Working with Docker](https://docs.semaphoreci.com/ci-cd-environment/working-with-docker/) :heavy_check_mark:

CI.4 **[Cirrus CI](https://cirrus-ci.org/features/)**: :heavy_check_mark:

1. **Sistema gratuito:** (para repositorios públicos) :heavy_check_mark:
2. **Compatible con Github Checks:**  [Cirrus CI: Manual Tasks](https://cirrus-ci.org/guide/writing-tasks/#manual-tasks) :heavy_check_mark:
3. **Trabajar con Docker:** :heavy_check_mark:

CI.5 **[AppVeyor](https://www.appveyor.com/docs/)**: :x:

1. **Sistema gratuito:** :heavy_check_mark:
2. **Compatible con Github Checks:** :question: Según [appveyor/ci : issue 2311](https://github.com/appveyor/ci/issues/2311) comentan que no está soportado.
3. **Trabajar con Docker:** [AppVeyor: Docker](https://www.appveyor.com/docs/linux-images-software/#docker) :heavy_check_mark:

****

### :bulb: Elección

Se opta por elegir *Github Actions* y *Cirrus CI* como sistemas de integración, que son los que cumplen todos los criterios, aunque *Circle CI* es una posible alternativa a considerar.
