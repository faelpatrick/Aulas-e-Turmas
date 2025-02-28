from PIL import Image

PLUGIN_NOME = "Pixel Art"
PLUGIN_ICONE = "🎨"

def aplicar(imagem):
    tamanho = (imagem.width // 10, imagem.height // 10)  # Reduz resolução
    imagem_pequena = imagem.resize(tamanho, Image.NEAREST)
    return imagem_pequena.resize(imagem.size, Image.NEAREST)  # Expande com efeito pixelado
