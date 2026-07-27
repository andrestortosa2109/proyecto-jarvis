// SEMANA 0 — Servo controlado con PWM "a mano" (sin librerías)
// Pruébalo en wokwi.com: New Project → ESP32, añade un Servo al diagrama
// y conecta: servo signal → GPIO 18, V+ → 5V, GND → GND
//
// La gracia: NO usamos la librería Servo. Generamos nosotros la señal
// de 50 Hz con pulsos de 0.5-2.5 ms. Así entiendes QUÉ es un servo.

const int PIN_SERVO = 18;
const int PIN_POTE = 34;
const int FRECUENCIA = 50;     // 50 Hz = un pulso cada 20 ms (estándar servo)
const int RESOLUCION = 16;     // 16 bits → valores de 0 a 65535

// Convierte un ángulo (0-180°) al "duty" que genera el pulso correcto.
// 0°   → pulso de 0.5 ms → duty = (0.5/20) * 65535 ≈ 1638
// 180° → pulso de 2.5 ms → duty = (2.5/20) * 65535 ≈ 8192
int anguloADuty(int angulo) {
  float ms = 0.5 + (angulo / 180.0) * 2.0;   // 0.5 a 2.5 ms
  return (int)((ms / 20.0) * 65535.0);
}

void setup() {
  Serial.begin(115200);
  // API nueva del core ESP32 v3.x: ledcAttach asocia el PWM al PIN
  // (ya no a un número de canal manual como en versiones antiguas).
  ledcAttach(PIN_SERVO, FRECUENCIA, RESOLUCION);
  Serial.println("Servo listo. Reto del potenciometro: RETO SEMANA 0 completado.");
}

// RETO SEMANA 0 (entregable de la semana 1): control en lazo directo.
// El potenciómetro en GPIO 34 manda directamente el ángulo del servo.
void loop() {
  int lectura = analogRead(PIN_POTE);
  int ang = map(lectura, 0, 4095, 0, 180);
  // IMPORTANTE: en la API nueva, ledcWrite también recibe el PIN (no el
  // canal) como primer argumento — de ahí venía el bug de que el servo
  // no se movía aunque `ang` calculara bien.
  ledcWrite(PIN_SERVO, anguloADuty(ang));
  delay(20);
}
