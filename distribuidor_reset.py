import http.server
import socketserver

class ForcePWAHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Service-Worker-Allowed', '/')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_GET(self):
        # Forçamos o Chrome a ler o manifesto com um ID novo (bypass de cache)
        if self.path == '/' or self.path.endswith('.html'):
            self.path = '/sac.html'
        return super().do_GET()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8080), ForcePWAHandler) as httpd:
    print("--- AGORA TENTE INSTALAR NOVAMENTE: localhost:8080 ---")
    httpd.serve_forever()
