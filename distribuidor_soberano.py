import http.server
import socketserver
import os

os.chdir(r'C:\dataequitysystem')

class SovereignHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Permite que o Service Worker (sw.js) controle todo o domínio
        self.send_header('Service-Worker-Allowed', '/')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8080), SovereignHandler) as httpd:
    print(f"--- SISTEMA ONLINE: {os.getcwd()} ---")
    print("No celular, recarregue: http://localhost:8080/sac.html")
    httpd.serve_forever()
