# src/gpt_client.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def obtener_respuesta(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # modelo gratuito si tienes créditos activos
            messages=[
                {"role": "system", "content": "Eres un analista de reclutamiento TI."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[ERROR] No se pudo generar respuesta: {e}"

