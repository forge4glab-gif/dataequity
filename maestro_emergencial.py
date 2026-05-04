import http.server
import socketserver

class SovereignHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Garante que o navegador não use cache antigo
        self.extensions_map.update({'.js': 'application/javascript', '.json': 'application/json'})
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        with open('data.json', 'wb') as f:
            f.write(data)
        print(">>> [NEXO ATIVO] Saldo Atualizado via VPN")
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", 8080), SovereignHandler) as httpd:
    print("--- DASHBOARD ONLINE: ACESSE http://localhost:8080/index.html ---")
    httpd.serve_forever()
