import sys
import os
import joblib
from sklearn.tree import DecisionTreeClassifier

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.data_processor import carregar_e_limpar_dados

def treinar_arvore_decisao():
    df, le = carregar_e_limpar_dados('data/summer_movies.csv')

    # Criando o alvo: 1 para notas >= 7.0, 0 para menores
    df['label_avaliacao'] = (df['average_rating'] >= 7.0).astype(int)

    # Incluindo a categoria no treino
    X = df[['runtime_minutes', 'num_votes', 'categoria_encoded']]
    y = df['label_avaliacao']

    clf = DecisionTreeClassifier(max_depth=5, random_state=42)
    clf.fit(X, y)

    joblib.dump(clf, 'models/tree_model.pkl')
    
    return clf.score(X, y)

if __name__ == "__main__":
    acuracia = treinar_arvore_decisao()
    print(f"✅ Árvore de Decisão atualizada com categorias!")
    print(f"🎯 Nova Acurácia: {acuracia:.4f}")