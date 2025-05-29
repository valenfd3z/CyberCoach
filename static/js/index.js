document.addEventListener("DOMContentLoaded", function () {
    const botonIniciarSesion = document.getElementById('botonIniciarSesion');
    const botonRegistrarse = document.getElementById('botonRegistrarse');
    const botonCerrarSesion = document.getElementById('botonCerrarSesion');

    // Redirige a la página de inicio de sesión cuando se hace clic en "Iniciar sesión"
    if (botonIniciarSesion) {
        botonIniciarSesion.addEventListener("click", function () {
            window.location.href = '/iniciar_sesion';  // Redirige a la página de inicio de sesión
        });
    }

    // Redirige a la página de registro cuando se hace clic en "Registrarse"
    if (botonRegistrarse) {
        botonRegistrarse.addEventListener("click", function () {
            window.location.href = '/registrar';  // Redirige a la página de registro
        });
    }

    // Redirige a la página principal al cerrar sesión
    if (botonCerrarSesion) {
        botonCerrarSesion.addEventListener("click", function () {
            window.location.href = '/cerrar_sesion';  // Redirige a la ruta de cierre de sesión
        });
    }
});