# 🎬 PROJETO MLOPS: PREVISÃO DE SUCESSO DE FILMES

## 🐳 FastAPI + Docker

Este projeto implementa um modelo de **Machine Learning (Scikit-learn)** para prever a probabilidade de sucesso de filmes, utilizando uma **API RESTful (FastAPI)** empacotada em um contêiner **Docker**. Este setup garante a **reprodutibilidade** e a **facilidade de deploy** em qualquer ambiente.

---

# 📁 ESTRUTURA DO PROJETO

O projeto segue a estrutura padrão, sendo a pasta principal **`projeto-mkt-mle`**.

```text
/
├── 🐳 Dockerfile                  # Define o ambiente de execução e as dependências
├── 📦 requirements.txt            # Dependências Python (Versões corrigidas e fixadas)
├── ⚡ app.py                      # Core da API FastAPI (Define os endpoints)
├── 📖 README.md                   # Este arquivo
├── 🤖 model/
│   └── model.pkl                  # Modelo ML serializado
└── 🧠 src/
    └── predict.py                 # Lógica de Feature Engineering e Predição
                                   # (CONTÉM A LISTA FINAL DE FEATURES)
```

---

# 🚀 COMO FAZER O DEPLOY DO SERVIÇO

### 📋 Pré-requisitos

**Docker instalado e em execução.**

### 1️⃣ Construir a Imagem Docker

Na pasta raiz do projeto:

```bash
docker build -t movie-success-api .
```

### 2️⃣ Rodar o Contêiner

```bash
docker run -d -p 8000:8000 --name ml_api movie-success-api
```

### 3️⃣ Verificar o Status

```bash
docker ps
```

> ✅ **Saída Esperada:** O contêiner **`ml_api`** deve ter o status **`Up X seconds`**.

### 📚 Documentação da API

**Swagger UI:**

`http://localhost:8000/docs`

---

# 🧪 PROVAS DE VALIDAÇÃO FINAL

O teste abaixo prova que a API está **estável** e processa a predição corretamente, resolvendo os problemas de **compatibilidade e alinhamento de dados**.

### 🔗 ENDPOINT

```text
POST http://localhost:8000/predict
```

### 📤 Payload de Teste Enviado

```json
{
  "Title": "Aventura do MLOps",
  "Release_Date": "2025-01-20",
  "Overview": "Um filme de ação e ficção científica com alto orçamento.",
  "Original_Language": "en",
  "Genre": "Action, Science Fiction"
}
```

### 📥 Resposta do Servidor — Log de Sucesso

```json
{
  "probability": 0.566,
  "recommendation": "MEDIO RISCO",
  "prediction_time": "..."
}
```

> ✅ **Resultado:** A API processou a requisição e retornou a probabilidade de sucesso, a recomendação e o tempo de predição.

---

# 🛠️ DESAFIOS DE MLOPS RESOLVIDOS

## ⭐ Destaque

### 1️⃣ COMPATIBILIDADE DE VERSÃO

O `requirements.txt` foi corrigido para fixar a versão do **scikit-learn** (e.g., `scikit-learn==1.6.1`), resolvendo o erro de carregamento do modelo.

### 2️⃣ ALINHAMENTO DE FEATURES — ERRO CRÍTICO 500

O problema **"columns are missing"** foi resolvido no `src/predict.py`, garantindo que a lista **FINAL_FEATURE_COLUMNS** (com as **69 colunas exatas**) seja usada para preencher as features ausentes com zero, estabilizando a inferência.

---

## 🎯 RESULTADO FINAL

✅ Modelo de Machine Learning integrado à API
✅ API RESTful desenvolvida com FastAPI
✅ Aplicação empacotada em Docker
✅ Dependências com versões fixadas
✅ Modelo ML serializado com `model.pkl`
✅ Alinhamento das **69 features**
✅ Tratamento de features ausentes
✅ Endpoint `/predict` validado
✅ Documentação disponível via Swagger UI
