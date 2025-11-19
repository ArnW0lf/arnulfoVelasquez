# network_adapters.py
from .base_llm_adapter import BaseLLMAdapter

# --- 1. ADAPTADOR FACEBOOK ---
class FacebookAdapter(BaseLLMAdapter):
    NETWORK = "facebook"
    SCHEMA = {
      "text": "El texto adaptado aquí...",
      "hashtags": ["#tag1", "#tag2", "#tag3"],
      "character_count": 200,
      "tone": "casual",
      "suggested_image_prompt": "Prompt detallado para IA generativa..."
    }
    SPECIFIC_RULES = (
        "El texto debe ser atractivo, tener un límite de 200 caracteres, y usar emojis. "
        "El tono debe ser 'casual' y amigable para fomentar la interacción."
    )

# --- 2. ADAPTADOR INSTAGRAM ---
class InstagramAdapter(BaseLLMAdapter):
    NETWORK = "instagram"
    SCHEMA = {
      "text": "El texto adaptado aquí...",
      "hashtags": ["#tag1", "#tag2", "#tag3"],
      "character_count": 180,
      "tono": "Alegre y llamativo",
      "suggested_image_prompt": "Prompt detallado para IA generativa..."
    }
    SPECIFIC_RULES = (
        "El texto (caption) debe ser corto, altamente visual, tener un límite de 150 caracteres, "
        "y usar muchos emojis. Adicionalmente, genera un 'suggested_image_prompt' conciso, "
        "moderno y apto para una IA de imágenes (ej. 'fotografía de tecnología moderna...')."
    )

# --- 3. ADAPTADOR LINKEDIN ---
class LinkedInAdapter(BaseLLMAdapter):
    NETWORK = "linkedin"
    SCHEMA = {
      "text": "El post formal aquí...",
      "hashtags": [],
      "character_count": 250,
      "tone": "formal, serio"
    }
    SPECIFIC_RULES = (
        "El tono debe ser 'formal', 'serio' y 'profesional'. Enfócate en el valor técnico "
        "y el impacto profesional. No uses emojis, o úsalos de forma muy limitada, seria y profesional. "
        "El post debe ser estructurado y orientado a la comunidad de negocios y academicos."
    )

# --- MAPEO DE ADAPTADORES (El registro de las clases) ---
ADAPTER_MAP = {
    "facebook": FacebookAdapter,
    "instagram": InstagramAdapter,
    "linkedin": LinkedInAdapter
}


