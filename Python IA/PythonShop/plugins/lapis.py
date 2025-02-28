from PIL import Image, ImageOps, ImageFilter

PLUGIN_NOME = "Esboço a Lápis"
PLUGIN_ICONE = "✏️"

def aplicar(imagem):
    imagem_pb = imagem.convert("L")  # Converte para escala de cinza
    imagem_invertida = ImageOps.invert(imagem_pb)  # Inverte cores
    imagem_borrada = imagem_invertida.filter(ImageFilter.GaussianBlur(10))  
    return Image.blend(imagem_pb, imagem_borrada, 0.5)  # Mescla as imagens
