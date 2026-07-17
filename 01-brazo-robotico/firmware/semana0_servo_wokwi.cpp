// SEMANA 0 — Servo controlado con PWM "a mano" (sin librerías)
// Pruébalo en wokwi.com: New Project → ESP32, añade un Servo al diagrama
// y conecta: servo signal → GPIO 18, V+ → 5V, GND → GND
//
// La gracia: NO usamos la librería Servo. Generamos nosotros la señal
// de 50 Hz con pulsos de 0.5-2.5 ms. Así entiendes QUÉ es un servo.

const int PIN_SERVO = 18;
const int CANAL_PWM = 0;       // el ESP32 tiene 16 canales PWM
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
  ledcSetup(CANAL_PWM, FRECUENCIA, RESOLUCION);
  ledcAttachPin(PIN_SERVO, CANAL_PWM);
  Serial.println("Servo listo. Barriendo 0-180 grados...");
}

void loop() {
  // Barrido suave de ida...
  for (int ang = 0; ang <= 180; ang += 2) {
    ledcWrite(CANAL_PWM, anguloADuty(ang));
    delay(20);
  }
  // ...y de vuelta
  for (int ang = 180; ang >= 0; ang -= 2) {
    ledcWrite(CANAL_PWM, anguloADuty(ang));
    delay(20);
  }
}

// RETO SEMANA 0: añade un potenciómetro en Wokwi (GPIO 34) y sustituye
// el barrido por:  int ang = map(analogRead(34), 0, 4095, 0, 180);
// Cuando lo tengas, ya has completado el entregable de la semana 1.
