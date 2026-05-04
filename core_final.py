import http.server
import socketserver

class GlobalCoreHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        # Grava o nexo de R$ 0,08 diretamente no data.json
        with open('data.json', 'wb') as f:
            f.write(post_data)
            
        print(">>> [SUCESSO] Auditoria Recebida via 5G/Wi-Fi")
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

# "0.0.0.0" permite que o sinal entre pelo seu IP 189.63.226.103
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", 8080), GlobalCoreHandler) as httpd:
    print("--- DATAEQUITY CORE ATIVO ---")
    print("Escutando em: http://189.63.226.103:8080")
    httpd.serve_forever()
