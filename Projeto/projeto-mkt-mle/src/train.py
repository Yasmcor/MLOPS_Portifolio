import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score

# --- MLOps: RASTREAMENTO DE EXPERIMENTOS ---
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature # <-- NOVO
from mlflow.models.signature import ModelSignature   # <-- NOVO

# --- Importa as funções das Sprints anteriores ---
from data_loader import load_data 
from data_cleaner import create_target_and_clean
from feature_eng import generate_features

# CONFIGURAÇÃO MLflow 
EXPERIMENT_NAME = "movie_success_prediction_base"


def train_model():
    """
    Executa o pipeline completo: Carga -> Limpeza/Target -> Features -> Split -> Treino/Avaliação com MLflow.
    """
    
    # 1. INGESTÃO DE DADOS
    print("--- 1. INGESTÃO DE DADOS ---")
    df_raw = load_data(source_type='local') 

    # 2. LIMPEZA E CRIAÇÃO DO ALVO
    print("\n--- 2. LIMPEZA E CRIAÇÃO DO ALVO ---")
    df_clean = create_target_and_clean(df_raw)
    
    # 3. ENGENHARIA DE FEATURES
    print("\n--- 3. ENGENHARIA DE FEATURES (Sprint 3) ---")
    df_final = generate_features(df_clean)

    # 4. PREPARAÇÃO PARA O SPLIT
    Y = df_final['Success_Flag']
    
    # Features X: Remove colunas não preditoras
    X = df_final.drop(columns=['Success_Flag', 'Title', 'Overview']) 
    
    print(f"\nDimensão de X (Features Prontas): {X.shape}")

    # 5. SPLIT TREINO/TESTE
    # Usando stratify=Y para manter a proporção de Sucesso em ambos os conjuntos.
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.3, random_state=42, stratify=Y
    )
    print(f"✅ Split Treino/Teste concluído. Proporção treino: {X_train.shape[0]} linhas.")

    # 6. DEFINIÇÃO DO PIPELINE DE PRÉ-PROCESSAMENTO (ColumnTransformer)
    
    # Colunas Numéricas (para Standard Scaler)
    numeric_features = ['release_month', 'release_dayofweek']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features)
        ],
        remainder='passthrough' # Mantém todas as colunas dummy (Gêneros e Idiomas)
    )

    # 7. CRIAÇÃO DO PIPELINE COMPLETO
    # ADICIONANDO class_weight='balanced' para melhorar o RECALL da classe minoritária (Sucesso)
    model_pipeline = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression(
            random_state=42, 
            solver='liblinear', 
            class_weight='balanced' # <-- OTIMIZAÇÃO CRÍTICA DE ML
        )) 
    ])

    # --- Rastreamento com MLflow (Inicia o Experimento) ---
    with mlflow.start_run(run_name="Weighted_Logistic_Regression_Otimizado") as run:
        
        # 8. TREINAMENTO
        print("\n--- 8. TREINAMENTO DO MODELO (Logistic Regression - Weighted) ---")
        model_pipeline.fit(X_train, Y_train)

        # 9. AVALIAÇÃO
        Y_pred = model_pipeline.predict(X_test)
        
        metrics = {
            'accuracy': accuracy_score(Y_test, Y_pred),
            'precision': precision_score(Y_test, Y_pred, zero_division=0),
            'recall': recall_score(Y_test, Y_pred, zero_division=0),
            'f1_score': f1_score(Y_test, Y_pred, zero_division=0)
        }

        print("✅ Treinamento concluído. Avaliação no conjunto de teste:")
        for metric, value in metrics.items():
            print(f"   - {metric.capitalize()}: {value:.4f}")
            mlflow.log_metric(metric, value) # Rastreia as métricas no MLflow

        # Rastreia parâmetros e salva o pipeline completo como artefato
        mlflow.log_param("model_type", "LogisticRegression")
        mlflow.log_param("class_weight", "balanced")
        mlflow.log_param("threshold_votos", 1376)
        
        # --- CORREÇÃO WARNING MLflow (Tipagem) ---
        
        # 1. Cria o input_example
        input_example = X_train.head(5) 
        
        # 2. Inferir a assinatura completa do modelo
        signature = infer_signature(model_input=X_train, model_output=Y_pred)
        
        # 3. Loga o modelo, passando o input_example e a signature
        mlflow.sklearn.log_model(
            model_pipeline, 
            "model", 
            input_example=input_example,
            signature=signature # <-- NOVO PARÂMETRO
        ) 
        
        print(f"\n✅ MLflow Tracking Concluído. Run ID: {run.info.run_id}")

        return model_pipeline, metrics


if __name__ == '__main__':
    # Define o nome do experimento
    mlflow.set_experiment(EXPERIMENT_NAME)
    model, metrics = train_model()
    print("\n--- FIM DO PIPELINE ---")
