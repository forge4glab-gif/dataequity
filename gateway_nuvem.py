import http.server
import socketserver
import requests # Certifique-se de ter instalado: pip install requests

# Endereços das suas instâncias (ajuste se necessário)
AWS_ENDPOINT = "http://sua-instancia-aws.amazonaws.com/api/coleta"
ALIYUN_ENDPOINT = "http://sua-instancia-aliyun.com/api/coleta"

class CloudGatewayHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        print(f"--- Dado Capturado (VPN/Apps) via USB ---")
        
        # 1. Envia para AWS
        try:
            requests.post(AWS_ENDPOINT, data=post_data, timeout=2)
            print(" -> AWS: OK")
        except: print(" -> AWS: Falha de conexão")

        # 2. Envia para Aliyun
        try:
            requests.post(ALIYUN_ENDPOINT, data=post_data, timeout=2)
            print(" -> ALIYUN: OK")
        except: print(" -> ALIYUN: Falha de conexão")

        # 3. Atualiza o JSON local para a parte gráfica voltar a funcionar
        with open('data_display.json', 'wb') as f:
            f.write(post_data)

        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", 8080), CloudGatewayHandler) as httpd:
    print("--- GATEWAY DATAEQUITY: USB -> NUVEM (AWS/ALIYUN) ATIVO ---")
    httpd.serve_forever()
