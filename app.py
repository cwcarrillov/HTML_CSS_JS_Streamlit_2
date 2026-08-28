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

st.set_page_config(page_title="CSS 1", page_icon="🛢️", layout="centered")

FONDO = "#12304A"
SUPERFICIE = "#1B476B"
ACENTO = "#20E6C7"
TEXTO = "#F7FBFF"

# st.markdown inserta contenido en la app. Con unsafe_allow_html=True puede renderizar HTML/CSS.
st.markdown(dedent(f"""
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

.stApp{{background:{FONDO};color:{TEXTO};}}
h1,h2,h3,p,label{{color:{TEXTO} !important;}}
.card{{
    border:2px solid rgba(32,230,199,.55);
    border-radius:30px; overflow:hidden; clip-path: inset(0 round 30px);
    padding:24px; background:{SUPERFICIE}; box-shadow:0 14px 36px rgba(4,18,29,.22);
}}
.accent{{color:{ACENTO};font-weight:800;}}
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
<div class="card">
    <h1>Paleta visual <span class="accent">Oil & Gas</span></h1>
    <p>CSS aplica fondo, color de texto, superficies y color de acento.</p>
</div>
"""), unsafe_allow_html=True)

oil_bopd = st.slider("Petróleo [BOPD]", 100, 5000, 1200, 50)
water_bwpd = st.slider("Agua [BWPD]", 0, 5000, 600, 50)
