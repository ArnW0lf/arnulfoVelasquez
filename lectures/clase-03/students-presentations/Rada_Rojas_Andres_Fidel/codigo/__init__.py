from LLM_Networks import main_adapt
import json

if __name__ == "__main__":
    
    # El input que tu sistema debe aceptar
    input_data = {
      "titulo": "Nueva funcionalidad en nuestra plataforma",
      "contenido": "Hoy lanzamos una nueva característica que permite a los usuarios crear encuestas interactivas de forma rápida y sencilla.",
      "target_networks": ["facebook", "instagram", "linkedin", "tiktok", "whatsapp"]
    }

    print("--- INICIO DEL SISTEMA DE ADAPTACIÓN LLM ---")
    
    # Ejecutar el sistema completo
    full_result = main_adapt(input_data)
    
    print("\n--- OUTPUT FINAL DEL SISTEMA (JSON REQUERIDO) ---")
    # Imprimir el resultado final. Usamos ensure_ascii=False para ver los emojis y acentos.
    print(json.dumps(full_result, indent=2, ensure_ascii=False))