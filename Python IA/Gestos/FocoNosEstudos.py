# ✅ Importar as bibliotecas necessárias
import cv2                     # Biblioteca para capturar vídeo e manipular imagens
import mediapipe as mp         # Biblioteca para detectar pontos do rosto
import time                    # Biblioteca para contar o tempo
import winsound                # Biblioteca para tocar som no Windows

# 🔴 Definimos um limite de tempo (em segundos) para acionar o alerta se os olhos não forem detectados
TEMPO_LIMITE = 2  

# ✅ Inicialização do detector de rosto do MediaPipe
mp_face_mesh = mp.solutions.face_mesh  # Carregando o modelo de detecção de rosto
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5)  # Definindo a confiança mínima para detectar

# ✅ Variáveis de controle para saber se os olhos estão sendo detectados e contar o tempo
tempo_ausente = 0            # Vai armazenar o tempo em que os olhos não foram detectados
olhos_detectados = True      # Estado inicial, assumindo que os olhos estão na tela

# ✅ Captura de vídeo da webcam (0 significa a câmera principal do computador)
cam = cv2.VideoCapture(0)

# ✅ Loop infinito para capturar os frames da câmera
while True:
    ok, frame = cam.read()   # Captura cada frame da câmera
    if not ok:               # Se não conseguir capturar, ele sai do loop
        break

    # ✅ Espelhar a imagem para ficar mais intuitivo
    frame = cv2.flip(frame, 1)

    # ✅ Converter a imagem para RGB, pois o MediaPipe trabalha com esse formato
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # ✅ Detectar os pontos do rosto usando o MediaPipe
    resultado = face_mesh.process(rgb)

    # ✅ Se detectar um rosto, ele entra neste bloco
    if resultado.multi_face_landmarks:
        for face_landmarks in resultado.multi_face_landmarks:
            # ✅ Desenhar pequenos círculos nos pontos que representam os olhos
            for i in [33, 133, 362, 263]:  # Esses números representam os pontos nos olhos
                ponto = face_landmarks.landmark[i]    # Pegando as coordenadas do ponto
                h, w, _ = frame.shape                 # Pegando altura e largura do frame
                x, y = int(ponto.x * w), int(ponto.y * h)  # Convertendo para coordenadas da tela
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)  # Desenhar o ponto na tela

        # ✅ Quando os olhos são detectados, o tempo é reiniciado
        olhos_detectados = True
        tempo_ausente = time.time()  # Armazena o tempo em que os olhos foram detectados
    else:
        if olhos_detectados:
            # ✅ Se os olhos pararam de ser detectados, ele marca o tempo atual
            olhos_detectados = False
            tempo_ausente = time.time()
        else:
            # ✅ Calcula o tempo sem detectar os olhos
            if time.time() - tempo_ausente > TEMPO_LIMITE:
                print("⚠️ Atenção! Olhos não detectados por mais de 2 segundos!")
                
                # ✅ Toca um som de alerta se os olhos não aparecem por 2 segundos
                winsound.Beep(1000, 500)  # Som de 1000Hz por 500ms
                tempo_ausente = time.time()  # Reinicia o tempo para não tocar várias vezes

    # ✅ Exibir o vídeo na tela
    cv2.imshow("Detecção de Olhos", frame)

    # ✅ Se pressionar ESC (27), o programa para
    if cv2.waitKey(1) == 27:
        break

# ✅ Fecha a câmera e a janela quando o loop é finalizado
cam.release()
cv2.destroyAllWindows()
