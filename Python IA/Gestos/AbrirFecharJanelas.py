import cv2
import mediapipe as mp
import pyautogui
import time

# Inicializar MediaPipe
mp_mao = mp.solutions.hands.Hands(max_num_hands=2)
desenho = mp.solutions.drawing_utils
ultimo_gesto = ""
tempo_ultimo = 0
janelas_visiveis = True  # Flag para controlar estado

# Contar dedos para ambas as mãos)
def contar_dedos(pontos):
    dedos = 0
    if pontos[8].y < pontos[6].y: dedos += 1
    if pontos[12].y < pontos[10].y: dedos += 1
    if pontos[16].y < pontos[14].y: dedos += 1
    if pontos[20].y < pontos[18].y: dedos += 1
    if abs(pontos[4].x - pontos[2].x) > 0.1: dedos += 1
    return dedos

# Iniciar câmera
cam = cv2.VideoCapture(0)

while True:
    ok, frame = cam.read()
    if not ok:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = mp_mao.process(rgb)

    if resultado.multi_hand_landmarks:
        for mao in resultado.multi_hand_landmarks:
            desenho.draw_landmarks(frame, mao, mp.solutions.hands.HAND_CONNECTIONS)
            dedos = contar_dedos(mao.landmark)
            agora = time.time()

            if dedos == 0 and (ultimo_gesto != "fechada" or agora - tempo_ultimo > 2):
                if janelas_visiveis:
                    pyautogui.hotkey("win", "d")
                    print("🖥️ Mostrar Área de Trabalho")
                    janelas_visiveis = False
                    tempo_ultimo = agora
                    ultimo_gesto = "fechada"

            elif dedos == 5 and (ultimo_gesto != "aberta" or agora - tempo_ultimo > 2):
                if not janelas_visiveis:
                    pyautogui.hotkey("win", "d")
                    print("🔄 Restaurar Janelas")
                    janelas_visiveis = True
                    tempo_ultimo = agora
                    ultimo_gesto = "aberta"

    cv2.imshow("Gestos com a Mão", frame)
    if cv2.waitKey(1) == 27:  # ESC para sair
        break

cam.release()
cv2.destroyAllWindows()
