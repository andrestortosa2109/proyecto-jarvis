# Proyecto JARVIS 🤖

Brazo robótico controlado por voz + asistente estilo JARVIS, construido desde cero en un verano con ESP32 y Python. Presupuesto: <100 €.

## Qué hace (objetivo semana 8)

> "JARVIS, escanea la habitación" → la torreta pan-tilt barre el cuarto con su sensor ultrasónico.
> "JARVIS, enciende la luz" → un relé conmuta la lámpara.

Voz → PC (Whisper + LLM) → WiFi (HTTP/MQTT) → ESP32 → servos y relé.

## Estructura

- `01-brazo-robotico/` — firmware del ESP32 (C++/PlatformIO): PWM, cinemática, API HTTP
- `02-jarvis/` — el asistente en Python: reconocimiento de voz, LLM con function calling, síntesis de voz
- `docs/` — plan de 8 semanas y guías paso a paso

## Estado

- [x] Semana 0: entorno montado (VS Code, PlatformIO, Python, Git), servo simulado en Wokwi, JARVIS v0 escucha y responde
- [ ] Semana 1: PWM a fondo — servo real siguiendo un potenciómetro
- [ ] Semana 2: torreta pan-tilt con movimiento suavizado y modo escaneo
- [ ] Semana 3: cinemática + control desde el navegador
- [ ] Semana 4: API HTTP + decisión del brazo definitivo
- [ ] Semana 5: voz→texto→voz completo
- [ ] Semana 6: cerebro LLM con function calling
- [ ] Semana 7: domótica real (relé + MQTT)
- [ ] Semana 8: integración final — control por voz de todo

## Stack

ESP32 (C++, PlatformIO) · Python 3.14 · faster-whisper · edge-tts · MQTT (Mosquitto) · Wokwi para simulación

---

*Proyecto de aprendizaje de un estudiante de Ingeniería Electrónica Industrial. Documentado commit a commit.*
