import joblib
import pandas as pd
import datetime
from typing import Dict, Union, Any
import sys
import os

MODEL_PATH = "model/model.pkl" 

try:
    # Carrega o modelo/pipeline serializado
    # O joblib é mais seguro para modelos do scikit-learn
    LOADED_MODEL = joblib.load(MODEL_PATH)
    print(f"✅ INFO: Modelo carregado com sucesso de: {MODEL_PATH}")
except Exception as e:
    # Se falhar ao carregar o modelo, o processo morre e o log mostrará a mensagem
    print(f"❌ ERRO CRÍTICO: Falha ao carregar o modelo de {MODEL_PATH}. Erro: {e}")
    sys.exit(1) # Força a saída do contêiner

# --- Variáveis (Devem ser carregadas ou definidas, assumindo as colunas finais) ---

FINAL_FEATURE_COLUMNS = [
    # 1. Colunas Numéricas/FE (8 Colunas) - Devem vir PRIMEIRO!
    'runtime', 'num_cast', 'num_crew', 'release_year', 'overview_wc', 'tagline_wc', 
    'release_month', 'release_dayofweek',
    
    # 2. O RESTO DAS COLUNAS OHE (As 61 Colunas Copiadas do seu Terminal)
    'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 
    'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 
    'TV Movie', 'Thriller', 'War', 'Western', 'Original_Language_bn', 'Original_Language_ca',
    'Original_Language_cn', 'Original_Language_cs', 'Original_Language_da',
    'Original_Language_de', 'Original_Language_el', 'Original_Language_en',
    'Original_Language_es', 'Original_Language_et', 'Original_Language_eu',
    'Original_Language_fa', 'Original_Language_fi', 'Original_Language_fr',
    'Original_Language_he', 'Original_Language_hi', 'Original_Language_hu',
    'Original_Language_id', 'Original_Language_is', 'Original_Language_it',
    'Original_Language_ja', 'Original_Language_ko', 'Original_Language_la',
    'Original_Language_lv', 'Original_Language_ml', 'Original_Language_ms',
    'Original_Language_nb', 'Original_Language_nl', 'Original_Language_no',
    'Original_Language_pl', 'Original_Language_pt', 'Original_Language_ro',
    'Original_Language_ru', 'Original_Language_sr', 'Original_Language_sv',
    'Original_Language_ta', 'Original_Language_te', 'Original_Language_th',
    'Original_Language_tl', 'Original_Language_tr', 'Original_Language_uk',
    'Original_Language_zh'
]

def prepare_single_input(data: Dict[str, Union[str, int, float]]) -> pd.DataFrame:
    """
    Cria o DataFrame de entrada com todas as 63 colunas esperadas pelo ColumnTransformer.
    """
    # 1. Cria um DataFrame de 1 linha e insere valores padrão/nulos
    df_single = pd.DataFrame([data])
    
    # 2. FEATURE ENGINEERING BÁSICO
    df_single['Release_Date'] = pd.to_datetime(df_single['Release_Date'])
    df_single['release_month'] = df_single['Release_Date'].dt.month.astype(int)
    df_single['release_dayofweek'] = df_single['Release_Date'].dt.dayofweek.astype(int)
    
    # Adicionando contagens simples (Assumindo que estas colunas existem na entrada)
    df_single['runtime'] = df_single.get('runtime', [90]) 
    df_single['num_cast'] = df_single.get('num_cast', [5]) 
    df_single['num_crew'] = df_single.get('num_crew', [5]) 
    df_single['release_year'] = df_single['Release_Date'].dt.year.astype(int)
    df_single['overview_wc'] = df_single['Overview'].apply(lambda x: len(str(x).split()))
    df_single['tagline_wc'] = df_single['Overview'].apply(lambda x: len(str(x).split())) # Reuso Overview para simplificar
    
    # 3. CRIAÇÃO MANUAL DAS COLUNAS DUMMIES (GENRE e LANGUAGE)
    
    # Inicia todas as colunas OHE como 0
    for col in FINAL_FEATURE_COLUMNS:
        if col not in df_single.columns:
            df_single[col] = 0

    # a) OHE dos Gêneros (Suporta múltiplos gêneros separados por vírgula)
    if 'Genre' in df_single.columns:
        genres = str(df_single['Genre'].iloc[0]).split(', ')
        for genre in genres:
            if genre in FINAL_FEATURE_COLUMNS:
                df_single[genre] = 1

    # b) OHE do Idioma
    if 'Original_Language' in df_single.columns:
        lang_col = f"Original_Language_{df_single['Original_Language'].iloc[0]}"
        if lang_col in FINAL_FEATURE_COLUMNS:
            df_single[lang_col] = 1

    # 4. Retorna apenas as colunas que o modelo espera
    return df_single[FINAL_FEATURE_COLUMNS]


def predict_success(data: Dict[str, Union[str, int, float]]) -> Dict[str, Any]:
    """
    Recebe o dicionário de entrada, pré-processa e retorna a predição.
    """
    # 1. Preparar entrada (cria as 63 colunas)
    input_df = prepare_single_input(data)
    
    # 2. Predição
    # O pipeline treinado fará o scaling/vectorization e a predição
    probability = LOADED_MODEL.predict_proba(input_df)[0, 1]
    
    # 3. Recomendação de Risco
    
    if probability >= 0.80:
        recommendation = "SUCESSO"
    elif probability >= 0.50:
        recommendation = "MEDIO RISCO"
    else:
        recommendation = "ALTO RISCO"

    return {
        "probability": round(probability, 3),
        "recommendation": recommendation,
        "prediction_time": datetime.datetime.now().isoformat()
    }
