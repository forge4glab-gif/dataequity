import http.server
import socketserver
import os

os.chdir(r'C:\dataequitysystem')

class ForceSovereignHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Se o celular pedir a raiz ou o sac.html, entregamos o arquivo na marra
        if self.path == '/' or 'sac.html' in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            with open('sac.html', 'rb') as f:
                self.wfile.write(f.read())
            print("--- NEXO CAUSAL: sac.html ENTREGUE COM SUCESSO ---")
        else:
            return super().do_GET()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8080), ForceSovereignHandler) as httpd:
    print(f"--- SERVIDOR DE FORÇA BRUTA ATIVO EM: {os.getcwd()} ---")
    print("No celular, acesse: http://localhost:8080")
    httpd.serve_forever()
