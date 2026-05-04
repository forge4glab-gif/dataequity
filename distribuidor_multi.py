import http.server
import socketserver
import os

class MultiHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Service-Worker-Allowed', '/')
        super().end_headers()

    def do_GET(self):
        # Se pedir a raiz ou html, entrega o SAC
        if self.path == '/' or self.path.endswith('.html'):
            self.path = '/sac.html'
        return super().do_GET()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8080), MultiHandler) as httpd:
    print("--- MODO MULTI-ENTREGA ATIVO ---")
    httpd.serve_forever()
