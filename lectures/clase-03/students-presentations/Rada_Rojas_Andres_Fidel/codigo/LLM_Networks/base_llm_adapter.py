# base_adapter.py
import ollama
import json

class BaseLLMAdapter:
    """Clase base que maneja la conexión con Ollama y la lógica de adaptación."""

    # Configuración de Ollama (igual para todas las redes)
    MODEL = 'mistral:7b'
    
    # Atributos a ser definidos por las subclases (cada red)
    NETWORK = "RED_SOCIAL_INDEFINIDA"
    SCHEMA = {} # El formato JSON que nos dara LLM 
    SPECIFIC_RULES = "" # Reglas específicas de prompting

    def __init__(self, titulo: str, contenido: str):
        """Inicializa el adaptador con el contenido fuente."""
        self.titulo = titulo
        self.contenido = contenido

    def _get_output_schema_str(self):
        """Convierte el diccionario SCHEMA a una cadena JSON formateada para el prompt."""
        return json.dumps(self.SCHEMA, indent=4)

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

    def adapt(self):
        """Ejecuta la adaptación llamando a la API local de Ollama."""
        prompt = self._build_prompt()

        try:
            response = ollama.chat(
                model=self.MODEL,
                messages=[
                    {'role': 'user', 'content': prompt}
                ],
                options={
                    'temperature': 0.80, # Controla la creatividad (0.0=conservador, 1.0=creativo)
                    'num_predict': 254, # Limita la longitud máxima de la respuesta
                    'stop': ['\n\n'],   # Evita que el modelo continúe generando texto fuera del JSON
                    'format': 'json'    # ¡CLAVE! Fuerza al modelo a devolver JSON
                }
            )

            # Procesar y retornar el JSON (el output ya viene como string JSON)
            json_output = response['message']['content']
            return json.loads(json_output.strip())

        except Exception as e:
            print(f"Error al llamar a Ollama para {self.NETWORK}: {e}")
            return None