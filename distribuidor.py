import http.server
import socketserver

PORT = 808
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.apk': 'application/vnd.android.package-archive',
    '.ovpn': 'application/x-openvpn-profile',
    '.mobileconfig': 'application/x-apple-aspen-config',
})

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("SERVIÇO DE DISTRIBUIÇÃO ATIVO EM ")
    httpd.serve_forever()
