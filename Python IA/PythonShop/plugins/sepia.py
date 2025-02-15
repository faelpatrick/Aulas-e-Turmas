from PIL import Image

PLUGIN_NOME = "Sépia"
PLUGIN_ICONE = "🎞️"

def aplicar(imagem):
    """Aplica efeito sépia na imagem."""
    img = imagem.convert("RGB")
    pixels = img.load()
    
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = img.getpixel((i, j))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            pixels[i, j] = (min(tr, 255), min(tg, 255), min(tb, 255))

    return img