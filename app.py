# ============================================================
# GUÍA DE LECTURA DEL SCRIPT
# ============================================================
# Python / Streamlit = recibe datos y realiza cálculos.
# HTML = define qué elementos existen en pantalla.
# CSS = define cómo se ven esos elementos.
# JavaScript = define qué sucede cuando el usuario interactúa.
#
# Los comentarios están escritos en términos simples para que
# el archivo pueda utilizarse directamente durante la clase.
# ============================================================

import streamlit as st
# components permite insertar HTML, CSS y JavaScript dentro de Streamlit.
import streamlit.components.v1 as components

st.set_page_config(page_title="JS 1", page_icon="🛢️", layout="centered")

st.title("Interacción funcional con JavaScript")

components.html("""
<style>
/* CSS de este componente:
   .panel = tarjeta principal.
   .status = caja donde aparece el estado.
   button = botón HTML.
   button:hover = cambio visual cuando el cursor está encima.
   border-radius = curvas; box-shadow = sombra; transition = suavidad. */
html,body{margin:0;padding:10px;background:transparent;font-family:Arial,sans-serif;}
.panel{
    border:2px solid rgba(32,230,199,.65);
    border-radius:32px; overflow:hidden; clip-path: inset(0 round 32px);
    padding:28px; background:#1B476B; color:#F7FBFF;
    box-shadow:0 18px 42px rgba(4,18,29,.26);
}
.status{
    margin:18px 0; padding:14px 16px; border-radius:18px;
    background:rgba(247,251,255,.08);
}
button{
    width:100%; padding:13px; border:2px solid #20E6C7;
    border-radius:18px; background:#20557E; color:#20E6C7;
    font-weight:800; cursor:pointer; transition:transform .2s ease, box-shadow .2s ease;
}
button:hover{
    transform:translateY(-2px);
    box-shadow:0 0 24px rgba(32,230,199,.28);
    color:#F7FBFF;
}
strong{color:#20E6C7;}
</style>

<!-- panel = contenedor principal de esta demostración. -->
<div class="panel">
    <h2>Pozo A-17</h2>
    <!-- id="estado" es un nombre único. JavaScript lo usa para encontrar esta caja. -->
    <div id="estado" class="status">Estado: pendiente de revisión</div>
    <p>Revisiones ejecutadas: <strong id="contador">0</strong></p>
    <!-- Este botón tiene el identificador revisar. -->
    <button id="revisar">Ejecutar revisión</button>
</div>

<script>
// document representa el contenido HTML de este componente.

// getElementById busca un elemento usando su id.
// Aquí guardamos el botón en una constante llamada boton.
const boton = document.getElementById("revisar");

// Buscamos la caja donde mostraremos el estado.
const estado = document.getElementById("estado");

// Buscamos el número visible de revisiones.
const contador = document.getElementById("contador");

// let crea una variable cuyo valor puede cambiar.
// Empieza en cero porque todavía no se ha ejecutado ninguna revisión.
let revisiones = 0;

// addEventListener significa "escuchar una acción".
// click indica que la acción será un clic del usuario.
boton.addEventListener("click", () => {
    // Cada clic suma una revisión.
    revisiones = revisiones + 1;

    // textContent cambia el texto que ve el usuario.
    estado.textContent = "Estado: revisión ejecutada correctamente";

    // Actualizamos el contador visible con el nuevo valor.
    contador.textContent = revisiones;
});
</script>
""", height=300)

st.info("Aquí JavaScript sí cambia contenido y una variable del navegador al hacer clic.")
