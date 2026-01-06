import streamlit as st
import base64
import os

# 1. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="CatLang Analyzer", layout="wide")

# --- FUNCIÓN BASE64 MEJORADA ---
def get_base64_image(image_path):
    # Intenta encontrar el archivo en el directorio actual
    try:
        current_dir = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()
        full_path = os.path.join(current_dir, image_path)
        
        if os.path.exists(full_path):
            with open(full_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()
        return None
    except Exception:
        return None

# Carga de imagen
img_base64 = get_base64_image("Karin.png")

# 2. COLORES Y ESTILOS CSS
color_principal = "#EAD8CF"
color_complementario = "#BCE5F9"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Forum&family=Righteous&display=swap');

    .block-container {{ padding: 0rem; }}
    
    /* SECCIÓN 1 - RESPONSIVA */
    .section-top {{
        background-color: {color_principal};
        padding: 40px 10px 10px 10px;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }}
    
    .titulo-grande {{
        font-family: 'Righteous', cursive;
        font-size: clamp(40px, 10vw, 130px) !important; /* Ajuste automático según pantalla */
        color: #333;
        margin-bottom: 10px;
        line-height: 1;
    }}
    
    .descripcion-centrada {{
        font-family: 'Forum', serif;
        font-size: clamp(16px, 4vw, 18px);
        color: #444;
        max-width: 500px;
        margin: 20px auto 0px auto;
        text-align: center;
        line-height: 1.3;
        padding: 0 15px;
    }}

    .decoracion-curva {{
        background-color: #CFE1EA;
        height: clamp(20px, 5vw, 45px);
        width: 90%;
        max-width: 1300px;
        border-radius: 20px;
        margin: 10px auto;
        display: block;
    }}

    .img-container img {{
        max-width: 100%;
        height: auto;
        width: clamp(300px, 60vw, 650px);
        background-color: transparent !important;
    }}
    
    /* SECCIÓN 2 */
    .section-bottom {{
        background-color: #FFFFFF;
        padding: 40px 10px;
    }}

    /* Ajuste de selectores en móvil */
    [data-testid="stVerticalBlock"] > div {{
        width: 100%;
    }}

    div[data-baseweb="select"] > div {{
        background-color: {color_complementario} !important;
        border-radius: 12px;
        border: 2px solid #a8d5eb !important;
    }}

    .resultado-emocion {{
        font-size: clamp(35px, 8vw, 80px) !important;
        font-weight: bold;
        color: #2E7D32;
        text-align: center;
    }}

    .resultado-error {{
        font-family: 'Forum', serif;
        font-size: 22px !important;
        color: #888;
        text-align: center;
        margin-top: 20px;
    }}

    .automata-box {{
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 15px;
        border: 2px dashed {color_complementario};
        font-family: 'Courier New', monospace;
        text-align: center;
        margin: 20px auto;
        max-width: 90%;
        font-size: clamp(12px, 3vw, 16px);
        overflow-x: auto; /* Permite scroll horizontal si el autómata es muy largo en móvil */
    }}

    .footer {{
        background-color: #f1f1f1;
        padding: 30px 15px;
        text-align: center;
        border-top: 1px solid #ddd;
        margin-top: 50px;
    }}

    /* Media query para asegurar que columnas se apilen correctamente */
    @media (max-width: 768px) {{
        .titulo-grande {{ margin-top: 20px; }}
        .section-top {{ padding-top: 20px; }}
    }}
    </style>
    """, unsafe_allow_html=True)

# --- SECCIÓN 1: PRESENTACIÓN ---
st.markdown(f"""
    <div class="section-top">
        <h1 class="titulo-grande">CatLang Analyzer</h1>
        <div class="descripcion-centrada">
            Esta herramienta interpreta las posturas y señales físicas del felino como cadenas de un lenguaje formal, 
            utilizando conceptos de alfabetos (Σ), gramáticas y autómatas finitos (AFD).
        </div>
    </div>
    """, unsafe_allow_html=True)

if img_base64:
    st.markdown(f"""
        <div style="background-color:{color_principal}; text-align: center; padding-bottom: 30px;">
            <div class="img-container">
                <img src="data:image/png;base64,{img_base64}">
            </div>
            <div class="decoracion-curva"></div>
        </div>
        """, unsafe_allow_html=True)
else:
    st.error("No se pudo cargar la imagen 'Karin.png'. Verifica que esté en la raíz de tu repositorio de GitHub.")

# --- SECCIÓN 2: ANALIZADOR ---
st.markdown('<div class="section-bottom">', unsafe_allow_html=True)
col_espacio_izq, center_col, col_espacio_der = st.columns([0.2, 0.6, 0.2])

with center_col:
    st.markdown("<h2 style='text-align: center; font-family: Forum, serif;'>Analizador Léxico y Sintáctico</h2>", unsafe_allow_html=True)
    
    map_cola = {"Alta (Erguida)": "C_UP", "Baja (Relajada)": "C_LOW", "Erizada (Esponjada)": "C_PUFF"}
    map_orejas = {"Hacia adelante": "E_FWD", "Hacia atrás / Planas": "E_BWD"}
    map_ojos = {"Pupilas dilatadas": "P_EXP", "Pupilas contraídas": "P_CON"}
    map_cuerpo = {"Relajado": "B_RELAX", "Tenso / Encorvado": "B_TENSE"}

    c1, c2 = st.columns(2)
    with c1:
        s_cola = st.selectbox("COLA", list(map_cola.keys()))
        s_orejas = st.selectbox("OREJAS", list(map_orejas.keys()))
    with c2:
        s_ojos = st.selectbox("OJOS", list(map_ojos.keys()))
        s_cuerpo = st.selectbox("CUERPO", list(map_cuerpo.keys()))

    tk = [map_cola[s_cola], map_orejas[s_orejas], map_ojos[s_ojos], map_cuerpo[s_cuerpo]]

    if st.button("ANALIZAR LENGUAJE FORMAL", use_container_width=True):
        emocion = None
        if tk[0] == "C_UP" and tk[1] == "E_FWD" and tk[3] == "B_RELAX":
            emocion = "CURIOSIDAD"
        elif tk[0] == "C_LOW" and tk[1] == "E_FWD" and tk[2] == "P_CON" and tk[3] == "B_RELAX":
            emocion = "RELAJACIÓN"
        elif tk[0] == "C_PUFF" and tk[1] == "E_BWD" and tk[3] == "B_TENSE":
            emocion = "MIEDO / AGRESIÓN"
        elif tk[0] == "C_UP" and tk[1] == "E_FWD" and tk[2] == "P_EXP" and tk[3] == "B_TENSE":
            emocion = "ALERTA"

        if emocion:
            st.markdown(f'<p class="resultado-emocion">{emocion}</p>', unsafe_allow_html=True)
            st.markdown(f"""
            <div class="automata-box">
                q0 ➔ {tk[0]} ➔ q1 ➔ {tk[1]} ➔ q2 ➔ {tk[2]} ➔ q3 ➔ {tk[3]} ➔ q4 (FINAL)
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown('<p class="resultado-error">POSTURA NO RECONOCIDA - Intente nuevamente</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.markdown(f"""
    <div class="footer">
        <p><strong>Aviso Importante:</strong> Esta herramienta educativa no reemplaza el diagnóstico profesional veterinario.</p>
        <hr style="width: 30%; margin: 20px auto;">
        <p><b>Materia:</b> Teoría de Autómatas y Compiladores | <b>Secuencia:</b> 4CM41</p>
    </div>
    """, unsafe_allow_html=True)