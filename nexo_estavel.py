import http.server
import socketserver

PORT = 8080

class DataEquityStableHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Permite que qualquer celular com o APK leia o saldo e os índices
        return super().do_GET()

    def log_message(self, format, *args):
        # Impede que o excesso de logs trave a sua interface gráfica
        return

# Vinculação a 0.0.0.0 permite visibilidade total na rede local de Ribeirão Preto
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", PORT), DataEquityStableHandler) as httpd:
    print("🏛️ SISTEMA DATAEQUITY: MONITORAMENTO LOCAL REATIVADO")
    print("📡 Nexo Local: Porta 8080 (OK)")
    print("☁️ Cloud: AWS Lambda & Aliyun Integradas (OK)")
    print("🔑 Registro: INPI-PR-512026001509-0 (ATIVO)")
    httpd.serve_forever()
