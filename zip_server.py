import http.server
import socketserver

class ZipHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Content-Type', 'application/zip')
        self.send_header('Content-Disposition', 'attachment; filename="nexo.zip"')
        super().end_headers()

with socketserver.TCPServer(('', 8080), ZipHandler) as httpd:
    print("Soberania Ativa: Baixe em http://192.168.15.22:8080/nexo.zip")
    httpd.serve_forever()
