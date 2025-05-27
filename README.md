# Automatize-CV

Automatize-CV es una aplicación web creada con Python y Streamlit que permite evaluar candidatos TI de forma automática a partir de sus CVs (en PDF) y fichas de perfil (Word). Utiliza la API de OpenAI para generar un análisis detallado del match entre el candidato y el perfil requerido.

---

Funcionalidades

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

automatize-cv/
│
├── app.py
│   # Archivo principal de la aplicación Streamlit.
│   # Contiene la interfaz web: carga de archivos, botones, visualización de resultados.
│   # Ejecutas esto con `streamlit run app.py`.
│
├── requirements.txt
│   # Lista de todas las dependencias del proyecto que deben instalarse con pip.
│   # Incluye: streamlit, openai, pdfplumber, python-docx, dotenv, etc.
│
├── .env
│   # Archivo que contiene tu clave secreta de OpenAI.
│   # Este archivo debe estar en `.gitignore` para no subirlo a GitHub.
│
├── prompts/
│   └── prompt_maestro.txt
│       # Archivo de texto que contiene el prompt estructurado para enviar a GPT.
│       # Usa placeholders como {{CV}} y {{FICHA}} que luego son reemplazados en tiempo de ejecución.
│
├── src/
│   # Carpeta que contiene la lógica principal del procesamiento. Código modularizado.
│
│   ├── extractors.py
│   │   # Funciones para extraer texto de archivos PDF (CV) y Word (fichas).
│   │   # Convierte documentos cargados por el usuario en texto procesable.
│   │
│   ├── gpt_client.py
│   │   # Conexión con la API de OpenAI.
│   │   # Envía prompts, recibe respuestas, y maneja errores como falta de crédito o acceso a modelos.
│   │
│   ├── pipeline.py
│   │   # Orquestador principal.
│   │   # Junta: extracción de texto, generación del prompt, llamada a GPT, y delega generación de archivos.
│   │
│   ├── generators.py
│   │   # Genera documentos Word: CV estilizado, carta de presentación, tabla de habilidades.
│   │   # Utiliza `python-docx` para dar formato profesional.
│   │
│   └── utils.py
│       # Funciones auxiliares.
│       # Por ejemplo: separar respuesta GPT por secciones, formatear texto, sanitizar entrada/salida.
│
├── data/
│   # Carpeta con archivos de entrada y salida.
│
│   ├── cvs/
│   │   # Aquí puedes guardar los CVs PDF cargados por los usuarios (opcional).
│   │
│   ├── fichas/
│   │   # Aquí puedes guardar las fichas de perfil en Word que el usuario carga.
│   │
│   └── output/
│       # Aquí se guardan los documentos generados: CV estilizado, carta de presentación, etc.
│       # Puede vaciarse periódicamente si la app se usa en producción.



INSTALACION
# Instalar dependencias
pip install -r requirements.txt

#Conectar con la API de OpenAI (debes tener créditos primero)
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX

#Ejecutar Streamlit
streamlit run app.py

#Abrir la URL
http://localhost:8501 
