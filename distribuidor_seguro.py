import http.server
import ssl
import socketserver

PORT = 443  # Porta padrão para HTTPS
Handler = http.server.SimpleHTTPRequestHandler

# Localize os arquivos fornecidos pela Aliyun
cert_file = "C:/dataequitysystem/server.crt" 
key_file = "C:/dataequitysystem/server.key"

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=cert_file, keyfile=key_file)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print(f"DISTRIBUIDOR SEGURO (ALIYUN) ATIVO NA PORTA {PORT}")
    httpd.serve_forever()
