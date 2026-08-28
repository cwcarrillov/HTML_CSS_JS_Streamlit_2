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
# components permite ejecutar HTML/CSS/JS dentro de Streamlit.
import streamlit.components.v1 as components

st.set_page_config(page_title="JS 2", page_icon="🛢️", layout="centered")

st.title("Borde neón con hover")

components.html("""
<style>
/* CONCEPTOS DEL EFECTO NEÓN:
   .shell = contenedor exterior.
   ::before = capa extra creada por CSS, sin agregar otro div.
   conic-gradient = gradiente circular usado como franja luminosa.
   .active = clase que JavaScript agrega y quita.
   @keyframes spin = define la animación de giro. */
html,body{
    margin:0; padding:10px; background:transparent; font-family:Arial,sans-serif;
}
.shell{
    position:relative; padding:4px; border-radius:34px; overflow:hidden;
    clip-path: inset(0 round 34px); background:#12304A;
    box-shadow:0 18px 44px rgba(4,18,29,.28);
}
.shell::before{
    content:""; position:absolute; width:180%; height:180%;
    left:-40%; top:-40%;
    background: conic-gradient(from 0deg, transparent 0deg 220deg, #20E6C7 275deg, #F7FBFF 320deg, transparent 360deg);
    opacity:0; transition:opacity .22s ease;
}
.shell.active::before{
    opacity:1; animation:spin 1.5s linear infinite;
}
.card{
    position:relative; z-index:1; border-radius:30px; overflow:hidden;
    clip-path: inset(0 round 30px); padding:30px; background:#1B476B; color:#F7FBFF;
}
.card strong{color:#20E6C7;}
@keyframes spin{ to{ transform:rotate(360deg); } }
</style>

<div id="shell" class="shell">
    <div class="card">
        <h2>Pozo A-17</h2>
        <p>Producción: <strong>1,250 BOPD</strong></p>
        <p>Water Cut: <strong>31.4%</strong></p>
        <p>Pase el cursor para activar el borde neón.</p>
    </div>
</div>

<script>
// Buscamos el contenedor exterior usando su id.
const shell = document.getElementById("shell");

// mouseenter ocurre cuando el cursor ENTRA en la tarjeta.
shell.addEventListener("mouseenter", () => {
    // classList.add agrega la clase CSS active.
    // Esa clase enciende la animación del borde neón.
    shell.classList.add("active");
});

// mouseleave ocurre cuando el cursor SALE de la tarjeta.
shell.addEventListener("mouseleave", () => {
    // remove elimina active y apaga la animación.
    shell.classList.remove("active");
});
</script>
""", height=280)
