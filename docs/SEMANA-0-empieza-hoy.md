# Semana 0 — Empieza hoy, sin hardware

Todo esto se hace con tu PC. Cuando llegue el material, ya sabrás moverte.

## Día 1-2: Entorno

- [ ] Instala **VS Code** (code.visualstudio.com) y dentro la extensión **PlatformIO IDE**
- [ ] Instala **Python 3.12** (python.org) — marca "Add to PATH" en el instalador
- [ ] Instala **Git** (git-scm.com) y crea cuenta en **github.com** si no la tienes
- [ ] Crea tu primer repo: `proyecto-jarvis` (público, con README)

## Día 2-4: ESP32 simulado en Wokwi

**Wokwi** (wokwi.com) simula un ESP32 real en el navegador, gratis. El código que escribas ahí funcionará idéntico en tu placa física.

- [ ] Entra en wokwi.com → New Project → ESP32
- [ ] Haz el clásico: LED parpadeando (busca "blink" en sus ejemplos)
- [ ] Añade un servo al diagrama (botón + → Servo) y pega el código de `01-brazo-robotico/firmware/semana0_servo_wokwi.cpp`
- [ ] Reto: añade un potenciómetro y haz que el servo siga su posición → **eso es el entregable de la semana 1, conseguido antes de tener la placa**

## Día 4-7: La voz de JARVIS con el micro de tu PC

Tu portátil/webcam ya tiene micrófono — el USB comprado será mejora, no requisito.

- [ ] Abre terminal en `02-jarvis/src` y ejecuta:
  ```
  pip install faster-whisper edge-tts sounddevice soundfile
  ```
- [ ] Ejecuta `python jarvis_v0.py` — te graba 5 segundos, transcribe lo que dijiste y te responde hablando
- [ ] Reto: cambia la respuesta fija por un eco con personalidad ("Ha dicho usted: ...")

## Extra si te sobra energía

- Curso relámpago de Git: aprende `add`, `commit`, `push` (30 min, cualquier tutorial)
- Lee "ESP32 PWM" en Random Nerd Tutorials — es la teoría de la semana 1
- Pide ya el material si no lo has hecho: AliExpress tarda 2-3 semanas

**Regla de la semana 0:** no es estudiar, es dejar cosas FUNCIONANDO. Si el viernes tienes un servo virtual moviéndose y un script que te escucha, vas por delante del plan.
