from PIL import Image, ImageFilter

PLUGIN_NOME = "Pintura a Óleo"
PLUGIN_ICONE = "🖌"

def aplicar(imagem):
    return imagem.filter(ImageFilter.ModeFilter(size=10))  # Simula efeito de pintura a óleo
