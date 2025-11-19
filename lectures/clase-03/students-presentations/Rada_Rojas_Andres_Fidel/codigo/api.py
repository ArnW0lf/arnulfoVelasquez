# api.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
import json
from LLM_Networks.main_adapt import main_adapt # Importamos el LLM 

# CONFIGURACIÓN E INICIALIZACIÓN DE FASTAPI 
app = FastAPI(
    title="LLM API",
    description="API para adaptar contenido a múltiples redes sociales usando Mistral-7B (Ollama).",
    version="1.0.0"
)

# MODELOS PYDANTIC (Para validar el Input) 

class AdaptationInput(BaseModel):
    """Define la estructura del JSON de entrada (Input)."""
    titulo: str = Field(..., example="Inscripcion de materias en la carrera de ing informatica")
    contenido: str = Field(..., example="El dia de hoy se aprobaron las fechas de incricion de materias en la carrara de ing informatica, desde el 15 de nov al 25 de nov")
    target_networks: list[str] = Field(..., example=["facebook", "instagram", "linkedin"])
    
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "contenido": self.contenido,
            "target_networks": self.target_networks
        }


# ENDPOINT PRINCIPAL 

@app.post("/adapt", summary="Adapta el contenido fuente para las redes sociales especificadas.")
async def adapt_content(input_data: AdaptationInput):
    """
    Recibe el titulo, contenido y la lista de redes a las que se ba a publicar 
    """
    print(f"Petición recibida para redes: {input_data.target_networks}")
    
    full_result = main_adapt(input_data.to_dict())

    return full_result
