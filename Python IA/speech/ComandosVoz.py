# Instale as bibliotecas necessárias:
# py -m pip install pyttsx3
# py -m pip install SpeechRecognition
# py -m pip install pyautogui

import pyttsx3
import speech_recognition as sr
import pyautogui
import datetime

# Configurando o pyttsx3 para falar
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Velocidade da fala
engine.setProperty('volume', 1)  # Volume da voz

voices = engine.getProperty("voices") # buscar as voces disponiveis
engine.setProperty("voice", voices[1].id) # selecionar uma voz

def falar(texto): # Função para falar
    engine.say(texto) # Fala o texto recebido como parametro(texto)
    engine.runAndWait()

def reconhecer_fala():
    """Reconhece a fala do usuário e retorna o texto."""
    reconhecedor = sr.Recognizer()
    with sr.Microphone() as source: # se mic não funcionar, troque para sr.Microphone(device_index=1)
        falar("Estou a ouvir...")
        try:
            audio = reconhecedor.listen(source, timeout=5, phrase_time_limit=5)
            comando = reconhecedor.recognize_google(audio, language="pt-BR")
            return comando.lower() # Retornar o comando em letras minusculas usando o .lower
        except sr.UnknownValueError: # função do sr que identifica o erro de reconhecimento
            falar("Desculpe, não entendi.")
        except sr.RequestError:  # função do sr que identifica o erro de requisição
            falar("Erro no serviço de reconhecimento de fala.")
        except sr.WaitTimeoutError: # função do sr que identifica o erro de timeout
            falar("Nenhum som detectado.")
    return ""

def executar_comando(comando): # Função para executar os comandos
    """Executa os comandos baseados na entrada de voz."""
    if "horas" in comando: # Se o comando contém a palavra "horas"
        now = datetime.datetime.now().strftime("%H:%M")
        falar(f"Agora são {now}.")
    elif "abrir" in comando: # Se o comando contém a palavra "abrir"
        falar("Abrindo.")
        pyautogui.hotkey("win", "r")
    else: # Se o comando for desconhecido
        falar("Comando não reconhecido.")

def start(): # Função para iniciar o programa
    """Loop principal para escutar e executar comandos."""
    falar("Olá! Estou pronto para ouvir seus comandos.")
    while True: # Loop infinito inicia o programa até dizer sair
        comando = reconhecer_fala()
        if "sair" in comando:
            falar("Encerrando o programa. Até logo!")
            break
        executar_comando(comando)

start() # Iniciar o programa
