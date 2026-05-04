import http.server
import socketserver

class DataEquityCapture(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Captura o pulso vindo do Collector via 5G/Wi-Fi
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        
        # Atualiza o nexo de R$ 0,08 no saldo de 115k
        with open('data.json', 'wb') as f:
            f.write(data)
            
        print(">>> [NEXO CONFIRMADO] Auditoria externa recebida.")
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        # Serve o Dashboard para você ver os 115k
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", 8080), DataEquityCapture) as httpd:
    print("--- GATEWAY DE ESCALA: ONLINE ---")
    print("Aguardando Collector no IP 189.63.226.103:8080")
    httpd.serve_forever()
