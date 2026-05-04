import http.server
import socketserver

class ForceSovereign8090(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    def do_GET(self):
        if self.path == '/' or self.path == '': self.path = '/index.html'
        return super().do_GET()

# Garante a identidade PWA
ForceSovereign8090.extensions_map.update({'.json': 'application/manifest+json', '.js': 'application/javascript'})

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8090), ForceSovereign8090) as httpd:
    print("--- NOVA FREQUÊNCIA ATIVA: localhost:8090 ---")
    httpd.serve_forever()
