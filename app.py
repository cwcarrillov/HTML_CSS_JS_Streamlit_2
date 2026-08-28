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

st.set_page_config(page_title="CSS 2", page_icon="🛢️", layout="centered")

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
h1,h2,h3,p,label{color:#F7FBFF !important;}
.card{
    border:2px solid rgba(32,230,199,.60);
    border-radius:32px; overflow:hidden; clip-path: inset(0 round 32px);
    padding:26px; background:#1B476B;
    box-shadow:0 16px 40px rgba(4,18,29,.24);
    transition:transform .24s ease, box-shadow .24s ease;
}
.card:hover{
    transform:translateY(-5px);
    box-shadow:0 20px 46px rgba(32,230,199,.18);
}
.value{color:#20E6C7;font-size:1.25rem;font-weight:800;}
</style>
"""), unsafe_allow_html=True)

oil_bopd = st.slider("Petróleo [BOPD]", 100, 5000, 1200, 50)
water_bwpd = st.slider("Agua [BWPD]", 0, 5000, 600, 50)

st.markdown(dedent(f"""

<!-- ========================================================
     GUÍA RÁPIDA DE HTML
     div   = caja o contenedor.
     h1    = título principal.
     h2/h3 = subtítulos.
     p     = párrafo.
     span  = permite aplicar estilo solo a una parte del texto.
     class = conecta un elemento HTML con una regla CSS.
     ======================================================== -->
<div class="card">
    <h1>Tarjeta curva</h1>
    <p>Petróleo: <span class="value">{oil_bopd:,} BOPD</span></p>
    <p>Agua: <span class="value">{water_bwpd:,} BWPD</span></p>
    <p>En este ejemplo CSS controla bordes, sombras, radio y superficie.</p>
</div>
"""), unsafe_allow_html=True)
