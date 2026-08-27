document.addEventListener("DOMContentLoaded", () => {
    const html = document.documentElement;
    const toggleBtn = document.getElementById("theme-toggle");
    

    if (!toggleBtn) {
        return;
    }

    const themeIcon = toggleBtn.querySelector(".theme-icon");

    const applyTheme = (theme) => {
        const safeTheme = theme === "dark" ? "dark" : "light";

        html.setAttribute("data-bs-theme", safeTheme);
        toggleBtn.setAttribute("aria-pressed", String(safeTheme === "dark"));
        toggleBtn.setAttribute("title", safeTheme === "dark" ? "Cambiar a modo claro" : "Cambiar a modo oscuro");

       if (themeIcon) {
            themeIcon.className = safeTheme === "dark"
                ? "fa-solid fa-sun theme-icon"
                : "fa-solid fa-moon theme-icon";
        }

        localStorage.setItem("theme", safeTheme);
    };

    const savedTheme = localStorage.getItem("theme");
    const systemTheme = window.matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light";

    applyTheme(savedTheme === "dark" || savedTheme === "light" ? savedTheme : systemTheme);

    toggleBtn.addEventListener("click", () => {
        const currentTheme = html.getAttribute("data-bs-theme") === "dark" ? "dark" : "light";
        applyTheme(currentTheme === "dark" ? "light" : "dark");
    });
});

//Mostrar / ocultar contraseña
function togglePassword(fieldId){
    const field = document.getElementById(fieldId);
    const icon = document.getElementById('icon-' + fieldId);

    if(field.type == "password"){
        field.type = "text";
        icon.classList.remove('fa-eye');
        icon.classList.add('fa-eye-slash');
    } else {
        field.type = "password";
        icon.classList.remove('fa-eye-slash');
        icon.classList.add('fa-eye');
    }
}

// Mensajes flotantes
document.addEventListener("DOMContentLoaded", function () {
    const toastElList = [].slice.call(document.querySelectorAll('.toast'));
    toastElList.forEach(function (toastEl) {
        const toast = new bootstrap.Toast(toastEl, {
            delay: 3000
        });
        toast.show();
    });
});

