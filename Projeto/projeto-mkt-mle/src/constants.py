#MLOps: ARQUIVO DE GOVERNANÇA DE FEATURES
# Contém as listas de colunas OHE que devem estar presentes no input da API (Inferência).

# Colunas que sobraram no DF ANTES da aplicação do ColumnTransformer
BASE_FEATURES = [
    'Title', 
    'Overview', 
    'Original_Language', 
    'Genre'
]

# Gêneros gerados no One-Hot Encoding (19 colunas)
GENRE_COLUMNS = [
    'Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 
    'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 
    'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 
    'TV Movie', 'Thriller', 'War', 'Western'
]

# Idiomas gerados no One-Hot Encoding (42 colunas - drop_first=True)
LANGUAGE_COLUMNS = [
    'Original_Language_bn', 'Original_Language_ca', 'Original_Language_cn', 
    'Original_Language_cs', 'Original_Language_da', 'Original_Language_de', 
    'Original_Language_el', 'Original_Language_en', 'Original_Language_es', 
    'Original_Language_et', 'Original_Language_eu', 'Original_Language_fa', 
    'Original_Language_fi', 'Original_Language_fr', 'Original_Language_he', 
    'Original_Language_hi', 'Original_Language_hu', 'Original_Language_id', 
    'Original_Language_is', 'Original_Language_it', 'Original_Language_ja', 
    'Original_Language_ko', 'Original_Language_lv', 'Original_Language_ml', 
    'Original_Language_ms', 'Original_Language_nb', 'Original_Language_nl', 
    'Original_Language_no', 'Original_Language_pl', 'Original_Language_pt', 
    'Original_Language_ro', 'Original_Language_ru', 'Original_Language_sr', 
    'Original_Language_sv', 'Original_Language_ta', 'Original_Language_te', 
    'Original_Language_th', 'Original_Language_tl', 'Original_Language_tr',
    'Original_Language_uk', 'Original_Language_zh', 'Original_Language_la', 
    'Original_Language_ur', 'Original_Language_ar'
] 

# Colunas criadas pelo Feature Engineering (Temporais)
TEMPORAL_COLUMNS = ['release_month', 'release_dayofweek']

# A lista completa de features
FINAL_FEATURE_COLUMNS = TEMPORAL_COLUMNS + GENRE_COLUMNS + LANGUAGE_COLUMNS
