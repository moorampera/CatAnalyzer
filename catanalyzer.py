import streamlit as st
import base64
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="CatLang Analyzer", layout="wide")

# --- FUNCIÓN PARA CARGAR IMAGEN EN BASE64 ---
def get_base64_image(image_path):
    try:
        if os.path.exists(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        return None
    except:
        return None

# Asegúrate de que el archivo se llame gato.png en tu carpeta de GitHub
img_base64 = get_base64_image("gato.png")

# 2. COLORES Y ESTILOS CSS
color_principal = "#F9D0BC"
color_complementario = "#BCE5F9"

st.markdown(f"""
    <style>
    /* Eliminar márgenes por defecto de Streamlit */
    .block-container {{
        padding: 0rem;
    }}
    
    /* SECCIÓN 1: Color Principal */
    .section-top {{
        background-color: {color_principal};
        padding: 80px 20px;
        text-align: center;
        color: #1e1e1e;
    }}
    .titulo-grande {{
        font-size: 60px !important;
        font-weight: 800;
        margin-bottom: 10px;
    }}
    .descripcion-centrada {{
        font-size: 20px;
        max-width: 900px;
        margin: 0 auto 40px auto;
        line-height: 1.6;
    }}
    
    /* SECCIÓN 2: Fondo Blanco */
    .section-bottom {{
        background-color: #FFFFFF;
        padding: 60px 20px;
        min-height: 600px;
    }}

    /* Estilo de los selectores (Color Complementario) */
    div[data-baseweb="select"] > div {{
        background-color: {color_complementario} !important;
        border-radius: 12px;
        border: 2px solid #a8d5eb !important;
    }}

    /* Resultado de emoción */
    .resultado-emocion {{
        font-size: 80px !important;
        font-weight: bold;
        color: #2E7D32;
        text-align: center;
        margin-bottom: 5px;
    }}

    /* Cadena simulación de autómata */
    .automata-path {{
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 15px;
        border: 2px dashed {color_complementario};
        font-family: 'Courier New', Courier, monospace;
        font-size: 18px;
        text-align: center;
        color: #333;
        margin: 20px auto;
        max-width: 80%;
    }}
    .state {{
        color: #d63384;
        font-weight: bold;
    }}
    .arrow {{
        color: #0d6efd;
        font-weight: bold;
    }}

    /* Pie de página */
    .footer {{
        background-color: #f1f1f1;
        padding: 40px;
        text-align: center;
        border-top: 1px solid #ddd;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SECCIÓN 1: PRESENTACIÓN (Color #F9D0BC) ---
st.markdown(f"""
    <div class="section-top">
        <h1 class="titulo-grande">CatLang Analyzer</h1>
        <p class="descripcion-centrada">
            Esta herramienta interpreta las posturas y señales físicas del felino como cadenas de un lenguaje formal, 
            utilizando conceptos de alfabetos (Σ), gramáticas y autómatas finitos (AFD) para generar una 
            interpretación estructurada de su estado emocional.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Imagen Grande y Centrada (dentro de la sección principal)
if img_base64:
    st.markdown(f"""
        <div style="background-color:{color_principal}; padding-bottom: 60px; text-align: center;">
            <img src="data:image/png;base64,{img_base64}" width="600" style="border-radius: 20px; box-shadow: 0px 10px 30px rgba(0,0,0,0.1);">
        </div>
        """, unsafe_allow_html=True)

# --- SECCIÓN 2: ANALIZADOR (Fondo Blanco) ---
st.markdown('<div class="section-bottom">', unsafe_allow_html=True)

# Centrar el analizador
f1, center_col, f2 = st.columns([1, 2, 1])

with center_col:
    st.markdown("<h2 style='text-align: center;'>Analizador Léxico y Sintáctico</h2>", unsafe_allow_html=True)
    
    # Mapeo a Gramática Oficial
    map_cola = {"Alta (Erguida)": "C_UP", "Baja (Relajada)": "C_LOW", "Erizada (Esponjada)": "C_PUFF"}
    map_orejas = {"Hacia adelante": "E_FWD", "Hacia atrás / Planas": "E_BWD"}
    map_ojos = {"Pupilas dilatadas": "P_EXP", "Pupilas contraídas": "P_CON"}
    map_cuerpo = {"Relajado": "B_RELAX", "Tenso / Encorvado": "B_TENSE"}

    c1, c2 = st.columns(2)
    with c1:
        s_cola = st.selectbox("Elemento: COLA", list(map_cola.keys()))
        s_orejas = st.selectbox("Elemento: OREJAS", list(map_orejas.keys()))
    with c2:
        s_ojos = st.selectbox("Elemento: OJOS", list(map_ojos.keys()))
        s_cuerpo = st.selectbox("Elemento: CUERPO", list(map_cuerpo.keys()))

    # Tokens para lógica
    tk = [map_cola[s_cola], map_orejas[s_orejas], map_ojos[s_ojos], map_cuerpo[s_cuerpo]]

    if st.button("PROCESAR CADENA EN AFD", use_container_width=True):
        # Lógica de Emociones
        emocion = "POSTURA NO RECONOCIDA"
        if tk[0] == "C_UP" and tk[1] == "E_FWD" and tk[3] == "B_RELAX":
            emocion = "CURIOSIDAD"
        elif tk[0] == "C_LOW" and tk[1] == "E_FWD" and tk[2] == "P_CON" and tk[3] == "B_RELAX":
            emocion = "RELAJACIÓN"
        elif tk[0] == "C_PUFF" and tk[1] == "E_BWD" and tk[3] == "B_TENSE":
            emocion = "MIEDO / AGRESIÓN"
        elif tk[0] == "C_UP" and tk[1] == "E_FWD" and tk[2] == "P_EXP" and tk[3] == "B_TENSE":
            emocion = "ALERTA"

        # Mostrar Resultado Grande
        st.markdown(f'<p class="resultado-emocion">{emocion}</p>', unsafe_allow_html=True)

        # Simulación de Autómata (debajo del resultado)
        # Formato: q0 --(token)--> q1 ...
        path_html = f"""
        <div class="automata-path">
            <span class="state">q0</span> <span class="arrow">➔</span> {tk[0]} <span class="arrow">➔</span> 
            <span class="state">q1</span> <span class="arrow">➔</span> {tk[1]} <span class="arrow">➔</span> 
            <span class="state">q2</span> <span class="arrow">➔</span> {tk[2]} <span class="arrow">➔</span> 
            <span class="state">q3</span> <span class="arrow">➔</span> {tk[3]} <span class="arrow">➔</span> 
            <span class="state">q4 (FINAL)</span>
        </div>
        """
        st.markdown(path_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.markdown(f"""
    <div class="footer">
        <p><strong>Aviso Importante:</strong><br>
        Esta aplicación es una herramienta educativa basada en teoría de autómatas y no reemplaza 
        en ningún caso el diagnóstico profesional de un médico veterinario o especialista en 
        comportamiento animal. Si su gato presenta signos de malestar, dolor o cambios drásticos 
        en su conducta, consulte a un veterinario de inmediato.</p>
        <hr style="width: 50%; margin: 20px auto;">
        <p><b>Materia:</b> Teoría de Autómatas y Compiladores | <b>Secuencia:</b> 4CM41</p>
        <p style="font-size: 12px; color: #888;">UPIICSA - IPN | 2025</p>
    </div>
    """, unsafe_allow_html=True)