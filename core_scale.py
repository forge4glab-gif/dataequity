import http.server
import socketserver

class ScaleHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        with open('data.json', 'wb') as f:
            f.write(post_data)
        print(">>> [NEXO ENCONTRADO] Auditoria 5G recebida com sucesso!")
        self.send_response(200)
        self.end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", 8080), ScaleHandler) as httpd:
    print("--- DATAEQUITY CORE: AGUARDANDO SINAL EXTERNO ---")
    print("Destino configurado: http://189.63.226.103:8080")
    httpd.serve_forever()
