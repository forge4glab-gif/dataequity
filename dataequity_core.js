self.addEventListener('install', (e) => self.skipWaiting());
self.addEventListener('activate', (e) => {
    caches.keys().then(names => {
        for (let name of names) caches.delete(name);
    });
    self.registration.unregister().then(() => {
        console.log('Soberania v3.0 Encerrada. Reiniciando para v5.1.1...');
    });
});
