import http.server
import socketserver

class DataEquityDisplay(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        
        # Alimenta as 5 páginas do seu index.html
        with open('data.json', 'wb') as f:
            f.write(data)
            
        print(">>> Dados do Collector (27/04) recebidos e aplicados ao Display.")
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("0.0.0.0", 8080), DataEquityDisplay) as httpd:
    print("--- MONITOR ONLINE: AGUARDANDO DADOS DO COLETOR (27/04) ---")
    httpd.serve_forever()
