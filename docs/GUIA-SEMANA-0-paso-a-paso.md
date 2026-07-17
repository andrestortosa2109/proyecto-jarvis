# Guía Semana 0 — Paso a paso desde cero

Esta guía te deja tres cosas funcionando antes de que llegue el material: el entorno de programación, un servo simulado moviéndose con tu código, y un JARVIS v0 que te escucha y responde. Cada paso dice qué hacer, dónde pulsar y por qué.

**Orden importante:** los pasos 1-4 son instalaciones (una tarde). Los pasos 5-6 son los divertidos. No saltes al 5 sin el 1-2, ni al 6 sin el 3.

---

## PASO 1 — Instalar VS Code (15 min)

**Por qué:** VS Code es el editor donde escribirás todo el código del proyecto, tanto el del ESP32 (C++) como el de JARVIS (Python). Es gratuito, es el estándar de la industria, y lo usarás el resto de tu carrera.

1. Ve a **code.visualstudio.com** y pulsa el botón azul **Download for Windows**.
2. Ejecuta el instalador descargado. Acepta la licencia y pulsa **Siguiente** en todo, PERO en la pantalla "Tareas adicionales" marca estas casillas si no lo están:
   - "Agregar la acción 'Abrir con Code' al menú contextual de archivo" → te permitirá abrir cualquier carpeta con clic derecho.
   - "Agregar a PATH" → permite abrir VS Code desde la terminal escribiendo `code`.
3. Pulsa **Instalar** y al terminar, **Finalizar** (se abrirá VS Code).
4. Opcional pero recomendado: VS Code está en inglés. Si lo quieres en español, pulsa `Ctrl+Shift+X` (abre el panel de extensiones), busca "Spanish Language Pack", pulsa **Install** y reinicia cuando lo pida.

**Comprobación:** VS Code abierto con su pantalla de bienvenida.

---

## PASO 2 — Instalar PlatformIO dentro de VS Code (15 min)

**Por qué:** PlatformIO es la herramienta que compila tu código C++ y lo carga en el ESP32. Usamos esto en vez del IDE de Arduino porque gestiona librerías y placas de forma profesional, y porque el flujo de trabajo (proyectos con configuración explícita en un archivo `platformio.ini`) es el mismo que verás en la industria de sistemas embebidos.

1. En VS Code, pulsa `Ctrl+Shift+X` (icono de cuadraditos en la barra izquierda: panel de extensiones).
2. En el buscador de arriba escribe **PlatformIO IDE**.
3. Pulsa **Install** en el primer resultado (el del logo de la hormiga alienígena). 
4. **Paciencia:** la primera instalación descarga bastantes cosas (2-5 min con barra de progreso abajo a la derecha). No cierres VS Code.
5. Cuando termine, pedirá reiniciar VS Code: hazlo. Verás un icono nuevo de hormiga en la barra izquierda y una casita (PlatformIO Home) en la barra inferior azul.

**Comprobación:** icono de la hormiga visible en la barra lateral izquierda.

**Nota:** hoy no crearás ningún proyecto aquí — el paso 5 usa el simulador web. PlatformIO queda listo para cuando llegue la placa física.

---

## PASO 3 — Instalar Python (15 min)

**Por qué:** JARVIS vivirá en tu PC y estará escrito en Python: el lenguaje con mejores librerías de IA (reconocimiento de voz, síntesis, conexión con LLMs) y el segundo idioma de todo ingeniero hoy.

1. Ve a **python.org/downloads** y pulsa el botón amarillo **Download Python 3.12.x**.
2. Ejecuta el instalador. **ATENCIÓN — el paso más importante de toda la guía:** en la primera pantalla, abajo, marca la casilla **"Add python.exe to PATH"** antes de pulsar nada.
   - *Por qué:* el PATH es la lista de sitios donde Windows busca programas cuando escribes un comando en la terminal. Sin esta casilla, escribir `python` en la terminal dará "no se reconoce como comando" y tendrás que arreglarlo a mano.
3. Pulsa **Install Now** y espera. Cierra al terminar.
4. **Comprobación:** pulsa la tecla Windows, escribe `powershell`, ábrelo, y escribe:
   ```
   python --version
   ```
   Debe responder algo como `Python 3.12.7`. Escribe también `pip --version` (pip es el instalador de librerías de Python; debe responder con una versión).

