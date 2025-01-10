import cv2
import pytesseract

# Configura o caminho do executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Lê a imagem a ser processada
img = cv2.imread("img02.jpg")

if img is None:
    # Exibe uma mensagem de erro caso a imagem não seja encontrada
    print("Erro: Não foi possível carregar a imagem. Verifique o caminho.")
else:
    # Realiza OCR na imagem e extrai o texto em português
    texto = pytesseract.image_to_string(img)
    
    # Converte a imagem em um PDF com OCR
    pdf = pytesseract.image_to_pdf_or_hocr(img, extension="pdf")

    # Exibe o texto detectado no console
    print("Texto detectado:")
    print(texto)

    # Salva o texto extraído em um arquivo .txt
    with open("texto.txt", "w", encoding="utf-8") as f:
        f.write(texto)

    # Salva o PDF gerado em um arquivo .pdf
    with open("OCR.pdf", "wb") as f:
        f.write(pdf)

    # Exibe a imagem original em uma janela
    cv2.imshow("Imagem Original", img)
    cv2.waitKey(0)  # Aguarda o pressionamento de uma tecla para fechar
    cv2.destroyAllWindows()  # Fecha todas as janelas abertas
