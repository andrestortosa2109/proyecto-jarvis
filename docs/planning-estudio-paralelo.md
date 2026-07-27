# Planning de estudio paralelo al proyecto (8 semanas)

**La regla madre:** el proyecto manda (70%), el estudio acompaña (30%). Esto son ~5-6 h/semana de estudio además del proyecto. Si una semana vas apurado, recorta estudio, nunca proyecto — un proyecto terminado vale más que tres cursos a medias.

**Los cuatro recursos y cómo se usa cada uno:**

- **freeCodeCamp en español** (freecodecamp.org/espanol) — interactivo, escribes código desde el minuto 1. Se usa en dosis diarias: 30 min/día, vale hacerlo en el móvil en ratos muertos. Objetivo: soltura en Python.
- **CS50x de Harvard** (cs50.harvard.edu/x) — los fundamentos: cómo piensa un programador. Se usa en un bloque semanal fijo de 2-3 h (recomiendo sábado por la mañana): ver la clase (a 1.5x se puede) + intentar el problem set aunque no lo termines. Es tu "asignatura" del verano.
- **Exercism** (exercism.org) — el gimnasio. Ejercicios cortos revisados por mentores humanos gratis. Se empieza en la semana 5, cuando ya tengas base: 2 ejercicios/semana, y SIEMPRE pide mentoría — que un profesional te diga "esto se escribe así" es oro.
- **learncpp.com** — NO es un curso a seguir: es el diccionario. Se consulta cuando el firmware te exija algo que no entiendes (punteros, referencias, clases).

---

## El calendario, semana a semana

### Semana 0 (esta) — mientras terminas Wokwi y JARVIS v0

- **freeCodeCamp:** empieza "Python para todos" o el módulo de fundamentos de Python. 30 min/día. Notarás que jarvis_v0.py se vuelve legible.
- **CS50:** crea cuenta en edX y ve la Lección 0 (introducción). Es ligera; sirve para engancharte.
- *Por qué así:* JARVIS ya te está pidiendo Python; alimenta esa necesidad.

### Semana 1 — PWM y fundamentos ESP32 (proyecto en C++)

- **CS50:** Lección 1 (C). Con tu base de ensamblador te resultará familiar — verás qué hace el compilador que tú hacías a mano.
- **freeCodeCamp:** sigue con la dosis diaria de Python.
- *Conexión:* el C de CS50 y el C++ de tu firmware son primos hermanos; todo lo que aprendas el sábado lo usarás el lunes.

### Semana 2 — Torreta pan-tilt (el firmware crece)

- **CS50:** Lección 2 (arrays, memoria básica).
- **learncpp:** primera consulta guiada — lee los capítulos de funciones y scope cuando ordenes tu código en funciones.
- *Conexión:* tu firmware guardará posiciones de servos en arrays esta misma semana.

### Semana 3 — Cinemática y servidor web

- **CS50:** Lección 3 (algoritmos, búsqueda, ordenación).
- **freeCodeCamp:** remata el certificado básico de Python este fin de semana si puedes.
- *Conexión:* la cinemática ES un algoritmo; empezarás a pensar en pasos formales.

### Semana 4 — API HTTP + decisión del brazo

- **CS50:** Lección 4 (memoria, PUNTEROS). La lección más importante del curso para un ingeniero embebido — tómala con calma, repite lo que haga falta.
- **learncpp:** capítulos de punteros y referencias como refuerzo.
- *Conexión:* en un ESP32 con 520 KB de RAM, entender memoria es supervivencia. Esta semana conecta CS50 con tu chip de verdad.

### Semana 5 — JARVIS: Python y voz (el proyecto cambia a Python)

- **CS50:** Lección 5 (estructuras de datos).
- **Exercism:** ¡empieza! Track de Python, 2 ejercicios, pide mentoría en ambos.
- **freeCodeCamp:** baja a mantenimiento (repaso, ratos muertos) — Exercism toma el relevo.
- *Conexión:* toda la semana escribirás Python real; los ejercicios te pulirán el estilo.

### Semana 6 — El cerebro LLM

- **CS50:** Lección 6 (¡Python!). Verás formalizado lo que llevas 2 semanas haciendo — es la lección que más cuesta abajo se te hará.
- **Exercism:** 2 ejercicios más de Python. Busca los de manejo de strings y diccionarios (JARVIS vive de eso).
- *Extra:* lee sobre `async/await` cuando el bucle de voz te lo pida.

### Semana 7 — Domótica y MQTT

- **CS50:** semana de comodín — úsala para terminar problem sets pendientes o descansar de CS50 (la lección de SQL puedes saltarla sin culpa: no la necesitas aún).
- **Exercism:** abre el track de C++ (2 ejercicios fáciles). Vuelves a C++ justo cuando tu firmware necesita su último empujón.
- **learncpp:** consulta clases/structs si quieres ordenar el firmware como un pro.

### Semana 8 — Integración final

- **Estudio en pausa casi total:** esta semana es 90% proyecto. Solo mantén 1 ejercicio de Exercism para no perder el hábito.
- **CS50 final project:** truco legal — tu JARVIS *puede ser* tu proyecto final de CS50. Grabas el vídeo de demo, escribes la descripción, y te llevas el certificado de Harvard con el mismo trabajo. Dos pájaros, un tiro.

### Después del verano (septiembre)

- **Libro:** *Making Embedded Systems* de Elecia White — ahora sí, con 8 semanas de firmware encima, lo leerás asintiendo.
- **Exercism:** ritmo de mantenimiento (1-2/semana) alternando C++ y Python.
- **CS50:** si te quedaron lecciones, termínalas con calma; el certificado no caduca.

---

## Resumen visual de carga

| Semana | Proyecto (manda) | CS50 (sáb, 2-3h) | freeCodeCamp (30min/día) | Exercism | learncpp |
|---|---|---|---|---|---|
| 0 | Wokwi + JARVIS v0 | Lección 0 | Python básico | — | — |
| 1 | PWM real | Lección 1 (C) | Python | — | — |
| 2 | Torreta | Lección 2 | Python | — | funciones |
| 3 | Cinemática | Lección 3 | rematar cert. | — | — |
| 4 | API + brazo | Lección 4 (!) | mantenimiento | — | punteros |
| 5 | Voz | Lección 5 | — | Python ×2 | — |
| 6 | LLM | Lección 6 (Py) | — | Python ×2 | — |
| 7 | MQTT | comodín | — | C++ ×2 | clases |
| 8 | Integración | proyecto final* | — | ×1 | — |

(!) = la lección clave para embebidos. * = presenta tu JARVIS como proyecto final de CS50.

**Última regla:** si un sábado no puedes con CS50, no lo saltes — hazlo el domingo más corto. La constancia semanal vale más que la intensidad. Y cualquier concepto que se atragante, tráemelo: lo vemos juntos sobre tu propio código.
