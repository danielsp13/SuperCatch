# MODELO DE SOLUCIÓN



### Infraestructura Virtual (2022/23)

****

*Autor: danielsp13 (Daniel Pérez Ruiz)*. Este documento lo he creado para desarrollar un primer modelo orientativo para la solución que propongo, en el que reflejaré con más detalle que en el readme algunas cuestiones que son importantes y necesarias para validar, principalmente, la lógica de negocio que hay detrás de la aplicación.

****

#### Fase 1: ¿Quiénes son los usuarios reales de la aplicación? ¿Y clientes?

Usando la metodología de "personas":

> Juan Campos, 53 años, entrenador del equipo de fútbol de tercera división española, Monachil CF. Esta es su segunda temporada al cargo. En la anterior, no le fue muy bien y el equipo no pudo pelear por el ascenso a la siguiente categoría. En esta nueva campaña, necesita una solución para planificar mejor la temporada y evitar que los jugadores lleguen cansados al final, o que se pierdan partidos que no se deberían perder.

Juan es nuestro potencial usuario de la aplicación, en combinación con su equipo técnico. Pero, ¿son ellos realmente quienes nos comprarán el producto? No, quien estaría realmente interesado en nuestro producto, y quien de verdad sería ***nuestro cliente***, es ***la entidad deportiva (equipo de fútbol en cuestión)***. 

****

#### Fase 2: ¿Qué datos se necesitan para la solución? ¿Quiénes los proporcionan? 

Para la aplicación se requieren un conjunto de datos considerable, que son:

* *Ficha técnica de los jugadores*: Proporcionado por la sección deportiva del club. Contiene todos los atributos técnicos del jugador típicos, a destacar: *posición que juega, posición alternativa, edad, etc.*.
* *Atributos de los jugadores:* Proporcionado por la sección deportiva del club. Cuando se ficha a un jugador, este pasa un reconocimiento médico para ver sus cualidades. Estos datos son clave para el seguimiento del jugador y concretamente podemos tener los atributos de *velocidad, pase, tiro, potencia física, defensa* además de otras cosas adicionales como *tendencia a lesión,...*.

* *Ejercicios de entrenamiento:* Proporcionado por el cuerpo técnico. Cada ejercicio de entrenamiento debe especificar el *tipo de entrenamiento (individual,grupo), cualidad que se trabaja, grado de dificultad, tiempo de duración...*. Estos ejercicios propuestos por el cuerpo técnico serán la base para la posterior toma de decisiones de la aplicación.
* *Calificaciones y resultados:* Proporcionado por el entrenador. El entrenador una vez tiene la planificación del entrenamiento del día **(recibida por nuestra aplicación)**, otorga una calificación a cada jugador, lo que se verá reflejado en el sistema como una actualización de los atributos del jugador.

****

#### Fase 3: ¿Qué lógica de negocio hay detrás de la aplicación?

Se requerirá un manejo de cálculo importante estadístico como pueden ser medias / desviaciones típicas, varianzas... También se requerirá desarrollo de algoritmos para la asignación y planificación de los entrenamientos (ejemplo: no es conveniente que si se hacen subgrupos de trabajo, un mismo jugador haga ejercicios con demasiada dificultad; o también, el orden en el que estos entrenamientos se planifican hay que tenerlo en cuenta, ya que los jugadores no pueden terminar el día estando demasiado cansados, etc...) . Finalmente, también se puede requerir visualización de gráficos o informes para que el entrenador pueda recibir toda esta información de una manera cómoda.

