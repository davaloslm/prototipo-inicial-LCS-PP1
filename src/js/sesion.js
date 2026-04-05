const usuario = JSON.parse(sessionStorage.getItem("usuarioLogueado"));

//mostrar nombre
if (!usuario) {
    window.location.href = "./index.html";
} else {
    document.getElementById("nombreUsuario").textContent = usuario.nombre;
}

//cierre de sesion
document.getElementById("btnCerrarSesion").addEventListener("click", () => {
    sessionStorage.removeItem("usuarioLogueado");
    window.location.href = "./index.html";
});

//habilitar selects de estado y prioridad segun rol
document.querySelectorAll(".edicion").forEach(e => {
    
    if (usuario.rol != "supervisor") {
        
        e.disabled = true;
    }
});

//Mostrar card para ir a historial de registros
const cardHistorial = document.getElementById("cardHistorial");
if (cardHistorial) {
    if (usuario.rol === "supervisor") {
        cardHistorial.classList.remove("d-none");
    } else {
        cardHistorial.classList.add("d-none");
    }
}