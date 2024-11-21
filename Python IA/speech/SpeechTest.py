import pyttsx3

# Inicializar o sintetizador de voz
engine = pyttsx3.init()

# Configurando a velocidade e o volume da fala:
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

# Definir a língua como português
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
    
engine.setProperty('voice', voices[1].id)

engine.say("Olá, tudo bem?")
engine.runAndWait()

# Encerrar o sintetizador de voz
engine.stop()
