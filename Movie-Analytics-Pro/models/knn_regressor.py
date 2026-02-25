import sys
import os
import joblib
from sklearn.neighbors import KNeighborsRegressor

# Adiciona a pasta raiz ao path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.data_processor import carregar_e_limpar_dados

def treinar_knn(k=3):
    # O processador agora retorna o DataFrame e o codificador de categorias
    df, le = carregar_e_limpar_dados('data/summer_movies.csv')

    # X agora inclui 'categoria_encoded'
    X = df[['runtime_minutes', 'num_votes', 'categoria_encoded']]
    y = df['average_rating']

    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(X, y)

    # Salvamos o modelo e o codificador (necessário para converter novas entradas)
    joblib.dump(knn, 'models/knn_model.pkl')
    joblib.dump(le, 'models/label_encoder.pkl')
    
    return knn.score(X, y)

if __name__ == "__main__":
    score = treinar_knn()
    print(f"✅ KNN atualizado com categorias e salvo!")
    print(f"📊 Nova Precisão (R²): {score:.4f}")