**Si falla** ("python no se reconoce..."): desinstala Python desde Configuración → Aplicaciones, y reinstala marcando la casilla del PATH.

---

## PASO 4 — Git y GitHub (30 min)

**Por qué:** Git guarda "fotografías" (commits) de tu código en cada momento: puedes volver atrás cuando rompas algo, y GitHub las publica online. Tu GitHub será tu portfolio: cuando busques prácticas o trabajo, es lo primero que mirará un buen empleador. Empezar a usarlo desde el día 1 es de las decisiones más rentables del proyecto.

### 4a. Instalar Git

1. Ve a **git-scm.com/downloads** → Windows → "64-bit Git for Windows Setup".
2. Ejecuta el instalador. Tiene MUCHAS pantallas de opciones: pulsa **Next** en todas (los valores por defecto son correctos) e **Install** al final.
3. Comprobación en PowerShell: `git --version` → debe responder con una versión.

### 4b. Cuenta y configuración

1. Crea cuenta en **github.com** (botón Sign up) con tu email. Elige un nombre de usuario presentable — lo verán empleadores.
2. Preséntate a Git en PowerShell (esto firma tus commits):
   ```
   git config --global user.name "Tu Nombre"
   git config --global user.email "tuemail@ejemplo.com"
   ```

### 4c. Tu primer repositorio

1. En github.com pulsa el botón verde **New** (o el "+" arriba a la derecha → New repository).
2. Repository name: `proyecto-jarvis`. Déjalo en **Public** (es tu portfolio). Marca **Add a README file**. Pulsa **Create repository**.
3. Clónalo (descárgalo enlazado) a tu PC. En PowerShell:
   ```
   cd Desktop
   git clone https://github.com/TU_USUARIO/proyecto-jarvis.git
   ```
   (Sustituye TU_USUARIO por tu nombre de usuario. La primera vez, GitHub te pedirá iniciar sesión en una ventana del navegador.)
4. El ciclo que repetirás siempre — memorízalo como respirar:
   ```
   git add .                          ← prepara TODOS los cambios
   git commit -m "qué he hecho"       ← fotografía con descripción
   git push                           ← súbela a GitHub
   ```
   *Por qué así:* `add` elige qué entra en la foto, `commit` la toma (queda en tu PC), `push` la publica. Un commit al final de cada sesión de trabajo es el hábito.

**Comprobación:** edita el README.md del repo (con VS Code), haz el ciclo add/commit/push, recarga la página de GitHub y verás tu cambio online.

---

## PASO 5 — Tu primer servo, simulado en Wokwi (1-2 h)

**Por qué:** Wokwi (wokwi.com) es un simulador de ESP32 que corre en el navegador, gratis. Ejecuta tu código C++ real sobre una placa virtual con componentes virtuales. Todo lo que hagas aquí funcionará idéntico en tu placa física — es la máquina del tiempo que te deja empezar la semana 1 hoy.

### 5a. Crear el proyecto

1. Ve a **wokwi.com** y crea cuenta (Sign up, puedes usar la de GitHub — así se enlazan).
2. Pulsa **+ New Project** y elige **ESP32** (el primero, a secas).
3. Verás dos paneles: izquierda el **código** (`sketch.ino`), derecha el **diagrama** (la placa dibujada).

### 5b. Añadir el servo y cablearlo

1. En el panel del diagrama, pulsa el botón **+** (arriba). Busca y elige **Servo**.
2. Aparece el servo. Arrástralo a un lado de la placa.
3. Cablea haciendo clic en un pin y luego en su destino (se dibuja un cable):
   - **PWM** del servo (naranja) → pin **18** del ESP32. *Por qué el 18: es un GPIO libre cualquiera; en el código le decimos al ESP32 que genere la señal ahí.*
   - **V+** del servo (rojo) → **5V** del ESP32. *En el simulador no hay problema de corriente; en la realidad esto iría a la fuente externa — recuerda las reglas de seguridad.*
   - **GND** del servo (marrón) → **GND** del ESP32. *La masa común: sin referencia compartida, la señal PWM no significa nada.*

### 5c. El código

