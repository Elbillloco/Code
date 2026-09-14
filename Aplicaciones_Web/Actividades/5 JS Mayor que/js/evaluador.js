const btnComparar = document.getElementById("btnComparar");

btnComparar.addEventListener("click", function(){
    
    const number01 = Number(document.getElementById("number01").value);
    const number02 = Number(document.getElementById("number02").value);

    const resultado = document.getElementById("resultado");
    const contenedorResultado = document.querySelector(".color_resultado");

    if (isNaN(number01) || isNaN(number02)){
        resultado.textContent = "Debe ingresar solamente numeros";
        return;
    }

    if (number01 > number02){
        resultado.textContent = ("El numero " + number01 + " es el numero mayor");

    } else if (number01 < number02){
        resultado.textContent = ("El numero " + number02 + " es el numero mayor");

    } else if (number01 === number02){
        resultado.textContent = ("Los numeros son iguales");
    }

    const numeroMayor = Math.max(number01, number02);

    if (numeroMayor > 100){
        contenedorResultado.style.backgroundColor = "rgb(75, 4, 74)";
    } else {
        contenedorResultado.style.backgroundColor = "rgb(87, 10, 20)";
    }
})