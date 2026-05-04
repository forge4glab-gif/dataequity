import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith(".ovpn"):
            self.send_header('Content-Type', 'application/x-openvpn-profile')
            self.send_header('Content-Disposition', 'attachment; filename="DataEquity_Collector.ovpn"')
        super().end_headers()

with socketserver.TCPServer(('', 8080), MyHandler) as httpd:
    print("Nexo Ativo em http://0.0.0.0:8080")
    httpd.serve_forever()
