const btnComparar = document.getElementById("btnComparar");

btnComparar.addEventListener("click", function(){
    
    const number01 = document.getElementById("number01").value;
    const number02 = document.getElementById("number02").value;

    const resultado = document.getElementById("resultado");

    if (number01 > number02){
        resultado.textContent = ("El numero " + number01 + " es el numero mayor");

    } else if (number01 < number02){
        resultado.textContent = ("El numero " + number02 + " es el numero mayor");

    } else if (number01 === number02){
        resultado.textContent = ("Los numeros son iguales");
    }

    if (isNaN(number01) || isNaN(number02)){
        resultado.textContent = "Debe ingresar solamente numeros";
        return;
    }
})