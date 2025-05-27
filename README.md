# Automatize-CV

Automatize-CV es una aplicación web creada con Python y Streamlit que permite evaluar candidatos TI de forma automática a partir de sus CVs (en PDF) y fichas de perfil (Word). Utiliza la API de OpenAI para generar un análisis detallado del match entre el candidato y el perfil requerido.

---

## Funcionalidades

- Carga de CV en formato PDF
- Carga de Ficha de perfil en formato Word
- Evaluación automática con IA (GPT)
- Generación de:
  - Porcentaje de match
  - Puntos débiles
  - Tabla de habilidades
  - Resumen profesional
  - Experiencia laboral en formato narrativo
  - Carta de presentación
  - CV estilizado en formato Word

### Instalar dependencias
pip install -r requirements.txt

### Conectar con la API de OpenAI (debes tener créditos primero)
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX

### Ejecutar Streamlit
streamlit run app.py

### Abrir la URL
http://localhost:8501 
