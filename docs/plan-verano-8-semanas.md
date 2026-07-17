# Plan de verano: Brazo robótico + JARVIS en 8 semanas (<100 €)

**Estrategia:** los dos proyectos en secuencia, no en paralelo. Semanas 1-4 el brazo (hardware y control), semanas 5-8 el JARVIS (software e integración). Final: controlas el brazo por voz. Un solo proyecto que se integra vale más que dos a medias.

**Dedicación asumida:** 2-3 h/día, 5 días/semana. Si dedicas más, adelanta; no acumules teoría sin montar nada.

**No compres Raspberry Pi:** tu PC hará de servidor JARVIS. Mismo aprendizaje, 0 €.

---

## Qué es cada elemento, cómo funciona y para qué lo compras

**ESP32 (viene dentro del kit ELEGOO).** Un microcontrolador: un ordenador diminuto sin pantalla ni sistema operativo que ejecuta tu código directamente sobre el hardware. Doble núcleo a 240 MHz con WiFi y Bluetooth integrados. Sus pines GPIO leen sensores y generan señales eléctricas; entre ellas el PWM que controla servos. En tu proyecto es el cerebro del brazo: recibe órdenes por WiFi (de tu móvil o de JARVIS) y mueve los servos. También activará el relé.

**Servos SG90 (2 en la torreta + repuestos + 1 extra en el kit).** Un servo es un motor con control de posición: dentro lleva motor DC, engranajes reductores, un potenciómetro que mide el ángulo del eje y un circuito que lo corrige constantemente. Se controla con pulsos a 50 Hz: un pulso de 1 ms = 0°, 2 ms = 180°. Esto es exactamente lo que aprenderás a generar la semana 1. En la torreta, un servo es el eje horizontal (pan) y otro el vertical (tilt).

**Torreta pan-tilt (2 ejes).** Dos servos montados en soportes perpendiculares: uno gira en horizontal (pan) y otro inclina en vertical (tilt). Es la versión mínima de un brazo robótico: los mismos problemas de PWM, alimentación, control coordinado y cinemática, por una décima parte del coste. En la semana 4, con criterio ya formado, decides si dar el salto al brazo completo (ver opciones al final de la lista de compras); todo lo aprendido y los servos de repuesto se reutilizan.

**Fuente 5V 3A.** Convierte los 230 V alternos del enchufe en 5 V continuos. Es imprescindible porque cada SG90 puede pedir picos de ~0,8 A bajo carga; dos o más a la vez superan los 0,5 A que da un puerto USB — si alimentas los servos desde el ESP32, se reinicia o se quema. Regla de oro: servos a la fuente, ESP32 por USB, y las masas (GND) de ambos conectadas entre sí. *Añade un adaptador jack hembra a bornes (~2 €, búscalo como "adaptador jack DC hembra bornes") para conectar la fuente a la protoboard sin cortar cables.*

**Relé de 2 canales optoacoplado.** Un interruptor accionado eléctricamente: una señal de 3,3 V del ESP32 activa una bobina que cierra un contacto físico capaz de conmutar cargas mucho mayores. El "optoacoplador" aísla el microcontrolador del circuito de potencia mediante luz (un LED interno y un fototransistor), de modo que un fallo en la carga no puede quemar el ESP32. Es lo que le da "manos" a JARVIS: encender y apagar cosas reales. Empieza conmutando cargas de 5-12 V (tira LED, lámpara USB); no toques 230 V hasta que domines el montaje.

**Micrófono USB omnidireccional.** Cápsula de condensador + conversor analógico-digital + interfaz USB: el PC lo detecta como dispositivo de audio sin drivers. Omnidireccional significa que capta desde cualquier dirección, ideal para hablarle a JARVIS desde donde estés en el cuarto. Es la entrada de voz del sistema.

**Protoboard, cables dupont y resistencias (en el kit).** La protoboard es una placa de prototipado con contactos de muelle interconectados por filas: montas circuitos insertando componentes, sin soldar, y los deshaces igual. Los cables dupont conectan protoboard, módulos y ESP32. Las resistencias limitan corriente (p. ej., proteger un LED) y forman divisores de tensión. Son la mesa de trabajo de toda la electrónica que harás.

**Los ~35 módulos del kit ELEGOO (pantalla OLED, sensores, teclado, pulsadores...).** No son imprescindibles para el brazo, pero son tu material de futuro: la OLED puede mostrar el estado de JARVIS, un sensor ultrasónico mide distancias (detección de objetos para el brazo), un PIR detecta presencia (JARVIS te saluda al entrar)... Cada módulo es un proyecto de fin de semana ya pagado.

