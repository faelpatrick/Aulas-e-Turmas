import speech_recognition as sr
import pyttsx3

# Inicializar o reconhecedor
recognizer = sr.Recognizer()

# Inicializar o sintetizador de voz
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    print("Escutando...")
    while True:
        try:
            with sr.Microphone(device_index=2) as source:
                recognizer.adjust_for_ambient_noise(source)  # Ajustar ruído ambiente
                print("Aguardando palavra-chave...")
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language="pt-PT").lower()  # Reconhece texto
                print(f"Você disse: {text}")

                # Responder à palavra-chave de início
                if start_keyword in text:
                    print("Palavra-chave detectada.")
                    speak("Estou aqui, como posso ajudar?")

                # Encerrar o programa com a palavra-chave de fim
                elif stop_keyword in text:
                    print("Palavra-chave detectada. Encerrando...")
                    speak("Até mais!")
                    break
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
        except sr.RequestError as e:
            print(f"Erro ao conectar ao serviço de reconhecimento: {e}")

# Definir as palavras-chave
start_keyword = "olá jarvis"
stop_keyword = "muito obrigado"

# Executar o programa
if __name__ == "__main__":
    speak(f"Diga {start_keyword} para começar ou {stop_keyword} para finalizar.")
    listen()
