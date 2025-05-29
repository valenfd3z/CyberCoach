document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".auth-form");
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm_password");

    form.addEventListener("submit", function (e) {
        if (password.value !== confirmPassword.value) {
            e.preventDefault();
            alert("Las contraseñas no coinciden");
        }
    });
});