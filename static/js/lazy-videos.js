/*
 * lazy-videos.js
 * Implementación de lazy loading para videos
 * 
 * Esta implementación usa IntersectionObserver para optimizar el rendimiento
 * y mejorar la experiencia del usuario al cargar videos.
 */

document.addEventListener('DOMContentLoaded', function() {
    // Inicialización del lazy loading para videos
    // 
    // Usa IntersectionObserver para detectar cuando los videos están a punto de ser visibles
    // y cargarlos solo cuando sea necesario.
    
    // Configuración del IntersectionObserver
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const iframe = entry.target;
                if (!iframe.classList.contains('lazy-loaded')) {
                    // Iniciar la carga del video
                    iframe.removeAttribute('loading');
                    // Mostrar el video
                    iframe.classList.add('lazy-loaded');
                    // Dejar de observar este video
                    observer.unobserve(iframe);
                }
            }
        });
    }, {
        threshold: 0.1, // Umbral: cargar cuando el 10% del video está visible
        rootMargin: '0px 0px 100px 0px' // Margen adicional para cargar antes de que sea visible
    });

    // Observar todos los iframes con clase 'lazy-video'
    document.querySelectorAll('.lazy-video').forEach(iframe => {
        observer.observe(iframe);
    });
});
