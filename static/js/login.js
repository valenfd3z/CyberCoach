document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevenir el comportamiento por defecto (recargar la página)

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Muestra un mensaje de éxito y redirige al usuario a la página principal
            alert('Inicio de sesión exitoso');
            window.location.href = '/';  // Redirige a la página principal (index)
        } else {
            // Muestra un mensaje de error si las credenciales son incorrectas
            alert('Credenciales incorrectas');
        }
    })
    .catch(error => {
        console.error('Error:', error);  // Muestra el error si ocurre un problema
    });
});
