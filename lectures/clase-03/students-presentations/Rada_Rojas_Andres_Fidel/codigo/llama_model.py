import ollama
import json

def adaptar_contenido_mistral(titulo, contenido, red_social):
    # 1. Definir el PROMPT estructurado
    # Le decimos al modelo qué queremos y CÓMO queremos el output (en JSON)
    prompt = f"""
    Eres un experto en marketing de redes sociales. Tu tarea es adaptar un contenido
    dado para la plataforma '{red_social}'.

    Título Original: {titulo}
    Contenido Original: {contenido}

    Reglas para {red_social.upper()}:
    - El texto debe ser atractivo y usar emojis.
    - El tono debe ser 'casual'.
    - Genera 3-5 hashtags relevantes.
    - El resultado DEBE ser un objeto JSON que siga exactamente el siguiente formato:
    {{
      "text": "El texto adaptado aquí...",
      "hashtags": ["#tag1", "#tag2", "#tag3"],
      "character_count": 250,
      "tone": "casual"
    }}
    """
    
    try:
        # 2. Llamada a la API local de Ollama
        response = ollama.chat(
            model='mistral:7b',
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            # Importante: Le pedimos a Mistral que genere directamente un JSON
            options={
                'temperature': 0.7,
                'num_predict': 512, # Limita la longitud
                'stop': ['\n\n'],
                'format': 'json' # Esto es CLAVE para la salida estructurada
            }
        )

        # 3. Procesar la respuesta JSON
        # La respuesta ya viene en un string JSON, solo necesitamos parsearla
        json_output = response['message']['content']
        return json.loads(json_output)
    
    except Exception as e:
        print(f"Error al llamar a Ollama: {e}")
        return None

# --- DEMOSTRACIÓN ---
titulo_ejemplo = "Nueva funcionalidad en nuestra plataforma"
contenido_ejemplo = "Hoy lanzamos una nueva característica que permite a los usuarios crear encuestas interactivas de forma rápida y sencilla."

resultado_facebook = adaptar_contenido_mistral(
    titulo_ejemplo, 
    contenido_ejemplo, 
    "facebook"
)
# --- CÓDIGO ACTUAL ---
# print(f"Resultado para Facebook:\n{json.dumps(resultado_facebook, indent=2)}")

# --- CÓDIGO CORREGIDO ---
print(f"Resultado para Facebook:\n{json.dumps(resultado_facebook, indent=2, ensure_ascii=False)}")