**Cómo encaja todo (arquitectura final):** tu voz → micrófono USB → PC (Whisper transcribe, el LLM decide) → orden por WiFi (HTTP/MQTT) → ESP32 → PWM a los servos del brazo o señal al relé → algo se mueve o se enciende en el mundo real.

---

## Blindaje de tu ordenador — reglas de seguridad

El único camino físico entre el circuito y tu PC es el cable USB del ESP32. Por ahí pueden pasar dos cosas malas: **retroalimentación** (meter corriente de la fuente externa hacia el puerto USB) y **cortocircuito** (un cable mal puesto que exige al puerto más corriente de la que debe dar). Estas reglas eliminan el riesgo:

1. **La fuente externa alimenta SOLO a los servos.** Nunca conectes el +5V de la fuente al pin 5V/VIN del ESP32 mientras esté enchufado por USB. Con el ESP32 se comparte únicamente GND (masa común). Esta es la regla de oro.
2. **Cablea siempre con todo desenchufado** (USB fuera, fuente fuera). Revisa el montaje completo antes de dar corriente, en este orden: primero la fuente de los servos, después el USB.
3. **Hub USB como fusible sacrificial (~8 €, recomendado).** Conecta el ESP32 al PC a través de un hub USB barato: si algún día algo falla, se quema el hub, no tu placa base. Es el blindaje definitivo por el precio de un menú.
4. **Comprueba polaridad dos veces.** El 90% de los accidentes es cruzar 5V y GND en la protoboard. Usa siempre el mismo código de colores: rojo = 5V, negro = GND, y no lo rompas jamás.
5. **Nada de 230 V.** El relé conmuta solo cargas de 5-12 V (tira LED, lámpara USB). La red eléctrica queda fuera de este proyecto.
6. **Si el PC avisa de "sobrecorriente en USB" o el puerto se apaga:** desconecta, busca el corto con calma y no reconectes hasta encontrarlo. Ese aviso es la protección de tu placa funcionando, no un daño.

Lo estadísticamente probable no es dañar el ordenador, es quemar un servo o un ESP32 (~7 €). Por eso el kit trae repuestos: es parte del aprendizaje, no una tragedia.

---

## Enlaces de compra (verificados en Amazon.es, julio 2026)

**OPCIÓN A — Kit de iniciación + torreta pan-tilt (recomendada): ~96,45 € total.** Un kit trae de golpe protoboard, cables, resistencias, LEDs, servo extra, pantalla OLED, teclado y ~35 módulos/sensores que te servirán para futuros proyectos, con 30+ proyectos guiados:

| Producto | Valoración | Precio | Enlace |
|---|---|---|---|
| ELEGOO Super Kit de Inicio ESP-32 (placa incluida, 35+ módulos) | 4,4★ (56) | 39,99 € | https://www.amazon.es/ELEGOO-Tutorial-Desarrollo-Microcontrolador-Compatible/dp/B0FVWW7MD4 |
| Soporte pan-tilt 2 ejes con rodamiento | 4,6★ | 11,05 € | https://www.amazon.es/Bracket-Multifunci%C3%B3n-Tornillos-Cojinete-Importados/dp/B0B3W2MPF5 |
| Pack 3× servo SG90 | 4,4★ (19) | 8,99 € | https://www.amazon.es/microservomotores-miniservos-proyectos-rob%C3%B3ticos-helic%C3%B3pteros/dp/B0FK5P4W3S |
| Fuente 5V 3A con jack 5,5 mm | 4,4★ (200) | 12,95 € | https://www.amazon.es/Fuente-alimentaci%C3%B3n-CA-CC-Clavija/dp/B0BYS9Y2B6 |
| AZDelivery relé 2 canales optoacoplado | 4,6★ (968) | 5,49 € | https://www.amazon.es/AZDelivery-Optoacoplador-Low-Level-Trigger-Compatible-Incluido/dp/B078Q326KT |
| Micrófono USB conferencia omnidireccional | 4,4★ (493) | 17,98 € | https://www.amazon.es/Micr%C3%B3fono-Conferencia-Ordenador-Condensador-Omnidireccional/dp/B0CP7ZSJK9 |

