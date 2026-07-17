"""
JARVIS v0 — te escucha, transcribe y responde hablando.
Funciona con el micrófono integrado de tu PC. Sin APIs de pago.

Instalación (una vez):
    pip install faster-whisper edge-tts sounddevice soundfile

Uso:
    python jarvis_v0.py
"""

import asyncio
import os
import tempfile

import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel

import edge_tts

SEGUNDOS_GRABACION = 5
FRECUENCIA_MUESTREO = 16000
VOZ = "es-ES-AlvaroNeural"  # prueba también: es-ES-ElviraNeural


def grabar() -> str:
    """Graba unos segundos de audio y devuelve la ruta del wav temporal."""
    print(f"🎙️  Hable ahora ({SEGUNDOS_GRABACION} s)...")
    audio = sd.rec(
        int(SEGUNDOS_GRABACION * FRECUENCIA_MUESTREO),
        samplerate=FRECUENCIA_MUESTREO,
        channels=1,
    )
    sd.wait()
    ruta = os.path.join(tempfile.gettempdir(), "jarvis_entrada.wav")
    sf.write(ruta, audio, FRECUENCIA_MUESTREO)
    return ruta


def transcribir(ruta_wav: str) -> str:
    """Convierte voz a texto con Whisper (local, gratis)."""
    print("🧠 Transcribiendo...")
    # 'small' equilibra velocidad y calidad. Si va lento, usa 'base'.
    modelo = WhisperModel("small", device="cpu", compute_type="int8")
    segmentos, _ = modelo.transcribe(ruta_wav, language="es")
    return " ".join(s.text.strip() for s in segmentos)


async def hablar(texto: str) -> None:
    """Convierte texto a voz y lo reproduce."""
    ruta = os.path.join(tempfile.gettempdir(), "jarvis_salida.mp3")
    await edge_tts.Communicate(texto, VOZ).save(ruta)
    # Reproducción multiplataforma sencilla:
    if os.name == "nt":
        os.system(f'start /min wmplayer "{ruta}"')  # Windows
    else:
        os.system(f'mpg123 "{ruta}" 2>/dev/null || afplay "{ruta}"')


def pensar(texto_usuario: str) -> str:
    """El 'cerebro' v0: respuesta fija. En la semana 6 aquí entrará el LLM."""
    if not texto_usuario.strip():
        return "No he oído nada, señor. ¿El micrófono funciona?"
    return f"Le he entendido perfectamente. Ha dicho: {texto_usuario}. Aún soy un JARVIS bebé, pero deme seis semanas."


if __name__ == "__main__":
    wav = grabar()
    texto = transcribir(wav)
    print(f"📝 Usted dijo: {texto}")
    respuesta = pensar(texto)
    print(f"🤖 JARVIS: {respuesta}")
    asyncio.run(hablar(respuesta))
