import pandas as pd
import numpy as np
from typing import Tuple, List

# --- Constantes de controle ---
# DEFINIÇÃO DAS FEATURES INVÁLIDAS PARA O MODELO (DATA LEAKAGE)
# Estas colunas não existem antes do lançamento do filme e DEVEM ser removidas das features.
POST_RELEASE_LEAKAGE = [
    'Popularity', 
    'Vote_Count', 
    'Vote_Average'
]

# PARÂMETROS DE NEGÓCIO PARA DEFINIR SUCESSO
VOTE_QUANTILE = 0.75 # Limite de relevância: Acima do 75% dos filmes em termos de votos
VOTE_AVG_MIN = 6.0   # Limite de qualidade: Nota mínima para ser considerado sucesso


def create_target_and_clean(df_raw: pd.DataFrame) -> pd.DataFrame:
    """
    Cria a variável alvo (Success_Flag) e remove features que causariam Data Leakage.

    Args:
        df_raw: DataFrame bruto carregado do data_loader.
    
    Returns:
        DataFrame limpo, com a coluna 'Success_Flag' e apenas features válidas.
    """
    
    df_clean = df_raw.copy()
    
    # 1. TRATAMENTO DE NULOS (Estratégia do seu EDA original)
    df_clean.dropna(subset=['Title', 'Release_Date'], inplace=True)
    
    # CORREÇÃO PANDAS WARNING: Atribuição direta para evitar SettingWithCopyWarning
    df_clean.loc[:, 'Overview'] = df_clean['Overview'].fillna('SEM DESCRIÇÃO')
    df_clean.loc[:, 'Genre'] = df_clean['Genre'].fillna('Unknown')
    
    # 2. FEATURE ENGINEERING: CRIAÇÃO DO ALVO (SUCCESS_FLAG)
    # Calcule o limite de votos (P75). 
    limite_votos = np.quantile(df_clean['Vote_Count'], VOTE_QUANTILE)
    
    # Aplicação da lógica de Sucesso/Fracasso (Regra: Votos >= P75 E Nota >= 6.0)
    # Esta é uma métrica de negócio robusta, não apenas uma nota arbitrária.
    df_clean['Success_Flag'] = np.where(
        (df_clean['Vote_Count'] >= limite_votos) & 
        (df_clean['Vote_Average'] >= VOTE_AVG_MIN), 
        1, 
        0
    )
    print(f"✅ Variável Alvo 'Success_Flag' criada (Limite Votos: {limite_votos:.0f}, Nota Mínima: {VOTE_AVG_MIN}).")
    print(f"Distribuição do Alvo: 1 (Sucesso) = {df_clean['Success_Flag'].mean() * 100:.2f}%")
    
    # 3. CORREÇÃO CRÍTICA DE DATA LEAKAGE
    # Remove as colunas que não estariam disponíveis no momento da predição
    df_clean.drop(columns=POST_RELEASE_LEAKAGE, inplace=True)
    df_clean.drop(columns=['Poster_Url'], inplace=True) # URL é irrelevante
    
    print("🛑 Colunas de Data Leakage (Popularity, Vote_Count, Vote_Average) removidas das Features.")
    # Bloco de Otimização de Memória (Downcasting)
    print("✅ Aplicando downcasting para otimização de memória...")
    
    df_clean['Success_Flag'] = df_clean['Success_Flag'].astype('int8')
    df_clean['Original_Language'] = df_clean['Original_Language'].astype('category')

    return df_clean

if __name__ == '__main__':
    # Bloco de Teste: Executado apenas quando roda 'python data_cleaner.py'
    from data_loader import load_data 
    
    print("--- Teste de Módulo de Limpeza e criação do Alvo ---")
    df_raw = load_data(source_type='local') 
    
    df_processed = create_target_and_clean(df_raw)
    
    print("\nSanity Check (Shape e Colunas):")
    print(f"Dimensão do dataFrame limpo: {df_processed.shape}")
    
    # Verificação final: se essas colunas NÃO existirem, está correto!
    cols_check = [col for col in POST_RELEASE_LEAKAGE if col in df_processed.columns]
    if not cols_check:
        print("🎉 Verificação de Leakage OK. As features inválidas não existem mais no DataFrame.")
    else:
        print(f"ERRO: As colunas de Leakage ainda estão presentes: {cols_check}")
