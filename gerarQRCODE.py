import qrcode

# Dados que você quer codificar no QR code
data = "https://www.example.com"

# Cria uma instância do QRCode
qr = qrcode.QRCode(
    version=1,  # Controle do tamanho do QR Code
    # Controle do nível de correção de erro
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Tamanho de cada caixa do QR Code
    border=4,  # Tamanho da borda
)

# Adiciona os dados ao QR Code
qr.add_data(data)
qr.make(fit=True)

# Cria uma imagem do QR Code
img = qr.make_image(fill_color="black", back_color="white")

# Salva a imagem do QR Code
img.save("qrcode.png")
