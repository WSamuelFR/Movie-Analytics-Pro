import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def carregar_e_limpar_dados(caminho_csv):
    # Lendo o CSV
    df = pd.read_csv(caminho_csv, na_values='NA')

    # 1. Tratamento de nulos
    df['average_rating'] = df['average_rating'].fillna(df['average_rating'].mean())
    df['runtime_minutes'] = df['runtime_minutes'].fillna(df['runtime_minutes'].median())
    df['num_votes'] = df['num_votes'].fillna(0)
    df['genres'] = df['genres'].fillna('Others')

    # 2. Extração da Categoria (Gênero Principal)
    # Pegamos apenas o primeiro gênero da lista (ex: "Comedy, Romance" -> "Comedy")
    df['categoria'] = df['genres'].str.split(',').str[0]

    # 3. Encoding: Transformar texto em números (Ex: Comedy=1, Drama=2...)
    le = LabelEncoder()
    df['categoria_encoded'] = le.fit_transform(df['categoria'])

    # 4. Garantindo tipos numéricos
    df['runtime_minutes'] = df['runtime_minutes'].astype(int)
    df['num_votes'] = df['num_votes'].astype(int)
    df['average_rating'] = df['average_rating'].astype(float)

    return df, le # Retornamos o DataFrame e o codificador para usar na interface depois