import qrcode
import os

# Dados extraídos do arquivo dataequity.conf.conf
config_data = """[Interface]
Address = 10.0.0.5/32
DNS = 1.1.1.1
MTU = 1380
PrivateKey = WOHDJpKKPQDc7AJlzooGIRxDzIkKxvHxYmfnUlQZTWU=

[Peer]
AllowedIPs = 10.0.0.0/24
Endpoint = 47.85.161.107:51820
PublicKey = QlSkv2NEXLmvaXPZ+RpXDzwwMFSw3YaXMePOeFW8pWc="""

# Geração do Objeto Visual
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(config_data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("DataEquity_Nexo_WG.png")
print("Nexo Gerado: DataEquity_Nexo_WG.png")
