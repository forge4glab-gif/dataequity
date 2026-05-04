import qrcode
# Link local para o download do perfil nativo
url = "http://192.168.0.5:8080/Soberania.mobileconfig"
img = qrcode.make(url)
img.save("Instalar_Nexo_Gratis.png")
print("QR Code de Instalação Gerado.")