Añade si quieres blindaje total del PC: un hub USB básico (~8 €, cualquiera bien valorado sirve: https://www.amazon.es/s?k=hub+usb+4+puertos).

Con esta opción un solo ESP32 controla brazo + relé (mismo nodo); la tira LED sobra porque el kit trae LEDs. Ajuste del plan: el "segundo ESP32" de la semana 7 se sustituye por el mismo ESP32 del brazo.

**Alternativa al kit si quieres visión artificial en el futuro:** Freenove Ultimate ESP32-WROVER con CÁMARA integrada, 240 piezas, 122 proyectos — 4,4★ (216), 57,95 € — https://www.amazon.es/Freenove-Ultimate-ESP32-WROVER-Included-Compatible/dp/B0CJJJ7BCY (sube el total a ~117 €, pero la cámara abre proyectos de reconocimiento tipo Stark).

**OPCIÓN B — Piezas sueltas: ~96 €.** Más barata por poco, sin extras para el futuro:

| Producto | Valoración | Precio | Enlace |
|---|---|---|---|
| ELEGOO 2× ESP32 Type-C | 4,6★ (171) | 14,99 € | https://www.amazon.es/ELEGOO-Desarrollo-ESP-WROOM-32-Microcontrolador-Compatible/dp/B0D8T7LZF2 |
| BOJACK kit 2× protoboard 830 + cables + resistencias | 4,5★ (486) | 13,99 € | https://www.amazon.es/BOJACK-Breadboard-Soldadura-Flexibles-Protoboard/dp/B0B18G3V5T |
| Fuente 5V 3A con jack 5,5 mm | 4,4★ (200) | 12,95 € | https://www.amazon.es/Fuente-alimentaci%C3%B3n-CA-CC-Clavija/dp/B0BYS9Y2B6 |
| AZDelivery relé 2 canales optoacoplado | 4,6★ (968) | 5,49 € | https://www.amazon.es/AZDelivery-Optoacoplador-Low-Level-Trigger-Compatible-Incluido/dp/B078Q326KT |
| Micrófono USB conferencia omnidireccional | 4,4★ (493) | 17,98 € | https://www.amazon.es/Micr%C3%B3fono-Conferencia-Ordenador-Condensador-Omnidireccional/dp/B0CP7ZSJK9 |
| Tira LED COB USB 5V 1m | 4,3★ | 8,56 € | https://www.amazon.es/OULARA-Regulable-320ledes-iluminaci%C3%B3n-Dormitorio/dp/B0D5MJC4ZX |
| Brazo robótico 4DOF | — | 22,29 € | https://www.amazon.es/VIFER-Kit-Brazo-rob%C3%B3tico-RaspberryPi/dp/B086K15F38 |

**El brazo — decisión aplazada a la semana 4 (a propósito):** empiezas con la torreta pan-tilt y, cuando ya sepas lo que es controlar servos de verdad, eliges brazo con criterio. Las tres rutas, de mejor a peor relación calidad/precio:

1. **Imprimir el EEZYbotARM MK2 (~35 €):** brazo open source diseñado para servos de 9g, mecánica muy superior a los kits acrílicos (planos gratis en thingiverse.com/thing:1454048). Necesitas acceso a impresora 3D — pregunta en el fablab de tu universidad.
2. **Kit acrílico (~22 €) + servos MG90S metálicos:** el punto débil de los kits baratos son los engranajes de plástico de los SG90; con MG90S mejora mucho — Miuzei 10× metal, 4,4★ (321), 27,99 €: https://www.amazon.es/Miuzei-Servomotor-engranajes-unidades-Modelismo/dp/B0D7ZW6LSW
3. **Adeept 5-DOF (69,99 €):** la opción "compra y listo" de calidad, 4,1★ (275) — https://www.amazon.es/Adeept-rob%C3%B3tico-Compatible-Bricolaje-procesamiento/dp/B085C2S1N7

En AliExpress el kit del brazo y el relé salen 30-40% más baratos si no te importa esperar 2-3 semanas.

---

## FASE 1 — Torreta pan-tilt (semanas 1-4)

### Semana 1 — Fundamentos ESP32 y PWM

- Instala VS Code + PlatformIO (evita el IDE de Arduino, aprenderás más).
- Programas básicos: parpadear LED, leer botón, comunicación serie.
- Entiende PWM a fondo: qué es el duty cycle, por qué un servo se controla con pulsos de 1-2 ms a 50 Hz. Genera las señales tú mismo con `ledcWrite` antes de usar librerías.
- Mueve tu primer servo SG90 con potenciómetro.
- **Entregable:** servo que sigue la posición de un potenciómetro.

### Semana 2 — Montaje y control de múltiples servos

- Monta la torreta pan-tilt (~30 min) y aprovecha el tiempo ganado en el software.
- Alimentación correcta: servos a la fuente 5V, ESP32 por USB, **masas comunes**. Este es el error nº1 de todo el mundo.
- Controla los 2 ejes a la vez. Añade movimiento suavizado (interpolación entre posiciones, no saltos bruscos) y un modo "escaneo" automático.
- Extra: móntale el sensor ultrasónico del kit ELEGOO encima → radar que barre la habitación y mide distancias.
- **Entregable:** torreta que ejecuta secuencias suaves y escanea su entorno.

### Semana 3 — Cinemática y control remoto

- Cinemática: convierte coordenadas (x, y, z) de un punto de la habitación en ángulos pan/tilt (trigonometría aplicada de verdad). Estudia también la cinemática inversa de brazo 2-link: es la teoría que usarás cuando compres el brazo.
- Monta un servidor web en el ESP32 (WiFi) con sliders para controlar la torreta desde el móvil.
- **Entregable:** apuntar la torreta a coordenadas que escribes en el navegador.

### Semana 4 — API, documentación y DECISIÓN del brazo

- Añade una API HTTP limpia al ESP32: `POST /move {"pan":90,"tilt":45}`, `POST /sequence/scan`. Esto es lo que usará JARVIS después.
- Calibra límites de cada servo para no forzar el mecanismo.
- Sube todo a GitHub: README con fotos, vídeo corto, esquema de conexiones.
- **Decisión del brazo:** con 4 semanas de experiencia, elige entre imprimir el EEZYbotARM MK2, kit acrílico + MG90S, o Adeept (ver sección de compra). Pídelo ahora para tenerlo en la fase 2.
- **Entregable:** repo público documentado + torreta con API + brazo pedido (si sigues enganchado).

---

## FASE 2 — JARVIS (semanas 5-8)

### Semana 5 — Python y voz

- Si tu Python está flojo: 2-3 días intensivos (funciones, clases, pip, entornos virtuales).
- Reconocimiento de voz local con `faster-whisper` (gratis, funciona en tu PC) o la API de OpenAI/Groq si prefieres simplicidad.
- Síntesis de voz: `edge-tts` (gratis y suena bien en español).
- **Entregable:** script que te escucha, transcribe y te responde hablando.

### Semana 6 — Cerebro con LLM

- Conecta un LLM por API (Claude, GPT o Groq con Llama, que tiene capa gratuita).
- Diseña el bucle: escuchar → transcribir → LLM decide → responder/actuar.
- Aprende *function calling*: el LLM no solo habla, devuelve acciones estructuradas (`{"accion":"encender_luz"}`).
- Palabra de activación ("Oye JARVIS") con `openwakeword` o detección simple de energía.
- **Entregable:** asistente de voz conversacional con personalidad (el prompt de sistema es tuyo: hazlo sarcástico como JARVIS).

### Semana 7 — Domótica real

- El mismo ESP32 del brazo + relé: enciende/apaga una lámpara o tira LED vía HTTP o MQTT (instala Mosquitto; MQTT es el estándar en IoT industrial y te servirá profesionalmente).
- Integra: "JARVIS, enciende la luz" → función → MQTT → relé.
- Añade 2-3 habilidades más: hora, tiempo (API meteorológica), temporizadores.
- **Entregable:** controlar la luz de tu cuarto por voz.

### Semana 8 — Integración final: el momento Stark

- Conecta JARVIS con la API de la semana 4: "JARVIS, escanea la habitación" → la torreta barre; si ya montaste el brazo, "JARVIS, coge el objeto" → secuencia del brazo.
- Pule la latencia, maneja errores (WiFi caído, no entendió el comando).
- Documenta en GitHub, graba un vídeo de demo de 1-2 min. Súbelo a LinkedIn: proyectos así generan contactos reales.
- **Entregable:** demo en vídeo del sistema completo controlado por voz.

---

## Reglas del plan

1. **Monta antes de leer.** Máximo 30 min de teoría antes de tocar hardware cada día.
2. **Si te atascas >1 h, simplifica el objetivo,** no abandones la semana.
3. **Commit diario en GitHub,** aunque sea pequeño. El historial es tu diario de aprendizaje.
4. **No cambies de proyecto a mitad.** Las ideas nuevas van a una lista para después.

## Recursos recomendados

- ESP32: documentación de Random Nerd Tutorials (web, gratis, excelente).
- PlatformIO: docs oficiales + primer proyecto guiado.
- Cinemática inversa: busca "2 link arm inverse kinematics" (vídeos cortos, la matemática es asequible).
- MQTT: tutorial de HiveMQ "MQTT Essentials".
- Whisper/faster-whisper y edge-tts: READMEs de sus repos en GitHub.

**Qué habrás ganado al final:** sistemas embebidos reales (PWM, WiFi, APIs en microcontrolador), electrónica práctica (alimentación, relés, servos), Python sólido, integración con IA, MQTT/IoT, y dos repos documentados en GitHub. Eso ya es un perfil que destaca al terminar la carrera.
