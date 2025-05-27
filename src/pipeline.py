# src/pipeline.py

from src.extractors import extraer_texto_pdf, extraer_texto_word
from src.gpt_client import obtener_respuesta


def separar_por_bloques(texto):
    """
    Separa un texto en bloques clave usando títulos o marcadores específicos.
    Devuelve un diccionario con secciones como % de Match, Puntos débiles, Tabla de habilidades.
    """
    bloques = {}
    secciones = {
        "% de Match": None,
        "Puntos débiles": None,
        "Tabla de habilidades": None
    }

    lines = texto.splitlines()
    current_key = None
    buffer = []

    for line in lines:
        line = line.strip()
        if line in secciones:
            if current_key and buffer:
                bloques[current_key] = "\n".join(buffer).strip()
            current_key = line
            buffer = []
        elif current_key:
            buffer.append(line)

    if current_key and buffer:
        bloques[current_key] = "\n".join(buffer).strip()

    return bloques


def procesar_candidato(cv_file, ficha_file):
    """
    Procesa los archivos de CV y ficha, envía el prompt al modelo y devuelve las secciones analizadas.
    """
    cv_texto = extraer_texto_pdf(cv_file)
    ficha_texto = extraer_texto_word(ficha_file)

    with open("prompts/prompt_maestro.txt", "r", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = prompt_template.replace("{{CV}}", cv_texto).replace("{{FICHA}}", ficha_texto)

    resultado = obtener_respuesta(prompt)
    bloques = separar_por_bloques(resultado)

    return {
        "resultado": resultado,
        "match_porcentaje": bloques.get("% de Match"),
        "puntos_debiles": bloques.get("Puntos débiles"),
        "tabla_skills": bloques.get("Tabla de habilidades")
    }
