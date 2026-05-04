import http.server
import json
import os
from datetime import datetime

PORT = 8080
DATA_FILE = "data.json"
COPYRIGHT_KEY = "INPI-PR-512026001509-0"

class DataEquityHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        return super().do_GET()

    def do_POST(self):
        if self.path == '/data.json':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                new_data = json.loads(post_data)
                with open(DATA_FILE, 'r', encoding='utf-8') as f:
                    current_data = json.load(f)
                
                # Monetização do dado identificado via blockchain
                current_data['saldo'] += new_data.get('nexo', 0.08)
                current_data['status'] = "monetizando_rede_ativa"
                current_data['last_update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Salvamento maximizado (Etapa 3)
                with open(DATA_FILE, 'w', encoding='utf-8') as f:
                    json.dump(current_data, f, indent=4)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "sucesso", "mensagem": "Nexo transferido"}
                self.wfile.write(json.dumps(response).encode())
                print(f">>> [MONETIZAÇÃO] Recebido pulso de {self.client_address[0]} às {current_data['last_update']}")
            except Exception as e:
                self.send_error(500, f"Erro: {str(e)}")

os.chdir(os.path.dirname(os.path.abspath(__file__)))
server = http.server.HTTPServer(('0.0.0.0', PORT), DataEquityHandler)
print(f"🏛️ DataEquity System Online | Porto: {PORT}")
print(f"🔑 Chave de Proteção: {COPYRIGHT_KEY}")
server.serve_forever()
