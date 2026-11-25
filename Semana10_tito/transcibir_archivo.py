import speech_recognition as sr
def procesar_transcripcion(texto):
    return texto.lower().strip()
r = sr.Recognizer()
with sr.AudioFile("becas_01.wav") as source:
    audio = r.record(source)
try:
    texto = r.recognize_google(audio, language="es-MX")
    print("Transcripción original:", texto)

    texto_limpio = procesar_transcripcion(texto)
    print("Transcripción limpia:", texto_limpio)
except sr.UnknownValueError:
    print("No se pudo entender el audio.")
except sr.RequestError as error:
    print("Error del servicio:", error)