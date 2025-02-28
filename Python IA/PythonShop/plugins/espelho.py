from PIL import Image

PLUGIN_NOME = "Espelho"
PLUGIN_ICONE = "🔁"

def aplicar(imagem):
    imagem_espelhada = imagem.transpose(Image.FLIP_LEFT_RIGHT)  # Espelha horizontalmente
    return imagem_espelhada
