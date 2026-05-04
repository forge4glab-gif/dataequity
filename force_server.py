import http.server
import socketserver

class ForceDownloadHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-Type', 'application/octet-stream')
        self.send_header('Content-Disposition', 'attachment; filename="g.ovpn"')
        super().end_headers()

with socketserver.TCPServer(('', 8080), ForceDownloadHandler) as httpd:
    print("Soberania Ativa em http://192.168.15.22:8080/g.ovpn")
    httpd.serve_forever()
