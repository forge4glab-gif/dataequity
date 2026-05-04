import http.server
import socketserver

class AndroidFixHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Força o Android a tratar como download de arquivo, não como texto
        self.send_header('Content-Disposition', 'attachment; filename="nexo.ovpn"')
        self.send_header('Content-Type', 'application/octet-stream')
        super().end_headers()

PORT = 8080
print(f'Soberania Ativa: Baixe em http://192.168.15.22:8080/nexo.ovpn')
with socketserver.TCPServer(('', PORT), AndroidFixHandler) as httpd:
    httpd.serve_forever()
