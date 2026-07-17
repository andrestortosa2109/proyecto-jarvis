# Proyecto 2: JARVIS (semanas 5-8)

**Objetivo:** asistente de voz en el PC (Python) que controla luces por MQTT y el brazo robótico por HTTP.

## Estructura

- `src/` — código Python (voz, LLM, acciones)
- `docs/` — arquitectura, prompts, notas

## Hitos

- [ ] S5: escucha → transcribe (faster-whisper) → responde hablando (edge-tts)
- [ ] S6: LLM con function calling + palabra de activación "Oye JARVIS"
- [ ] S7: control de luz real vía ESP32 + relé (MQTT)
- [ ] S8: integración con el brazo + vídeo demo

## Stack

Python 3.11+, faster-whisper, edge-tts, API de LLM (Claude/Groq), paho-mqtt, Mosquitto
