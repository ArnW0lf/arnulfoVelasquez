# main_system.py
import json
from .network_adapters import ADAPTER_MAP

def main_adapt(data: dict) -> dict:
    """
    Función principal que simula la API o el módulo, procesando el input
    y adaptando el contenido para todas las redes sociales objetivo.

    Input requerido:
    {
      "titulo": "...",
      "contenido": "...",
      "target_networks": ["facebook", "instagram", ...]
    }
    """
    
    # 1. Extracción de datos de entrada
    titulo = data.get("titulo", "")
    contenido = data.get("contenido", "")
    target_networks = data.get("target_networks", [])

    final_output = {}

    # 2. Iterar sobre las redes solicitadas
    for network_key in target_networks:
        
        # 3. Buscar la clase de adaptador correspondiente
        AdapterClass = ADAPTER_MAP.get(network_key)

        if AdapterClass:
            print(f"-> Adaptando contenido para: {network_key.upper()}...")
            
            # 4. Instanciar y ejecutar la adaptación
            adapter_instance = AdapterClass(titulo, contenido)
            result = adapter_instance.adapt()

            if result:
                final_output[network_key] = result
            else:
                final_output[network_key] = {"error": f"Fallo al generar contenido en {network_key}."}
        else:
            final_output[network_key] = {"error": f"Adaptador no implementado para {network_key}."}

    return final_output

# ---------------- DEMOSTRACIÓN ----------------

if __name__ == "__main__":
    
    # El input que tu sistema debe aceptar
    input_data = {
      "titulo": "Nueva funcionalidad en nuestra plataforma",
      "contenido": "Hoy lanzamos una nueva característica que permite a los usuarios crear encuestas ,interactivas de forma rápida y sencilla.",
      "idioma": "Español",
      "target_networks": ["facebook", "instagram", "linkedin", "tiktok", "whatsapp"]
    }

    print("--- INICIO DEL SISTEMA DE ADAPTACIÓN LLM ---")
    
    # Ejecutar el sistema completo
    full_result = main_adapt(input_data)
    
    print("\n--- OUTPUT FINAL DEL SISTEMA (JSON REQUERIDO) ---")
    # Imprimir el resultado final. Usamos ensure_ascii=False para ver los emojis y acentos.
    print(json.dumps(full_result, indent=2, ensure_ascii=False))