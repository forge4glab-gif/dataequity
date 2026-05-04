import http.server
import socketserver

class UltimateHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        html_content = r'''<html><head>
    <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests"><meta charset="UTF-8"><style>
    .nav-footer { margin-top: 50px; display: flex; gap: 20px; border-top: 1px solid #222; padding-top: 20px; }
    .btn-nav { background: none; border: 1px solid #facc15; color: #facc15; padding: 12px 25px; cursor: pointer; text-transform: uppercase; font-size: 0.8em; font-weight: bold; transition: 0.3s; }
    .btn-nav:hover { background: #facc15; color: #000; }
    .btn-nav:disabled { border-color: #444; color: #444; cursor: not-allowed; }
</style></head><body style="background:#000;color:#fff;padding:50px;text-align:center;">
    <h2>SAC - CENTRAL DE SOBERANIA</h2>
    <p>Suporte Técnico: rscvictorpsc@gmail.com</p>
    <p>Protocolo de Atendimento Ativo 24/7 via AWS CloudWatch.</p>
    <div class="nav-footer" style="justify-content:center;">
        <button class="btn-nav" onclick="location.href='faq.html'">VOLTAR (06)</button>
        <button class="btn-nav" disabled>FINALIZADO</button>
    </div>
<script>
// Alinhamento com collector.py: Bypass de SSL para rede local
if (location.protocol === 'http:') {
    console.log("Nexo de Soberania: Ignorando restrições de SSL.");
}

function ativarNexoReal() {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js', { scope: '/' }).then(function(reg) {
            console.log('Service Worker registrado.');
            alert("Nexo Causal Ativado! Se o Android avisar 'Conexão não segura', clique em AVANÇADO e PROSSEGUIR.");
        }).catch(function(err) {
            console.error('Falha no nexo:', err);
        });
    }
}
window.onload = ativarNexoReal;
</script>
</body></html>

<div style='margin-top:30px; border:2px solid #facc15; padding:20px;'><h3 style='color:#facc15'>DOWNLOAD DO COLLECTOR MOBILE</h3><p>Instale o motor de auditoria no seu celular para selar o nexo causal.</p><a href='DataEquity_Collector_Mobile.apk' style='background:#facc15; color:#000; padding:10px; text-decoration:none; font-weight:bold;'>BAIXAR .APK AGORA</a></div>
<div style='margin-top:30px; border:2px solid #00f; padding:20px; background:#001;'>
    <h3 style='color:#fff'>ATIVAR COLLECTOR LIVE</h3>
    <p>Clique abaixo para transformar esta página no Coletor Oficial no seu celular.</p>
    <button onclick="instalarCollector()" style='background:#00f; color:#fff; padding:15px; border:none; cursor:pointer; font-weight:bold;'>ATIVAR NO CELULAR</button>
</div>
<script>
function instalarCollector() {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js').then(() => {
            alert('Nexo Causal Ativado! Adicione à tela inicial para iniciar a coleta de R$ 0,08.');
        });
    }
}
</script>


'''
        self.wfile.write(html_content.encode('utf-8'))
        print("--- NEXO CAUSAL: INTERFACE ENVIADA AO CELULAR ---")

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 8080), UltimateHandler) as httpd:
    print("--- MONITOR ÚNICO ATIVO: localhost:8080 ---")
    httpd.serve_forever()
