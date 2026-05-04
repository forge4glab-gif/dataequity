import http.server
import socketserver

class AndroidDirectHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# Escuta absoluta para o cabo USB na porta 8080
socketserver.TCPServer.allow_reuse_address = True
try:
    with socketserver.TCPServer(("0.0.0.0", 8080), AndroidDirectHandler) as httpd:
        print("--- SOBERANIA V4: RECEPTOR ATIVO ---")
        print("Aguardando pulso do DataEquity via USB...")
        httpd.serve_forever()
except Exception as e:
    print(f"Erro ao abrir porta: {e}")
