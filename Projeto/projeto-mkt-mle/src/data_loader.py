
import pandas as pd
import os
import zipfile
import subprocess
from pathlib import Path

# --- Variáveis de Configuração ---
# O MLOps Sênior centraliza configurações em variáveis, não em código espalhado.
KAGGLE_DATASET_ID = "disham993/9000-movies-dataset"
ZIP_FILENAME = "9000-movies-dataset.zip"
CSV_FILENAME = "mymoviedb.csv"
DATA_RAW_PATH = Path("data/raw") # Usamos pathlib para caminhos robustos

def load_data(source_type: str = 'local') -> pd.DataFrame:
    """
    Carrega o dataset de filmes. Prioriza a leitura local,
    mas pode baixar via API do Kaggle se necessário.

    Args:
        source_type: 'kaggle' para forçar download, ou 'local' para tentar carregar o CSV.
    
    Returns:
        Um DataFrame do Pandas contendo os dados brutos.
    """
    
    # Garante que a pasta de dados brutos exista
    DATA_RAW_PATH.mkdir(parents=True, exist_ok=True)
    
    file_path = DATA_RAW_PATH / CSV_FILENAME
    zip_path = DATA_RAW_PATH / ZIP_FILENAME

    if source_type == 'kaggle' or not file_path.exists():
        print(f"Buscando dados no Kaggle (ID: {KAGGLE_DATASET_ID}).")
        
        # 1. Download (Usando subprocess.run para simular o comando !kaggle)
        try:
            subprocess.run(
                ["kaggle", "datasets", "download", "-d", KAGGLE_DATASET_ID, "-p", DATA_RAW_PATH],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print("Download concluído.")
        except subprocess.CalledProcessError as e:
            print(f"ERRO: Falha ao baixar do Kaggle. Verifique a API Key e a instalação. Detalhes: {e.stderr.decode()}")
            raise
        except FileNotFoundError:
            print("ERRO: O comando 'kaggle' não foi encontrado. Certifique-se de que a API está instalada e configurada.")
            raise

        # 2. Descompactar
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(DATA_RAW_PATH)
            print(f"Arquivo descompactado em {DATA_RAW_PATH}.")
            
            # Opcional: remover o .zip após descompactar
            os.remove(zip_path)
        except FileNotFoundError:
            print("AVISO: Arquivo ZIP não encontrado após download. Tentando ler o CSV diretamente.")
            
        except Exception as e:
            print(f"ERRO ao descompactar: {e}")
            
    # 3. Carregar o CSV
    try:
        # Nota: O lineterminator='\n' é tecnicamente necessário para evitar erros de leitura no campo 'Overview'.
        df = pd.read_csv(file_path, lineterminator='\n')
        print(f"✅ Dados carregados com sucesso do arquivo: {file_path.resolve()}")
        print(f"Dimensão: {df.shape}")
        return df
    except FileNotFoundError:
        # Isso só deve acontecer se o download/descompactação falhou
        raise FileNotFoundError(f"CSV não encontrado em {file_path}. Verifique o processo de download.")
    except Exception as e:
        print(f"ERRO ao carregar o CSV: {e}")
        raise


if __name__ == '__main__':
    # Bloco para testar o script de forma isolada
    print("--- Teste de Módulo de Ingestão de Dados ---")
    
    # Exemplo de uso: Force o download uma vez ou use 'local' para reuso
    df_raw = load_data(source_type='local') 
    
    # Sanity Check
    print("\nSanity Check (5 primeiras linhas):")
    print(df_raw.head())
