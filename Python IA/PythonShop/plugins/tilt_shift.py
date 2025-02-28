from PIL import Image, ImageFilter, ImageDraw, ImageEnhance

PLUGIN_NOME = "Tilt Shift"
PLUGIN_ICONE = "📷"

def aplicar(imagem):
    largura, altura = imagem.size

    # Criar imagem desfocada
    img_blur = imagem.filter(ImageFilter.GaussianBlur(radius=12))

    # Criar máscara para definir a área de foco
    mask = Image.new("L", (largura, altura), 0)
    draw = ImageDraw.Draw(mask)

    # Definir a faixa central nítida (30% da altura)
    faixa_central = altura // 3
    faixa_inicio = (altura - faixa_central) // 2
    faixa_fim = faixa_inicio + faixa_central

    # Criar gradiente de desfoque
    for y in range(altura):
        if y < faixa_inicio:  # Borda superior
            fade = int((y / faixa_inicio) * 255)
        elif y > faixa_fim:  # Borda inferior
            fade = int(((altura - y) / (altura - faixa_fim)) * 255)
        else:  # Faixa central nítida
            fade = 255
        draw.line([(0, y), (largura, y)], fill=fade)

    # Aplicar a máscara para mesclar imagem nítida com a desfocada
    imagem_editada = Image.composite(imagem, img_blur, mask)

    # Aumentar saturação para realçar cores
    enhancer = ImageEnhance.Color(imagem_editada)
    return enhancer.enhance(1.7)
