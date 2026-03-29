const API_URL = "https://69c692f1f272266f3eaccdd0.mockapi.io/envios";
const form = document.querySelector("form");
const btnCrear = form.querySelector("button[type='submit']");
 
form.addEventListener("submit", async function (e) {
    e.preventDefault();
 
    const inputs = form.querySelectorAll("input, select, textarea");
 
    const [
        nombreRemitente, emailRemitente, telefonoRemitente,
        nombreDestinatario, emailDestinatario, telefonoDestinatario,
        direccionEntrega, ciudadEntrega, codigoPostal,
        peso, largo, ancho, alto,
        tipo,
        checkFrio, checkFragil,
        fechaEsperada, notasAdicionales,
    ] = inputs;
 
    const envio = {
        remitente:            nombreRemitente.value.trim(),
        emailRemitente:       emailRemitente.value.trim(),
        telefonoRemitente:    telefonoRemitente.value.trim(),
        destinatario:         nombreDestinatario.value.trim(),
        emailDestinatario:    emailDestinatario.value.trim(),
        telefonoDestinatario: telefonoDestinatario.value.trim(),
        direccionEntrega:     direccionEntrega.value.trim(),
        ciudadEntrega:        ciudadEntrega.value.trim(),
        codigoPostal:         codigoPostal.value.trim(),
        peso:                 parseFloat(peso.value) || 0,
        largo:                parseFloat(largo.value) || 0,
        ancho:                parseFloat(ancho.value) || 0,
        alto:                 parseFloat(alto.value) || 0,
        envioExpress:         tipo.value === "Express" ? true : false,
        frio:                 checkFrio.checked,
        fragil:               checkFragil.checked,
        fechaEsperada:        fechaEsperada.value || null,
        notasAdicionales:     notasAdicionales.value.trim(),
        estado:               "Pendiente",
        prioridad:            "Baja"
    };
 
    try {
        btnCrear.disabled = true;
        btnCrear.innerHTML = `<span class="spinner-border spinner-border-sm me-1"></span> Creando...`;
 
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(envio)
        });
 
        if (!response.ok) throw new Error("Error al crear el envío");
 
        const data = await response.json();
        form.reset();
        await Swal.fire({
            position: "top-end",
            icon: "success",
            title: `Envío creado con éxito`,
            showConfirmButton: false,
            timer: 1500
        });
        window.location.href = "./menu.html"; 
        
    } catch (error) {
        console.error(error);
        Swal.fire({
            position: "top-end",
            icon: "error",
            title: "No se pudo crear el envío",
            showConfirmButton: false,
            timer: 1500
        });
    } finally {
        btnCrear.disabled = false;
        btnCrear.innerHTML = "Crear Envío";
    }
});
 