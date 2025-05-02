
import cv2
import mediapipe as mp
import pyautogui
import time

mp_mao = mp.solutions.hands.Hands(max_num_hands=1)
desenho = mp.solutions.drawing_utils
ultimo_gesto = ""
tempo_ultimo = 0

def detectar_gesto(pontos):
    if not pontos:
        return None

    polegar = pontos[4]
    indicador = pontos[8]
    centro = pontos[5]  # base do indicador (referência central da mão)

    # Verificar se o polegar está mais na vertical (mudança em y) ou horizontal (mudança em x)
    orientacao = "vertical" if abs(polegar.y - centro.y) > abs(polegar.x - centro.x) else "horizontal"

    if orientacao == "vertical":
        if polegar.y < centro.y:
            return "volume_mais"
        elif polegar.y > centro.y:
            return "volume_menos"
    else:  # horizontal
        if indicador.y < pontos[6].y:  # indicador levantado
            return "play_pause"
        elif polegar.x > centro.x:
            return "faixa_proxima"
        elif polegar.x < centro.x:
            return "faixa_anterior"

    return None

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
            pontos = mao.landmark
            gesto = detectar_gesto(pontos)
            agora = time.time()

            if gesto and ((gesto != ultimo_gesto and agora - tempo_ultimo > 5) or agora - tempo_ultimo > 1.5):
                if gesto == "volume_mais":
                    pyautogui.press("volumeup", 6)
                    print("🔊 Polegar para cima → Volume +")
                elif gesto == "volume_menos":
                    pyautogui.press("volumedown", 6)
                    print("🔉 Polegar para baixo → Volume -")
                elif gesto == "faixa_anterior":
                    pyautogui.press("prevtrack")
                    print("⏮️ Polegar para esquerda → Faixa anterior")
                elif gesto == "faixa_proxima":
                    pyautogui.press("nexttrack")
                    print("⏭️ Polegar para direita → Próxima faixa")
                elif gesto == "play_pause":
                    pyautogui.press("playpause")
                    print("⏯️ Indicador levantado + polegar na horizontal → Play/Pause")

                ultimo_gesto = gesto
                tempo_ultimo = agora

    cv2.imshow("Player com Gestos - Refatorado", frame)
    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()
