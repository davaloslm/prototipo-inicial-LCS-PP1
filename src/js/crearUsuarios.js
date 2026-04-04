const API_URL = "https://69c692f1f272266f3eaccdd0.mockapi.io/usuarios";

const usuarios = [  
    {
        nombre: "operador1",
        email: "operador1@logitrack.com",
        contrasenia: "1234",
        rol: "operador"
    },
    {
        nombre: "operador2",
        email: "operador2@logitrack.com",
        contrasenia: "2345",
        rol: "operador"
    },
    {
        nombre: "supervisor1",
        email: "supervisor1@logitrack.com",
        contrasenia: "1234",
        rol: "supervisor"
    },
    {
        nombre: "supervisor2",
        email: "supervisor2@logitrack.com",
        contrasenia: "2345",
        rol: "supervisor"
    }
];

async function crearUsuarios(usuarios) {
    for (const usuario of usuarios) {
        try {
            const res = await fetch(API_URL, {
                method: 'POST',
                headers: { 'content-type': 'application/json' },
                body: JSON.stringify(usuario)  
            });

            if (!res.ok) {
                throw new Error(`HTTP error: ${res.status}`);
            }

            const data = await res.json();
            console.log("Usuario creado:", data);

        } catch (error) {
            console.log(`No se pudo crear el usuario: ${usuario.nombre}`);
            console.log(error);
        }
    }
}

crearUsuarios(usuarios);