1. Borra todo el contenido de `sketch.ino` y pega el código del archivo **`01-brazo-robotico/firmware/semana0_servo_wokwi.cpp`** de tu carpeta (ábrelo con VS Code, Ctrl+A, Ctrl+C).
2. Pulsa el botón verde **▶ (play)** arriba del diagrama.
3. **Qué debes ver:** el servo barriendo de 0° a 180° y de vuelta, suavemente, para siempre. Abajo, el monitor serie dice "Servo listo...".
4. **Léete el código con calma** — está comentado línea a línea. La idea central: no usamos librería de servo; generamos nosotros la señal de 50 Hz calculando el ancho de pulso. Cuando entiendas la función `anguloADuty()`, has entendido qué es un servo.

### 5d. El reto (el entregable de la semana 1)

1. Añade con **+** un **Potentiometer** al diagrama.
2. Cablea: patilla central (SIG) → pin **34** del ESP32; una lateral → 3V3; la otra → GND. *Por qué el 34: es un pin solo-entrada con conversor analógico-digital (ADC); el ESP32 leerá 0-4095 según giras la rueda.*
3. En el código, sustituye todo el `loop()` por:
   ```cpp
   void loop() {
     int ang = map(analogRead(34), 0, 4095, 0, 180);
     ledcWrite(CANAL_PWM, anguloADuty(ang));
     delay(20);
   }
   ```
   *Qué hace `map()`: regla de tres — convierte el rango del ADC (0-4095) al rango del servo (0-180).*
4. Dale a play y gira el potenciómetro con el ratón: el servo debe seguirte. **Eso es control en lazo directo, y es el entregable de la semana 1. Hecho sin placa.**
5. Guarda el proyecto (Save) y copia el código final a tu repo `proyecto-jarvis` → add/commit/push. Primer commit con chicha.

---

## PASO 6 — JARVIS v0 con el micro de tu PC (1 h)

**Por qué:** el micrófono USB comprado será una mejora, no un requisito: tu portátil o webcam ya tienen micro. Este paso deja funcionando el esqueleto voz→texto→respuesta→voz que en la semana 6 conectaremos a un LLM.

1. **Permiso de micrófono:** tecla Windows → "Configuración de privacidad del micrófono" → activa "Acceso al micrófono" y "Permitir que las aplicaciones de escritorio accedan".
2. Abre PowerShell **en la carpeta del proyecto**: abre el Explorador, entra en `PROYECTO IRON MAN\02-jarvis\src`, y en la barra de direcciones escribe `powershell` y Enter. *(Truco: eso abre la terminal ya situada ahí, sin pelearte con `cd`.)*
3. Instala las librerías:
   ```
   pip install faster-whisper edge-tts sounddevice soundfile
   ```
   *Qué es cada una: faster-whisper = voz→texto local (el modelo de OpenAI corriendo en TU PC, gratis y privado); edge-tts = texto→voz de Microsoft (gratis, suena natural en español); sounddevice/soundfile = grabar y guardar audio.*
4. Ejecuta:
   ```
   python jarvis_v0.py
   ```
5. **La primera vez tardará:** descarga el modelo Whisper (~500 MB). Es solo la primera vez.
6. Cuando diga "Hable ahora", di una frase. Debe imprimir lo que dijiste y **responderte con voz**.

**Problemas típicos:**

| Síntoma | Causa y arreglo |
|---|---|
| `pip no se reconoce...` | Python sin PATH → reinstala (Paso 3) |
| Transcribe vacío | Micrófono equivocado → Configuración → Sonido → elige el micro correcto como predeterminado |
| Va muy lento | Cambia `"small"` por `"base"` en la línea del modelo (menos preciso, mucho más rápido) |
| No suena la respuesta | Abre manualmente el mp3 que indica la ruta temporal; si existe, es solo el reproductor — dímelo y lo ajustamos |

7. **El reto:** abre `jarvis_v0.py` en VS Code y modifica la función `pensar()` — dale personalidad a las respuestas. Ese es exactamente el lugar donde en la semana 6 enchufaremos el cerebro LLM.

---

## Checklist del viernes

- [ ] VS Code + PlatformIO instalados (hormiga visible)
- [ ] `python --version` y `git --version` responden en PowerShell
- [ ] Repo `proyecto-jarvis` en GitHub con al menos 2 commits
- [ ] Servo virtual siguiendo al potenciómetro en Wokwi (entregable semana 1 ✓)
- [ ] JARVIS v0 te ha escuchado y respondido con voz

Si tienes las cinco, vas por delante del plan sin haber gastado un euro. Cualquier error en cualquier paso: cópialo y tráemelo, lo resolvemos juntos.
