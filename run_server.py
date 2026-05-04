import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def guess_type(self, path):
        if path.endswith('.html'): return 'text/html'
        return super().guess_type(path)

# Escuta em todas as interfaces na porta 8080
with socketserver.TCPServer(("0.0.0.0", 8080), MyHandler) as httpd:
    print("SERVIDOR DATAEQUITY: AGUARDANDO CONEXÃO PC E MOBILE...")
    httpd.serve_forever()
