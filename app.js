function sumar(){
    const forma =document.getElementById('forma');
    let operandoA = forma['operandoA'];
    let operandoB = forma['operandoB'];
    let resultado = parseInt(operandoA.value) + parseInt(operandoB.value);
    if(isNaN(resultado))
        resultado = 'No hay números';
    document.getElementById('resultado').innerHTML = `Resultado: ${resultado}`;
};
function restar(){
    const forma =document.getElementById('forma');
    let operandoA = forma['operandoA'];
    let operandoB = forma['operandoB'];
    let resultado = parseInt(operandoA.value) - parseInt(operandoB.value);
    if(isNaN(resultado))
        resultado = 'No hay números';
    document.getElementById('resultado').innerHTML = `Resultado: ${resultado}`;
};
function dividir(){
    const forma =document.getElementById('forma');
    let operandoA = forma['operandoA'];
    let operandoB = forma['operandoB'];
    let resultado = parseInt(operandoA.value) / parseInt(operandoB.value);
    if(isNaN(resultado))
        resultado = 'No hay números';
    document.getElementById('resultado').innerHTML = `Resultado: ${resultado}`;
};
function multiplicar(){
    const forma =document.getElementById('forma');
    let operandoA = forma['operandoA'];
    let operandoB = forma['operandoB'];
    let resultado = parseInt(operandoA.value) * parseInt(operandoB.value);
    if(isNaN(resultado))
        resultado = 'No hay números';
    document.getElementById('resultado').innerHTML = `Resultado: ${resultado}`;
};