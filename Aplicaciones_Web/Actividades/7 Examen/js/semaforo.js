// Obtención de elementos del DOM (Luces)
const luzRojo = document.getElementById("luzRojo");
const luzAmarillo = document.getElementById("luzAmarillo");
const luzVerde = document.getElementById("luzVerde");

// Obtención de elementos del DOM (Botones)
const btnAutoStart = document.getElementById("btnAutoStart");
const btnAutoStop = document.getElementById("btnAutoStop");

const btnVerde = document.getElementById("btnVerde");
const btnAmarillo = document.getElementById("btnAmarillo");
const btnRojo = document.getElementById("btnRojo");

// Obtención de elementos del DOM (Contadores)
const cntVerde = document.getElementById("cntVerde");
const cntAmarillo = document.getElementById("cntAmarillo");
const cntRojo = document.getElementById("cntRojo");

// Variables del estado de contadores
let contadorVerde = 0;
let contadorAmarillo = 0;
let contadorRojo = 0;

// Variables de control de secuencia automática
let intervaloAuto = null;
let ordenSecuencia = 0; // 0: Verde, 1: Amarillo, 2: Rojo

// Función para apagar todas las luces
function apagarLuces() {
    luzVerde.classList.remove("encendido");
    luzAmarillo.classList.remove("encendido");
    luzRojo.classList.remove("encendido");
}

// Función para encender la luz correspondiente e incrementar el contador
function encenderColor(color) {
    apagarLuces();

    if (color === "verde") {
        luzVerde.classList.add("encendido");
        contadorVerde++;
        cntVerde.textContent = contadorVerde;
    } else if (color === "amarillo") {
        luzAmarillo.classList.add("encendido");
        contadorAmarillo++;
        cntAmarillo.textContent = contadorAmarillo;
    } else if (color === "rojo") {
        luzRojo.classList.add("encendido");
        contadorRojo++;
        cntRojo.textContent = contadorRojo;
    }
}

// Función que define el ciclo automático: Verde -> Amarillo -> Rojo
function ejecutarSecuenciaAuto() {
    if (ordenSecuencia === 0) {
        encenderColor("verde");
        ordenSecuencia = 1;
    } else if (ordenSecuencia === 1) {
        encenderColor("amarillo");
        ordenSecuencia = 2;
    } else if (ordenSecuencia === 2) {
        encenderColor("rojo");
        ordenSecuencia = 0;
    }
}

// Evento para Iniciar Modo Automático
btnAutoStart.addEventListener("click", function() {
    if (intervaloAuto !== null) return; // Evita duplicar intervalos activados

    ejecutarSecuenciaAuto(); // Inicia inmediatamente el primer color
    intervaloAuto = setInterval(ejecutarSecuenciaAuto, 2000); // Cambia cada 2 segundos
});

// Evento para Detener Modo Automático
btnAutoStop.addEventListener("click", function() {
    if (intervaloAuto !== null) {
        clearInterval(intervaloAuto);
        intervaloAuto = null;
    }
});

// Eventos para Modo Manual (Detienen el automático y encienden la luz seleccionada)
btnVerde.addEventListener("click", function() {
    btnAutoStop.click();
    encenderColor("verde");
    ordenSecuencia = 1; // Prepara la secuencia para cuando vuelva a activar el modo auto
});

btnAmarillo.addEventListener("click", function() {
    btnAutoStop.click();
    encenderColor("amarillo");
    ordenSecuencia = 2;
});

btnRojo.addEventListener("click", function() {
    btnAutoStop.click();
    encenderColor("rojo");
    ordenSecuencia = 0;
});