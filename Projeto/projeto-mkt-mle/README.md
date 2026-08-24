PROJETO MLOPS: PREVISÃO DE SUCESSO DE FILMES (FASTAPI + DOCKER)
========================================================================================================

Este projeto implementa um modelo de Machine Learning (Scikit-learn) para prever a probabilidade de sucesso de filmes, utilizando uma API RESTful (FastAPI) empacotada em um contêiner Docker. Este setup garante a reprodutibilidade e a facilidade de deploy em qualquer ambiente.

ESTRUTURA DO PROJETO
--------------------------------------------------------------------------------------------------------

O projeto segue a estrutura padrão, sendo a pasta principal 'projeto-mkt-mle'.

/
├── Dockerfile                  # Define o ambiente de execução e as dependências
├── requirements.txt            # Dependências Python (Versões corrigidas e fixadas)
├── app.py                      # Core da API FastAPI (Define os endpoints)
├── README.md                   # Este arquivo
├── model/
│   └── model.pkl               # Modelo ML serializado
└── src/
    └── predict.py              # Lógica de Feature Engineering e Predição (CONTÉM A LISTA FINAL DE FEATURES)


COMO FAZER O DEPLOY DO SERVIÇO
--------------------------------------------------------------------------------------------------------

Pré-requisitos: Docker instalado e em execução.

Passo 1: Construir a Imagem Docker (na pasta raiz do projeto)
-------------------------------------------------------
docker build -t movie-success-api .

Passo 2: Rodar o Contêiner
---------------------------
docker run -d -p 8000:8000 --name ml_api movie-success-api

Passo 3: Verificar o Status
--------------------------
docker ps
# Saída Esperada: O contêiner 'ml_api' deve ter o status 'Up X seconds'.

Documentação da API (Swagger UI): http://localhost:8000/docs


PROVAS DE VALIDAÇÃO FINAL
--------------------------------------------------------------------------------------------------------

O teste abaixo prova que a API está estável e processa a predição corretamente, resolvendo os problemas de compatibilidade e alinhamento de dados.

ENDPOINT: POST http://localhost:8000/predict

Payload de Teste Enviado:
{
  "Title": "Aventura do MLOps",
  "Release_Date": "2025-01-20",
  "Overview": "Um filme de ação e ficção científica com alto orçamento.",
  "Original_Language": "en",
  "Genre": "Action, Science Fiction"
}

Resposta do Servidor (Log de Sucesso):
{
  "probability": 0.566,
  "recommendation": "MEDIO RISCO",
  "prediction_time": "..."
}


DESAFIOS DE MLOPS RESOLVIDOS (DESTAQUE)
--------------------------------------------------------------------------------------------------------

1. COMPATIBILIDADE DE VERSÃO: O requirements.txt foi corrigido para fixar a versão do scikit-learn (e.g., scikit-learn==1.6.1), resolvendo o erro de carregamento do modelo.

2. ALINHAMENTO DE FEATURES (ERRO CRÍTICO 500): O problema "columns are missing" foi resolvido no src/predict.py, garantindo que a lista FINAL_FEATURE_COLUMNS (com as 69 colunas exatas) seja usada para preencher as features ausentes com zero, estabilizando a inferência.