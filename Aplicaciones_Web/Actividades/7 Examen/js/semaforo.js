const luzRojo = document.getElementById("luzRojo");
const luzAmarillo = document.getElementById("luzAmarillo");
const luzVerde = document.getElementById("luzVerde");

const btnAutoStart = document.getElementById("btnAutoStart");
const btnAutoStop = document.getElementById("btnAutoStop");

const btnRojo = document.getElementById("btnRojo");
const btnAmarillo = document.getElementById("btnAmarillo");
const btnVerde = document.getElementById("btnVerde");

const cntRojo = document.getElementById("cntRojo");
const cntAmarillo = document.getElementById("cntAmarillo");
const cntVerde = document.getElementById("cntVerde");

let contadorVerde = 0;
let contadorAmarillo = 0;
let contadorRojo = 0;

let intervaloAuto = null;
let ordenSecuencia = 0;

function apagarLuces(){
    luzVerde.classList.remove("encendido");
    luzAmarillo.classList.remove("encendido");
    luzRojo.classList.remove("encendido");
}

function encenderColor(color){
    apagarLuces();

    if(color === "verde"){
        luzVerde.classList.add("encendido");
        contadorVerde++;
        cntVerde.textContent = contadorVerde;
    }else if(color === "amarillo"){
        luzAmarillo.classList.add("encendido");
        contadorAmarillo++;
        cntAmarillo.textContent = contadorAmarillo;
    }else if(color === "rojo"){
        luzRojo.classList.add("encendido");
        contadorRojo++;
        cntRojo.textContent = contadorRojo;
    }
}

function ejecutarSecuenciaAuto(){
    if(ordenSecuencia === 0 ){
        encenderColor("verde");
        ordenSecuencia = 1;
    }else if(ordenSecuencia === 1 ){
        encenderColor("amarillo");
        ordenSecuencia = 2;
    }else if(ordenSecuencia === 2 ){
        encenderColor("rojo");
        ordenSecuencia = 0;
    }
}

btnAutoStart.addEventListener("click", function(){
    if(intervaloAuto !== null) return;

    ejecutarSecuenciaAuto();
    intervaloAuto = setInterval(ejecutarSecuenciaAuto, 2000);
});

btnAutoStop.addEventListener("click", function(){
    if(intervaloAuto !== null){
        clearInterval(intervaloAuto);
        intervaloAuto = null;
    }
});

btnVerde.addEventListener("click", function(){
    btnAutoStop.click();
    encenderColor("verde");
    ordenSecuencia=1;
});
btnAmarillo.addEventListener("click", function(){
    btnAutoStop.click();
    encenderColor("amarillo");
    ordenSecuencia=1;
});
btnRojo.addEventListener("click", function(){
    btnAutoStop.click();
    encenderColor("rojo");
    ordenSecuencia=1;
});