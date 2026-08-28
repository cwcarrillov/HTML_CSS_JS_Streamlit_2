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
# dedent elimina la sangría del texto multilínea para que HTML no se muestre como código.
from textwrap import dedent

st.set_page_config(page_title="CSS 3", page_icon="🛢️", layout="centered")

# st.markdown inserta contenido en la app. Con unsafe_allow_html=True puede renderizar HTML/CSS.
st.markdown(dedent("""
<style>
/* ==========================================================
   GUÍA RÁPIDA DE CSS
   ==========================================================
   selector        = indica qué elemento queremos modificar.
   background      = cambia el fondo.
   color           = cambia el color del texto.
   border          = crea un borde.
   border-radius   = redondea las esquinas.
   overflow:hidden = recorta lo que sobresale de la tarjeta.
   clip-path       = fuerza la forma curva del contorno.
   padding         = espacio DENTRO del elemento.
   margin          = espacio FUERA del elemento.
   box-shadow      = crea una sombra o brillo.
   transition      = hace suave un cambio visual.
   transform       = mueve, gira o escala un elemento.
   :hover          = estilo usado cuando el cursor está encima.
   ========================================================== */

.stApp{background:#12304A;color:#F7FBFF;}
h1,h2,h3,p{color:#F7FBFF !important;}
.hover-card{
    position:relative;
    border:2px solid rgba(32,230,199,.50);
    border-radius:32px;
    overflow:hidden;
    clip-path: inset(0 round 32px);
    padding:28px;
    background:#1B476B;
    box-shadow:0 14px 36px rgba(4,18,29,.22);
    transition:transform .25s ease, box-shadow .25s ease, border-color .25s ease, background .25s ease;
}
.hover-card::before{
    content:"";
    position:absolute;
    inset:0;
    border-radius:32px;
    background:linear-gradient(135deg, rgba(32,230,199,.08), rgba(255,255,255,.02));
    opacity:.55;
    pointer-events:none;
}
.hover-card:hover{
    transform:translateY(-6px) scale(1.01);
    border-color:#20E6C7;
    background:#20557E;
    box-shadow:0 20px 48px rgba(32,230,199,.24);
}
.hover-label{
    color:#20E6C7;
    opacity:.55;
    transition:opacity .25s ease, letter-spacing .25s ease;
}
.hover-card:hover .hover-label{
    opacity:1;
    letter-spacing:.6px;
}
</style>
"""), unsafe_allow_html=True)

st.markdown(dedent("""

<!-- ========================================================
     GUÍA RÁPIDA DE HTML
     div   = caja o contenedor.
     h1    = título principal.
     h2/h3 = subtítulos.
     p     = párrafo.
     span  = permite aplicar estilo solo a una parte del texto.
     class = conecta un elemento HTML con una regla CSS.
     ======================================================== -->
<div class="hover-card">
    <h1>Reacción visual con CSS</h1>
    <p>Al pasar el cursor, la tarjeta se eleva, se ilumina y cambia sutilmente su fondo.</p>
    <p>Esto demuestra que CSS sí puede reaccionar al cursor, pero solo de forma visual.</p>
    <p class="hover-label">Pase el cursor sobre esta tarjeta para ver el efecto.</p>
</div>
"""), unsafe_allow_html=True)

st.success("En este caso CSS no recalcula nada: solo cambia aspecto, movimiento y brillo.")
