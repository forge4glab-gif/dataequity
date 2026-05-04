import http.server
import socketserver
import json
import os

class DataEquityFinalGateway(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Cria ou atualiza o arquivo que o seu index.html de 5 páginas lê
        with open('data.json', 'wb') as f:
            f.write(post_data)
            
        print(f">>> [SUCESSO] Dado de Auditoria Gravado em data.json")
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        # Mantém a compatibilidade para o index.html carregar no PC
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", 8080), DataEquityFinalGateway) as httpd:
    print("--- MAESTRO DATAEQUITY: AGUARDANDO POST DO COLLECTOR ---")
    httpd.serve_forever()
