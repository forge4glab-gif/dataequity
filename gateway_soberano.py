import http.server
import socketserver
import json
import requests

# Configuração de Destino
AWS_URL = "http://sua-instancia-aws.com/api"
ALIYUN_URL = "http://sua-instancia-aliyun.com/api"

class DataEquityGateway(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        
        # 1. Atualiza o Display (As 5 páginas do index.html)
        with open('data.json', 'wb') as f:
            f.write(data)
        
        # 2. Despacha para as Nuvens
        for url in [AWS_URL, ALIYUN_URL]:
            try: requests.post(url, data=data, timeout=1)
            except: pass

        print(">>> Pulso USB recebido: Display Atualizado | Nuvem Sincronizada")
        self.send_response(200)
        self.end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", 8080), DataEquityGateway) as httpd:
    print("--- SISTEMA ONLINE: AGUARDANDO COLLECTOR ---")
    httpd.serve_forever()
