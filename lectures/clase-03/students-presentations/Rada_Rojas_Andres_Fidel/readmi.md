# 📚 Documentación de Prompts - Módulo de Adaptación

## LLM Utilizado
**OLLAMA** con el modelo **`mistral:7b`**

---

## 1. Prompt Padre (Lógica Base)

Este *prompt* se encuentra en la clase **`BaseLLMAdapter`** y es la plantilla de comunicación que asegura que el modelo **Mistral** cumpla con los requisitos técnicos (formato JSON, idioma y reglas generales).

```python
class BaseLLMAdapter:

    def _build_prompt(self) -> str:
        """Construye el prompt completo combinando el contenido y las reglas de la subclase."""
        return f"""
        Eres un experto en marketing de redes sociales, altamente capacitado en la creación
        de contenido para la plataforma '{self.NETWORK.upper()}'.
        
        # INSTRUCCIÓN CLAVE: El texto de salida DEBE estar redactado íntegramente en ESPAÑOL.
        
        Título Original: {self.titulo}
        Contenido Original: {self.contenido}

        # REGLAS DE ADAPTACIÓN PARA {self.NETWORK.upper()}
        1. **Reglas Específicas:** {self.SPECIFIC_RULES}
        2. **Hashtags:** Genera 3 a 5 hashtags específicos.
        3. **Formato:** El resultado DEBE ser un objeto JSON que siga exactamente este formato (schema):
        {self._get_output_schema_str()}
        """

```

# --- 1. ADAPTADOR FACEBOOK ---
```python
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
```

# --- 2. ADAPTADOR INSTAGRAM ---
```python
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
```
# --- 3. ADAPTADOR LINKEDIN ---
```python
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
```
# --- DIAGRANA ---

![alt text](image.png)