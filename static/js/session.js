// Tiempo de inactividad en milisegundos (30 minutos)
const INACTIVITY_TIMEOUT = 30 * 60 * 1000;

// Tiempo de gracia antes de cerrar sesión (5 segundos)
const GRACE_PERIOD = 5000;

let inactivityTimer;
let graceTimer;

// Función para reiniciar el temporizador de inactividad
function resetInactivityTimer() {
    clearTimeout(inactivityTimer);
    inactivityTimer = setTimeout(() => {
        // Mostrar mensaje de advertencia antes de cerrar sesión
        alert('Has estado inactivo durante 30 minutos. Se cerrará tu sesión en 5 segundos.');
        startGracePeriod();
    }, INACTIVITY_TIMEOUT);
}

// Función para iniciar el tiempo de gracia
function startGracePeriod() {
    clearTimeout(graceTimer);
    graceTimer = setTimeout(() => {
        // Cerrar sesión después del tiempo de gracia
        window.location.href = '/cerrar_sesion';
    }, GRACE_PERIOD);
}

// Eventos que resetean el temporizador de inactividad
const activityEvents = [
    'mousemove',
    'mousedown',
    'mouseup',
    'keypress',
    'scroll',
    'touchstart'
];

// Inicializar el sistema de inactividad
function initInactivitySystem() {
    // Iniciar el temporizador inicial
    resetInactivityTimer();
    
    // Agregar listeners para todos los eventos de actividad
    activityEvents.forEach(event => {
        window.addEventListener(event, resetInactivityTimer);
    });
    
    // Cerrar sesión cuando se sale de la página
    window.addEventListener('beforeunload', () => {
        // Solo cerrar sesión si hay una sesión activa
        if (document.cookie.includes('session')) {
            fetch('/cerrar_sesion', {
                method: 'GET',
                credentials: 'include'
            });
        }
    });
}

// Iniciar el sistema cuando se carga la página
document.addEventListener('DOMContentLoaded', initInactivitySystem);
