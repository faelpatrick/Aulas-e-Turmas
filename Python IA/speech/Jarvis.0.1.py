import speech_recognition as sr
import pyttsx3
import pyautogui
from datetime import datetime
from time import sleep

# Inicializar o reconhecedor
recognizer = sr.Recognizer()

# Inicializar o sintetizador de voz
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def acoes(acao):
    # switch for acoes Horas, abrir x, responder x
    if "horas" in acao:
        now = datetime.now().strftime("%H:%M")
        speak(f"São: {now}")
    elif "abrir" in acao:
        speak(f"Abrindo... {acao}")
        pyautogui.hotkey("win", "r")
        sleep(1)
        acao = acao.replace("abrir ", "")
        pyautogui.write(acao)
        sleep(1)
        pyautogui.press("enter")
    else:
        speak("Desculpe, não entendi o comando.")


def listen(start_keyword, stop_keyword, callback):
    print("Escutando...")
    while True:
        try:
            with sr.Microphone(device_index=2) as source:
                recognizer.adjust_for_ambient_noise(source)  # Ajustar ruído ambiente
                print("Aguardando palavra-chave...")
                audio = recognizer.listen(source)

                text = recognizer.recognize_google(audio, language="pt-PT").lower()
                print(f"Você disse: {text}")

                # Responder à palavra-chave de início
                if start_keyword in text:
                    print("Palavra-chave detectada.")
                    acao = text.replace(start_keyword, "").strip()
                    print(f"O que deseja: {acao}")

                    # Executar o programa principal
                    acoes(acao)

                # Encerrar o programa com a palavra-chave de fim
                elif stop_keyword in text:
                    print("Disponha. Encerrando...")
                    speak("Até mais!")
                    break
        except sr.UnknownValueError:
            print("Não entendi o que você disse.")
        except sr.RequestError as e:
            print(f"Erro ao conectar ao serviço de reconhecimento: {e}")


# Definir as palavras-chave
start_keyword = "ok google"
stop_keyword = "muito obrigado"

# Executar o programa
if __name__ == "__main__":
    speak(f"Diga {start_keyword} para começar ou {stop_keyword} para finalizar.")
    listen(start_keyword, stop_keyword, acoes)
