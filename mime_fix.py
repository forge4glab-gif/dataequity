import http.server
import socketserver

class ForceMimeHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith(".ovpn"):
            # Informa ao celular que este é um perfil de VPN e não um texto
            self.send_header('Content-Type', 'application/x-openvpn-profile')
            self.send_header('Content-Disposition', 'attachment; filename="DataEquity_Collector.ovpn"')
        super().end_headers()

with socketserver.TCPServer(('', 8080), ForceMimeHandler) as httpd:
    print("Nexo de Entrega Ativo em http://0.0.0.0:8080")
    httpd.serve_forever()
