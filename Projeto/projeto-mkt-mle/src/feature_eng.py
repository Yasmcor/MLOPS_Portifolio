import pandas as pd
import numpy as np
from typing import List
# Importando a função de limpeza e target 
from .data_cleaner import create_target_and_clean 
# Importando a função de carregamento
from .data_loader import load_data 

def generate_features(df_clean: pd.DataFrame) -> pd.DataFrame:
    """
    Cria features de tempo e de categorias (gêneros e idiomas).

    Args:
        df_clean: DataFrame limpo, sem Data Leakage, com a coluna Success_Flag.
    
    Returns:
        DataFrame com novas colunas de features prontas para o modelo.
    """
    
    df_features = df_clean.copy()
    
    # 1. FEATURES TEMPORAIS (SAZONALIDADE)
    
    # Converte para datetime para extrair dados
    df_features['Release_Date'] = pd.to_datetime(df_features['Release_Date'])
    
    # Extrai o mês (sazonalidade de marketing - ex: Natal, Férias)
    df_features['release_month'] = df_features['Release_Date'].dt.month
    
    # Extrai o dia da semana (marketing em um fim de semana vs. dia de semana)
    # 0 = Segunda-feira, 6 = Domingo
    df_features['release_dayofweek'] = df_features['Release_Date'].dt.dayofweek
    
    # Remove a coluna original de data
    df_features.drop(columns=['Release_Date'], inplace=True)
    print("✅ Features temporais (Mês, Dia da Semana) criadas com sucesso.")

    # 2. FEATURES CATEGÓRICAS COMPLEXAS (GENRE)
    
    # Usa a função str.get_dummies para criar uma coluna binária para cada gênero.
    df_genres_dummies = df_features['Genre'].str.get_dummies(sep=', ')
    
    # Concatena as novas colunas e remove a coluna de texto original 'Genre'
    df_features = pd.concat([df_features, df_genres_dummies], axis=1)
    df_features.drop(columns=['Genre'], inplace=True)
    print(f"✅ One-Hot Encoding de Gênero aplicado. Total de gêneros: {df_genres_dummies.shape[1]}")

    # 3. FEATURES CATEGÓRICAS SIMPLES (IDIOMA)
    
    # Aplica One-Hot Encoding no idioma original. 
    # drop_first=True evita multicolinearidade
    df_features = pd.get_dummies(
        df_features, 
        columns=['Original_Language'], 
        drop_first=True,
        dtype=int
    )
    print(f"✅ One-Hot Encoding de Idioma aplicado. Total de idiomas: {df_features.filter(regex='Original_Language').shape[1]}")

    return df_features

if __name__ == '__main__':
    # Bloco de teste: Executa a Sprint 1 e 2 antes de si
    print("--- Teste de módulo de feature engineering ---")
    
    df_raw = load_data(source_type='local') 
    df_clean = create_target_and_clean(df_raw)
    
    df_final = generate_features(df_clean)
    
    print("\nSanity Check Final:")
    print(f"Dimensão Final do DataFrame: {df_final.shape}")
    print(f"Número total de features criadas: {df_final.shape[1]}")
