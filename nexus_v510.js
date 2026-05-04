/* DATAEQUITY CORE v5.1.0 - REGISTRO INPI: 512026001509-0 */
self.addEventListener('install', (e) => self.skipWaiting());
self.addEventListener('activate', (e) => e.waitUntil(self.clients.claim()));

async function pulse() {
    while (true) {
        try {
            await fetch('/api/sync?nexus_v510=true&t=' + Date.now(), { mode: 'no-cors', keepalive: true });
        } catch (err) { }
        await new Promise(r => setTimeout(r, 5000));
    }
}
pulse();
