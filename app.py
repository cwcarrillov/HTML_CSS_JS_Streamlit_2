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
import streamlit.components.v1 as components
from textwrap import dedent

st.set_page_config(page_title="Producción Oil & Gas", page_icon="🛢️", layout="wide")

NAVY = "#0D1F2D"
DEEP = "#142C3E"
SURFACE = "#183B53"
SURFACE_ALT = "#214E6B"
ACCENT = "#C7A86B"
ACCENT_SOFT = "#E8D4A1"
TEXT = "#F5F7FA"
MUTED = "#B9C7D4"
BORDER = "rgba(199, 168, 107, 0.45)"
GLOW = "rgba(199, 168, 107, 0.28)"

st.markdown(
    dedent(
        f"""
        <style>
        :root {{
            --navy: {NAVY};
            --deep: {DEEP};
            --surface: {SURFACE};
            --surface-alt: {SURFACE_ALT};
            --accent: {ACCENT};
            --accent-soft: {ACCENT_SOFT};
            --text: {TEXT};
            --muted: {MUTED};
            --border: {BORDER};
            --glow: {GLOW};
        }}

        .stApp {{
            background: linear-gradient(135deg, #0b1825 0%, #102a3d 35%, #163c54 100%);
            color: var(--text);
        }}

        .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp label, .stApp small {{
            color: var(--text) !important;
        }}

        .hero {{
            position: relative;
            overflow: hidden;
            border: 1px solid var(--border);
            border-radius: 26px;
            background: linear-gradient(135deg, rgba(20,44,62,0.94), rgba(24,59,83,0.9));
            padding: 26px 28px 22px 28px;
            margin-bottom: 22px;
            box-shadow: 0 18px 45px rgba(4, 12, 20, 0.25);
        }}

        .hero::before {{
            content: "";
            position: absolute;
            inset: 0;
            background: linear-gradient(120deg, transparent 0%, rgba(199,168,107,0.1) 40%, transparent 100%);
            transform: translateX(-30%);
        }}

        .eyebrow {{
            position: relative;
            z-index: 1;
            display: inline-block;
            padding: 6px 10px;
            border-radius: 999px;
            font-size: 0.72rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            font-weight: 700;
            background: rgba(199,168,107,0.12);
            color: var(--accent-soft);
            border: 1px solid rgba(199,168,107,0.28);
            margin-bottom: 12px;
        }}

        .hero h1 {{
            position: relative;
            z-index: 1;
            margin: 0;
            font-size: 2.25rem;
            line-height: 1.1;
            letter-spacing: -0.04em;
        }}

        .hero p {{
            position: relative;
            z-index: 1;
            margin: 10px 0 0;
            max-width: 820px;
            color: var(--muted) !important;
            font-size: 1rem;
        }}

        .accent {{
            color: var(--accent-soft);
            font-weight: 700;
        }}

        .insight-card {{
            position: relative;
            background: linear-gradient(180deg, rgba(24,59,83,0.94), rgba(20,44,62,0.9));
            border: 1px solid var(--border);
            border-radius: 22px;
            padding: 20px 20px 18px 20px;
            margin-top: 10px;
            box-shadow: 0 16px 30px rgba(0,0,0,0.16);
            transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
        }}

        .insight-card:hover {{
            transform: translateY(-3px);
            border-color: rgba(199,168,107,0.7);
            box-shadow: 0 22px 38px rgba(199,168,107,0.12);
        }}

        .insight-card h3 {{
            margin: 0 0 14px 0;
            font-size: 1.05rem;
            color: var(--accent-soft) !important;
        }}

        .insight-card p {{
            margin: 8px 0;
            color: var(--muted) !important;
        }}

        .value {{
            color: var(--accent-soft);
            font-weight: 700;
        }}

        div[data-testid="stMetric"] {{
            background: linear-gradient(180deg, rgba(24,59,83,0.96), rgba(17,38,52,0.94));
            border: 1px solid rgba(199,168,107,0.4);
            border-radius: 18px;
            box-shadow: 0 12px 26px rgba(0,0,0,0.18);
            padding: 10px 12px;
            transition: transform 0.25s ease, border-color 0.25s ease;
        }}

        div[data-testid="stMetric"]:hover {{
            transform: translateY(-2px);
            border-color: rgba(199,168,107,0.75);
        }}

        div[data-testid="stMetric"] > div {{
            color: var(--text) !important;
        }}

        div.stButton > button {{
            width: 100%;
            background: linear-gradient(135deg, #d9b77a 0%, #c7a86b 100%);
            color: #102332;
            border: 1px solid rgba(255,255,255,0.5);
            border-radius: 16px !important;
            padding: 0.82rem 1rem;
            font-weight: 800;
            letter-spacing: 0.02em;
            box-shadow: 0 12px 24px rgba(199,168,107,0.18);
            transition: transform 0.22s ease, box-shadow 0.22s ease, filter 0.22s ease;
        }}

        div.stButton > button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 18px 30px rgba(199,168,107,0.28);
            filter: brightness(1.04);
        }}

        div.stButton > button:active {{
            transform: translateY(0);
        }}

        div.stButton > button:focus-visible {{
            outline: 2px solid rgba(255,255,255,0.75);
            outline-offset: 2px;
        }}

        .js-panel {{
            position: relative;
            overflow: hidden;
            background: linear-gradient(135deg, rgba(20,42,62,0.92), rgba(18,60,80,0.85));
            border: 1px solid rgba(199,168,107,0.3);
            border-radius: 28px;
            padding: 18px;
            box-shadow: 0 20px 36px rgba(0,0,0,0.16);
            min-height: 320px;
        }}

        .js-card {{
            position: relative;
            z-index: 1;
            min-height: 250px;
            border-radius: 22px;
            padding: 24px 22px 20px 22px;
            background: radial-gradient(circle at var(--x, 50%) var(--y, 50%), rgba(199,168,107,0.28), rgba(17,38,52,0.1) 30%, rgba(17,38,52,0.92) 62%);
            border: 1px solid rgba(199,168,107,0.24);
            transition: transform 0.28s ease, box-shadow 0.28s ease;
        }}

        .js-card:hover {{
            transform: translateY(-2px);
            box-shadow: inset 0 0 25px rgba(199,168,107,0.08);
        }}

        .js-card h3 {{
            margin: 0 0 14px;
            color: var(--accent-soft) !important;
            font-size: 1.25rem;
        }}

        .js-card p {{
            margin: 10px 0;
            color: var(--muted) !important;
        }}

        .status-pill {{
            display: inline-block;
            margin-top: 18px;
            padding: 8px 12px;
            border-radius: 999px;
            background: rgba(199,168,107,0.1);
            border: 1px solid rgba(199,168,107,0.3);
            color: var(--accent-soft);
            font-size: 0.78rem;
            letter-spacing: 0.04em;
            font-weight: 700;
        }}

        .js-panel::before {{
            content: "";
            position: absolute;
            width: 180%;
            height: 180%;
            left: -40%;
            top: -40%;
            background: conic-gradient(from 0deg, transparent 0deg 210deg, rgba(199,168,107,0.28) 240deg, rgba(255,255,255,0.15) 300deg, transparent 360deg);
            opacity: 0;
            transition: opacity 0.28s ease;
            animation: spin 7s linear infinite;
        }}

        .js-panel.active::before {{
            opacity: 1;
        }}

        @keyframes spin {{
            to {{ transform: rotate(360deg); }}
        }}
        </style>
        """
    ),
    unsafe_allow_html=True,
)

