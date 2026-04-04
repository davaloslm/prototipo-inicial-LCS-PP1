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