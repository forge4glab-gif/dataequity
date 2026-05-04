import http.server
import socketserver

class CacheBusterHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Content-Disposition', 'attachment')
        super().end_headers()

PORT = 8080
print(f'Soberania Ativa: Baixe o NOVO ARQUIVO em http://192.168.15.22:8080/nexo_7444.ovpn')
with socketserver.TCPServer(('', PORT), CacheBusterHandler) as httpd:
    httpd.serve_forever()
