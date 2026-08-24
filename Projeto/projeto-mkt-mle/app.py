from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Union, Any
import sys

# --- Importa a lógica de predição da Sprint 5 ---
from src.predict import predict_success 

# --- Inicialização da FastAPI ---
app = FastAPI(
    title="Movie Success Prediction API (MLOps Baseline)",
    description="Previsão de Sucesso de Filmes para otimização de investimento em Marketing.",
    version="1.0"
)

# 1. DEFINIÇÃO DO ESQUEMA DE ENTRADA (Pydantic Model)
# Este é o contrato JSON que a API espera.
class MovieInput(BaseModel):
    Title: str
    Release_Date: str
    Overview: str
    Original_Language: str
    Genre: str

# 2. ENDPOINT DE SAÚDE (HEALTH CHECK)
# Crucial para o monitoramento (Pergunta 7).
@app.get("/health", status_code=200)
def health_check():
    """Confirma que o servidor está em execução."""
    return {"status": "ok", "message": "API is ready for inference."}


# 3. ENDPOINT PRINCIPAL DE PREDIÇÃO
@app.post("/predict", response_model=Dict[str, Any])
async def predict(input_data: MovieInput):
    """
    Recebe os dados do filme e retorna a probabilidade de sucesso.
    """
    try:
        # Transforma o Pydantic Model em um dicionário para a função predict_success
        data_dict = input_data.dict()
        
        # Chama a lógica de predição encapsulada (em src/predict.py)
        result = predict_success(data_dict)
        
        return result
        
    except Exception as e:
        # Em caso de falha de feature engineering ou modelo
        raise HTTPException(status_code=500, detail=f"Erro interno de inferência: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    # Para rodar localmente (Não é necessário para o Docker)
    uvicorn.run(app, host="0.0.0.0", port=8000)
