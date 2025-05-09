# Detector de Distrações - Foco no Estudo

Este projeto é um detector de distrações que utiliza a webcam para verificar se a pessoa está olhando para a tela.  
Se os olhos não forem detectados por mais de 2 segundos, um alerta sonoro é emitido e uma mensagem aparece no console.

---

## 🛠️ **Funcionalidades do Projeto**
- Detecta os olhos do usuário em tempo real usando a câmera.
- Emite um alerta sonoro caso os olhos saiam da tela por mais de 2 segundos.
- Exibe os pontos dos olhos em verde para facilitar a visualização.

---

## 🚀 **Como Funciona?**
1. O programa inicia a câmera do computador.
2. Utiliza o **MediaPipe** para identificar pontos específicos do rosto, como os olhos.
3. Marca os pontos dos olhos em verde na tela.
4. Se os olhos desaparecerem por mais de 2 segundos, toca um som de alerta.
5. O processo se repete até que a câmera seja desligada.

---

## 📌 **Código Explicado Passo a Passo**

### 1️⃣ Captura de Vídeo
```python
cam = cv2.VideoCapture(0)
```
- Captura o vídeo da câmera em tempo real.

---

### 2️⃣ Detecta os pontos do rosto
```python
resultado = face_mesh.process(rgb)
```
- O MediaPipe identifica os pontos do rosto, incluindo os olhos.

---

### 3️⃣ Desenha os pontos dos olhos na tela
```python
for i in [33, 133, 362, 263]:  # Esses números representam os pontos nos olhos
    ponto = face_landmarks.landmark[i]
    h, w, _ = frame.shape
    x, y = int(ponto.x * w), int(ponto.y * h)
    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
```
- São desenhados pequenos círculos verdes nos olhos.

---

### 4️⃣ Contagem do tempo sem detectar os olhos
```python
if time.time() - tempo_ausente > TEMPO_LIMITE:
    print("⚠️ Atenção! Olhos não detectados por mais de 2 segundos!")
    winsound.Beep(1000, 500)
```
- Caso os olhos desapareçam por mais de 2 segundos, um som é emitido.

---

## ▶️ **Como Executar o Projeto**
1. Clone ou baixe o projeto para o seu computador.
2. Abra o terminal (CMD) no diretório do projeto.
3. Instale as dependências necessárias:
    ```bash
    pip install opencv-python mediapipe
    ```
4. Execute o projeto:
    ```bash
    python nome_do_arquivo.py
    ```

---

## 💡 **Melhorias Futuras**
- Adicionar um contador de distrações.
- Exibir um alerta visual na tela.
- Integrar com um cronômetro de estudos.

---

Projeto desenvolvido para aulas práticas de visão computacional.
