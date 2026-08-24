# 🎓 Programa de Mentoria: Machine Learning e MLOps em Produção

### Este repositório é desenvolvido sob a tutoria especializada de Manoel Veríssimo. Ele serve como o hub central para o meu programa de desenvolvimento e portfólio prático em **Ciência de Dados, Machine Learning (ML) e MLOps (Machine Learning Operations)**


O objetivo deste programa é fazer uma transição robusta e prática, focando em como construir, versionar e sustentar modelos de ML em ambientes de produção, integrando minha experiência prévia em DataOps e Qualidade.

🎯 Por Que MLOps?

Minha atuação em **Qualidade de Dados (QD)** no setor financeiro me deu uma visão clara: entendi que o **maior gargalo de valor e impacto** não está apenas na modelagem, mas sim na **produtização robusta, segura e escalável** dos modelos – o núcleo da EML.

Este programa me capacita com as habilidades de engenharia necessárias para:

* **Sustentabilidade de Modelo:** Corrigir falhas operacionais (*Schema Drift*, *Data Drift*) no pipeline de produção.
* **Desenvolvimento Robusto:** Construir código limpo e versionado, garantindo a reprodutibilidade.
* **Otimização de Performance:** Entregar modelos que rodam com segurança e baixa latência.

Minha meta é atuar como Cientista de Dados, utilizando conhecimentos de ML e MLOps para desenvolver soluções orientadas a dados que sejam confiáveis, reproduzíveis e aplicáveis ao negócio.

🧠 Estrutura da Tutoria
O programa está dividido em módulos temáticos, seguindo a jornada completa de um projeto de ML, desde a concepção até a sustentação.

| 📊 Mentorada| 🖼️ Mentor | 🚀 Status |
| :--- | :--- | :--- |
|  Yasmin Correia | Manoel Veríssimo | Concluída 📅  |

🛠️ Stack Principal
<p align="left"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/> <img src="https://img.shields.io/badge/Jupyter%20Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Badge"/> <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn Badge"/> <p <img src="https://img.shields.io/badge/MLflow-009688?style=for-the-badge&logo=mlflow&logoColor=white" alt="MLFlow Badge"/> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git Badge"/> <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI Badge"/> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Badge"/>
    </p>


### Projeto final: projeto-mkt-mle.zip

## 🚀 Resumo do Projeto Final: Otimização de Marketing (MII-D)

# Hoje, o desafio não é mais criar modelos & IA's é vencer a Inação da Execução.

O principal problema da liderança hoje é a Inação. A espera pelo "modelo perfeito" e a demora na implantação faz com que a solução perca o valor em um mercado em constante mudança.
Desperdiçar verba em projetos com baixo potencial ou perder o timing do mercado é um grande Risco Financeiro do Marketing. 

Esta solução busca predizer o sucesso potencial de novos filmes ou avalia-los como "alto risco". Assim, apoiando o investimento em divulgação no marketing.

A entrega do MVP prioriza a velocidade e a confiabilidade sobre a complexidade desnecessária.
O **MII-D (Movies Investment Intelligence Dashboard)** é um projeto de **Classificação Binária** que visa **vencer a inação na execução** e otimizar o ROI de marketing antes do lançamento de um filme.

### 🎯 Missão de Negócio

Classificar um filme como **Sucesso 🚀** ou **Fracasso 📉** com base em *features* conhecidas **antes** do lançamento (mitigando **Data Leakage**), fornecendo *insights* acionáveis para o time de Marketing.

---

### ⚙️ Entrega MLOps e Resultados Chave

| Eixo | Detalhe da Entrega | Valor Agregado |
| :--- | :--- | :--- |
| **DataOps e Features** | Mitigação de **Data Leakage**, **Governança de Schema** (`src/constants.py`) e *Feature Engineering* de Sazonalidade (Mês de Lançamento) e Gêneros. | Garante a **confiabilidade** da predição em produção. |
| **Modelagem** | **Regressão Logística Tunada** com `class_weight`. Otimização focada no **F1-Score (0.4562)**. | Entrega um modelo **interpretável** e focado na **métrica de negócio** (equilíbrio entre *Recall* e *Precisão*). |
| **Deployment** | Modelo empacotado em **Contêiner Docker**, servido via **FastAPI** e consumido por um **Dashboard PoC (FlutterFlow App)**. | Demonstra **TTV (Time to Value)** rápido e a transição do modelo para **Produto de Dados** em tempo real. |

---

### 📢 Insights Acionáveis

* **Sazonalidade:** O investimento em marketing deve ser concentrado nos picos de sucesso: **Junho, Julho e Dezembro**.
* **Gênero (ROI):** Prioridade de investimento nos gêneros de maior retorno: **Animação, Ficção Científica e Aventura**.


### 💡 Módulo 2: Resultados Chave e Deployment

| 📊 Métrica de Performance | 🖼️ Prova de Conceito | 🚀 Deployment (MLOps) |
| :--- | :--- | :--- |
| A modelagem priorizou o **F1-Score (0.4562)**. Isso garante um balanço entre: <ul><li>**Recall (77%):** Capturar sucessos reais.</li><li>**Precisão (32%):** Evitar falsos positivos.</li></ul> | <img src="https://github.com/user-attachments/assets/f85d9564-37eb-4c92-9cc0-46e0f212e03a" alt="Dashboard MII-D App" width="100%" style="border-radius: 8px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);"/> | O modelo foi empacotado em **Contêiner Docker** e servido via **FastAPI** para alta performance. Demonstra **TTV** (Time to Value) e a transição para **Produto de Dados** em tempo real. |


