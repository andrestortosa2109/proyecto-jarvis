# Proyecto 1: Brazo robótico (semanas 1-4)

**Objetivo:** brazo 4DOF controlado por ESP32 con API HTTP, listo para integrarse con JARVIS.

## Estructura

- `firmware/` — código del ESP32 (PlatformIO)
- `docs/` — esquemas de conexión, fotos, notas de calibración

## Hitos

- [ ] S1: servo controlado con potenciómetro (PWM entendido)
- [ ] S2: brazo montado, 4 servos con movimiento suavizado
- [ ] S3: cinemática inversa 2D + control desde el navegador
- [ ] S4: API HTTP limpia + repo documentado en GitHub

## Notas de seguridad eléctrica

- Servos SIEMPRE a la fuente 5V externa, nunca al pin 5V del ESP32
- Masas comunes entre fuente y ESP32
- Calibrar límites de cada servo antes de secuencias automáticas
