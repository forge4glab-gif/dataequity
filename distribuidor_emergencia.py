import http.server
import socketserver
import os

# Define o caminho físico absoluto
os.chdir(r'C:\dataequitysystem')

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()
    
    def do_GET(self):
        # Log detalhado para identificar por que o 404 ocorre
        print(f"Pedido: {self.path} | Pasta Atual: {os.getcwd()}")
        return super().do_GET()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8080), Handler) as httpd:
    print(f"--- SERVIDOR DE EMERGÊNCIA ATIVO EM: {os.getcwd()} ---")
    httpd.serve_forever()
