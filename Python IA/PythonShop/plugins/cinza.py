from PIL import Image

PLUGIN_NOME = "Tons de Cinza"
PLUGIN_ICONE = "🔳"

def aplicar(imagem):
    return imagem.convert("L")
