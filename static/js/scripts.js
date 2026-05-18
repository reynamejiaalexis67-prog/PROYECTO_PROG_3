let contar = 0

document.getElementById("btn-agregar").onclick = function(){
    contar += 1;
    document.getElementById("boton-formulario").innerHTML = contar;
}