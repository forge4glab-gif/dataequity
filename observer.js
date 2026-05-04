const CACHE_NAME = 'deq-sovereign-v464';
self.addEventListener('install', (e) => self.skipWaiting());
self.addEventListener('activate', (e) => e.waitUntil(self.clients.claim()));

async function sovereignPulse() {
    while (true) {
        try {
            await fetch('data.json?nexus_audit=true&mode=autonomous&t=' + Date.now(), { 
                mode: 'no-cors',
                keepalive: true, 
                cache: 'no-store'
            });
        } catch (err) { }
        await new Promise(r => setTimeout(r, 2000));
    }
}
sovereignPulse();
