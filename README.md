# 🎓 Programa de Mentoria: Machine Learning e MLOps em Produção

### Este repositório é desenvolvido sob a tutoria especializada de Manoel Veríssimo. Ele serve como o hub central para o meu programa de desenvolvimento e portfólio prático em Machine Learning (ML) e MLOps (Machine Learning Operations)

O objetivo deste programa é fazer uma transição robusta e prática, focando em como construir, versionar e sustentar modelos de ML em ambientes de produção, integrando minha experiência prévia em DataOps e Qualidade.

🎯 Por Que MLOps?

Minha atuação em **Qualidade de Dados (QD)** no setor financeiro me deu uma visão clara: entendi que o **maior gargalo de valor e impacto** não está apenas na modelagem, mas sim na **produtização robusta, segura e escalável** dos modelos – o núcleo da EML.

Este programa me capacita com as habilidades de engenharia necessárias para:

* **Sustentabilidade de Modelo:** Corrigir falhas operacionais (*Schema Drift*, *Data Drift*) no pipeline de produção.
* **Desenvolvimento Robusto:** Construir código limpo e versionado, garantindo a reprodutibilidade.
* **Otimização de Performance:** Entregar modelos que rodam com segurança e baixa latência.

Minha meta é atuar como uma Engenheira de ML que, futuramente, utilizará essa visão de produção para se tornar uma Cientista de Dados de altíssimo impacto.

🧠 Estrutura da Tutoria
O programa está dividido em módulos temáticos, seguindo a jornada completa de um projeto de ML, desde a concepção até a sustentação:

🛠️ Stack Principal
<p align="left"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/> <img src="https://img.shields.io/badge/Jupyter%20Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Badge"/> <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn Badge"/> <img src="https://img.shields.io/badge/MLflow-009688?style=for-the-badge&logo=mlflow&logoColor=white" alt="MLFlow Badge"/> <img src="https://img.shields.io/badge/DVC-13B765?style=for-the-badge&logo=dvc&logoColor=white" alt="DVC Badge"/> </p>

Mentorada: Yasmin Correia 

Mentor Manoel Veríssimo 

Status: Concluída 📅

Projeto final: projeto-mkt-mle.zip
## 🚀 Resumo do Projeto Final: Otimização de Marketing (MII-D)

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

<img alt="image" src="https://github.com/user-attachments/assets/f85d9564-37eb-4c92-9cc0-46e0f212e03a" alt="Dashboard MII-D Proof of Concept" width="30%"/>

<div style="display: flex; justify-content: space-between; gap: 20px; flex-wrap: wrap;">

    <div style="flex: 1; min-width: 30%; max-width: 33%;">
        
        ### 📊 Métrica de Performance
        
        Nossa modelagem priorizou o **F1-Score (0.4562)** em vez da acurácia. Isso garante um balanço entre:
        
        * **Recall (77%):** Capturar a maioria dos sucessos reais (evitando a perda de receita).
        * **Precisão (32%):** Evitar falsos positivos (evitando investimentos caros em projetos ruins).
        
    </div>

    <div style="flex: 1; min-width: 30%; max-width: 33%; text-align: center;">
        
        ### 🖼️ Prova de Conceito
        
        <img 
            src="URL_DA_SUA_IMAGEM_AQUI" 
            alt="Dashboard MII-D App" 
            width="100%"
            style="border-radius: 8px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);"
        />
        
    </div>

    <div style="flex: 1; min-width: 30%; max-width: 33%;">
        
        ### 🚀 Deployment (MLOps)
        
        O modelo foi empacotado em **Contêiner Docker** e servido via **FastAPI** para alta performance.
        
        * **TTV:** Demonstra **Time to Value** rápido.
        * **Consumo:** Integrado a um dashboard **PoC (FlutterFlow)** para uso imediato do Marketing.
        
    </div>

</div>
