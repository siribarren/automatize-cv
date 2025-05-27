# app.py
import streamlit as st
from src.pipeline import procesar_candidato

st.set_page_config(page_title="Evaluador de Candidatos TI", layout="centered")

st.title("🔍 Evaluador de Candidatos TI")

cv_file = st.file_uploader("📄 Sube el CV (PDF)", type=["pdf"])
ficha_file = st.file_uploader("📘 Sube la Ficha de Perfil (Word)", type=["docx"])

if st.button("Evaluar Candidato"):
    if cv_file and ficha_file:
        with st.spinner("Analizando..."):
            resultado = procesar_candidato(cv_file, ficha_file)
            st.success("✅ Análisis completo.")
            st.text_area("📊 Resultado:", resultado, height=500)
    else:
        st.warning("Debes subir ambos archivos.")

