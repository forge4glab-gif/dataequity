import http.server
import socketserver
import os

class PWAForceHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Service-Worker-Allowed', '/')
        super().end_headers()

    def do_GET(self):
        if self.path == '/' or self.path == '':
            self.path = '/sac.html'
        return super().do_GET()

# Garante que o Android entenda que o JSON é um Manifesto de App
PWAForceHandler.extensions_map.update({
    '.json': 'application/manifest+json',
    '.js': 'application/javascript',
})

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8080), PWAForceHandler) as httpd:
    print("--- MONITOR DE SOBERANIA ATIVO EM: localhost:8080 ---")
    print("Aguardando o Chrome validar o Manifesto...")
    httpd.serve_forever()
