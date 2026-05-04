import http.server
import socketserver

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Cabeçalhos que matam o cache do Chrome
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

    def do_GET(self):
        if self.path == '/' or self.path.startswith('/?'):
            self.path = '/index.html'
        return super().do_GET()

# Força o reconhecimento técnico
NoCacheHandler.extensions_map.update({
    '.json': 'application/manifest+json',
    '.js': 'application/javascript',
})

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8080), NoCacheHandler) as httpd:
    print("--- SERVIDOR DE FORÇA TOTAL (CACHE ZERO) ATIVO ---")
    httpd.serve_forever()
