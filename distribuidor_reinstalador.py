import http.server
import socketserver
import os

# Força o diretório de trabalho
os.chdir(r"C:\dataequitysystem")

class DataEquityHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Service-Worker-Allowed', '/')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8080), DataEquityHandler) as httpd:
    print(f"--- SERVIDOR DE SOBERANIA ATIVO EM: {os.getcwd()} ---")
    print("O CELULAR DEVE CARREGAR A PAGINA AGORA...")
    httpd.serve_forever()
