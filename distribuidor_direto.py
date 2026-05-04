import http.server
import socketserver
import os

class DirectInjectionHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Caminho físico absoluto para garantir que não haja erro
        file_path = r'C:\dataequitysystem\sac.html'
        
        if os.path.exists(file_path):
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
            print("--- SUCESSO: sac.html injetado no fluxo USB ---")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Arquivo nao encontrado no caminho fisico!")
            print(f"--- ERRO: Arquivo nao encontrado em {file_path} ---")

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8080), DirectInjectionHandler) as httpd:
    print("--- MODO DE INJEÇÃO DIRETA ATIVO ---")
    print("No celular, acesse qualquer link ou apenas: http://localhost:8080")
    httpd.serve_forever()
