const API_URL = "https://69c692f1f272266f3eaccdd0.mockapi.io/envios";

const params = new URLSearchParams(window.location.search);
const id = params.get("id");

if (!id) {
    window.location.href = "./busqueda.html";
}

const form = document.getElementById("formDetalle");
const btnEditar = form.querySelector("button[type='submit']");
const selectEstado = document.getElementById("selectEstado");
const selectPrioridad = document.getElementById("selectPrioridad");

function formatearFecha(fechaISO) {
    if (!fechaISO) return "";
    return fechaISO.substring(0, 10);
}

function setSelectValue(selectEl, value) {
    const option = Array.from(selectEl.options).find(o => o.value === value);
    if (option) selectEl.value = value;
}

async function cargarDetalle() {
    try {
        const response = await fetch(`${API_URL}/${id}`);
        if (!response.ok) throw new Error("Envío no encontrado");

        const envio = await response.json();

        document.getElementById("trackingId").textContent        = envio.trackingId ?? envio.id;
        document.getElementById("remitente").value               = envio.remitente ?? "";
        document.getElementById("emailRemitente").value          = envio.emailRemitente ?? "";
        document.getElementById("telefonoRemitente").value       = envio.telefonoRemitente ?? "";
        document.getElementById("destinatario").value            = envio.destinatario ?? "";
        document.getElementById("emailDestinatario").value       = envio.emailDestinatario ?? "";
        document.getElementById("telefonoDestinatario").value    = envio.telefonoDestinatario ?? "";
        document.getElementById("direccionEntrega").value        = envio.direccionEntrega ?? "";
        document.getElementById("ciudadEntrega").value           = envio.ciudadEntrega ?? "";
        document.getElementById("codigoPostal").value            = envio.codigoPostal ?? "";
        document.getElementById("peso").value                    = envio.peso ?? "";
        document.getElementById("largo").value                   = envio.largo ?? "";
        document.getElementById("ancho").value                   = envio.ancho ?? "";
        document.getElementById("alto").value                    = envio.alto ?? "";
        document.getElementById("tipo").value                    = envio.envioExpress ? "Express" : "Normal";
        document.getElementById("checkFrio").checked             = envio.frio ?? false;
        document.getElementById("checkFragil").checked           = envio.fragil ?? false;
        document.getElementById("fechaEsperada").value           = formatearFecha(envio.fechaEsperada);
        document.getElementById("notasAdicionales").value        = envio.notasAdicionales ?? "";

        setSelectValue(selectEstado, envio.estado);
        setSelectValue(selectPrioridad, envio.prioridad);

    } catch (error) {
        console.error(error);
        await Swal.fire({
            position: "center",
            icon: "error",
            title: "Ocurrió un error al visualizar el envío",
            showConfirmButton: false,
            timer: 1500
        });
        window.location.href = "./busqueda.html";
    }
}

async function editarEnvio() {
    const nuevoEstado = selectEstado.value;
    const nuevaPrioridad = selectPrioridad.value;

    try {
        btnEditar.disabled = true;
        btnEditar.innerHTML = `<span class="spinner-border spinner-border-sm me-1"></span> Guardando...`;

        const response = await fetch(`${API_URL}/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                estado: nuevoEstado,
                prioridad: nuevaPrioridad
            })
        });

        if (!response.ok) throw new Error("Error al actualizar el envío");

        await Swal.fire({
            position: "top-end",
            icon: "success",
            title: "Envío actualizado correctamente.",
            showConfirmButton: false,
            timer: 1500
        });
        window.location.href = "./busqueda.html";


        
    } catch (error) {
        console.error(error);
        Swal.fire({
            position: "top-end",
            icon: "error",
            title: "No se pudo actualizar el envío",
            showConfirmButton: false,
            timer: 1500
        });
    } finally {
        btnEditar.disabled = false;
        btnEditar.innerHTML = "Editar";
    }
}

form.addEventListener("submit", function (e) {
    e.preventDefault();
    editarEnvio();
});

cargarDetalle();