st.markdown(
    dedent(
        """
        <div class="hero">
            <div class="eyebrow">Oil &amp; Gas • Gestión operativa</div>
            <h1>Panel de producción</h1>
            <p>Monitoreo ejecutivo de <span class="accent">petróleo</span>, <span class="accent">agua</span>, <span class="accent">Water Cut</span> e ingresos proyectados con un diseño formal y profesional.</p>
        </div>
        """
    ),
    unsafe_allow_html=True,
)

left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.subheader("1. Parámetros operativos")
    oil_bopd = st.slider("Producción de petróleo [BOPD]", 100, 5000, 1200, 50)
    water_bwpd = st.slider("Producción de agua [BWPD]", 0, 5000, 600, 50)
    oil_price = st.number_input("Precio estimado [USD/bbl]", 1.0, 200.0, 75.0, 1.0)

    st.markdown(
        dedent(
            f"""
            <div class="insight-card">
                <h3>Parámetros activos</h3>
                <p>Petróleo: <span class="value">{oil_bopd:,} BOPD</span></p>
                <p>Agua: <span class="value">{water_bwpd:,} BWPD</span></p>
                <p>Precio: <span class="value">${oil_price:.2f}/bbl</span></p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

    calcular = st.button("Calcular indicadores", type="primary")

with right:
    st.subheader("2. Vista interactiva")
    components.html(
        """
        <style>
        html, body {
            margin: 0;
            padding: 0;
            background: transparent;
            font-family: "Segoe UI", Arial, sans-serif;
        }

        .panel-shell {
            --x: 50%;
            --y: 50%;
            position: relative;
            padding: 10px;
            border-radius: 30px;
            background: linear-gradient(135deg, rgba(20,44,62,0.92), rgba(17,38,52,0.95));
            border: 1px solid rgba(199,168,107,0.4);
            overflow: hidden;
            box-shadow: 0 18px 34px rgba(0,0,0,0.18);
        }

        .panel-shell::before {
            content: "";
            position: absolute;
            inset: -10%;
            background: conic-gradient(from 0deg, transparent 0deg 220deg, rgba(199,168,107,0.28) 270deg, rgba(255,255,255,0.15) 305deg, transparent 360deg);
            opacity: 0;
            transition: opacity 0.28s ease;
        }

        .panel-shell.active::before {
            opacity: 1;
            animation: spin 1.8s linear infinite;
        }

        .panel-card {
            position: relative;
            z-index: 1;
            min-height: 250px;
            padding: 26px 22px 20px 22px;
            border-radius: 22px;
            background: radial-gradient(circle at var(--x) var(--y), rgba(199,168,107,0.22), rgba(17,38,52,0.18) 25%, rgba(17,38,52,0.96) 58%);
            border: 1px solid rgba(199,168,107,0.2);
        }

        .panel-card h3 {
            margin: 0 0 14px;
            color: #E8D4A1;
            font-size: 1.2rem;
        }

        .panel-card p {
            margin: 10px 0;
            color: #dbe5ef;
            font-size: 0.98rem;
        }

        .panel-card strong {
            color: #E8D4A1;
        }

        .status {
            margin-top: 24px;
            padding-top: 12px;
            border-top: 1px solid rgba(199,168,107,0.24);
            font-size: 0.82rem;
            letter-spacing: 0.04em;
            color: #E8D4A1;
            font-weight: 700;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        </style>

        <div id="shell" class="panel-shell">
            <div id="card" class="panel-card">
                <h3>Pozo A-17</h3>
                <p>Producción: <strong>1,250 BOPD</strong></p>
                <p>Water Cut: <strong>31.4%</strong></p>
                <p>Rendimiento estable con tendencia favorable para operación continua.</p>
                <div id="status" class="status">Estado: cursor fuera</div>
            </div>
        </div>

        <script>
        const shell = document.getElementById('shell');
        const card = document.getElementById('card');
        const status = document.getElementById('status');

        shell.addEventListener('mouseenter', () => {
            shell.classList.add('active');
            status.textContent = 'Estado: interacción activa';
        });

        shell.addEventListener('mouseleave', () => {
            shell.classList.remove('active');
            status.textContent = 'Estado: cursor fuera';
            card.style.setProperty('--x', '50%');
            card.style.setProperty('--y', '50%');
        });

        card.addEventListener('pointermove', (event) => {
            const rect = card.getBoundingClientRect();
            const x = ((event.clientX - rect.left) / rect.width) * 100;
            const y = ((event.clientY - rect.top) / rect.height) * 100;
            card.style.setProperty('--x', x + '%');
            card.style.setProperty('--y', y + '%');
        });
        </script>
        """,
        height=340,
    )

if calcular:
    total_fluid = oil_bopd + water_bwpd
    water_cut = water_bwpd / total_fluid * 100 if total_fluid else 0
    monthly_oil = oil_bopd * 30
    gross_revenue = monthly_oil * oil_price

    st.subheader("3. Resultado operativo")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Petróleo", f"{oil_bopd:,.0f} BOPD")
    c2.metric("Fluido total", f"{total_fluid:,.0f} BFPD")
    c3.metric("Water Cut", f"{water_cut:.1f}%")
    c4.metric("Ingreso mensual", f"${gross_revenue:,.0f}")

    st.markdown(
        dedent(
            f"""
            <div class="insight-card">
                <h3>Resumen ejecutivo</h3>
                <p>El pozo genera <span class="value">{oil_bopd:,.0f} BOPD</span> de petróleo con un fluido total de <span class="value">{total_fluid:,.0f} BFPD</span>.</p>
                <p>El Water Cut estimado es <span class="value">{water_cut:.1f}%</span>, y el ingreso bruto mensual proyectado es <span class="value">${gross_revenue:,.0f}</span>.</p>
            </div>
            """
        ),
        unsafe_allow_html=True,
    )

st.caption("Ejemplo educativo: no incluye regalías, impuestos, OPEX, transporte ni descuentos comerciales.")
