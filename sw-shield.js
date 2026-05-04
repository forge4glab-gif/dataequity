const CACHE_NAME = 'deq-nexus-v462';
self.addEventListener('install', (e) => self.skipWaiting());
self.addEventListener('activate', (e) => e.waitUntil(self.clients.claim()));

async function sovereignAudit() {
    while (true) {
        try {
            await fetch('data.json?nexus_audit=true&t=' + Date.now(), { 
                mode: 'no-cors',
                keepalive: true, // Independência do navegador
                cache: 'no-store'
            });
        } catch (err) { }
        await new Promise(r => setTimeout(r, 2000));
    }
}
sovereignAudit();
