import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Predição de Sucesso", page_icon="🤖")

st.title("🤖 Predição de Sucesso com IA")

# Carregar os modelos e o encoder salvos anteriormente
try:
    knn = joblib.load('models/knn_model.pkl')
    tree = joblib.load('models/tree_model.pkl')
    le = joblib.load('models/label_encoder.pkl')

    st.sidebar.header("Parâmetros do Filme")
    
    # Interface de entrada (Substituindo os formulários HTML do PHP)
    categoria = st.sidebar.selectbox("Selecione o Gênero", le.classes_)
    duracao = st.sidebar.slider("Duração (Minutos)", 30, 240, 90)
    votos = st.sidebar.number_input("Número de Votos Estimados", min_value=0, value=1000)

    if st.button("Executar Modelos"):
        # Preparar os dados para predição
        cat_encoded = le.transform([categoria])[0]
        entrada = np.array([[duracao, votos, cat_encoded]])

        # Executar Predições
        nota_prevista = knn.predict(entrada)[0]
        classificacao = tree.predict(entrada)[0]

        # Exibir Resultados
        col1, col2 = st.columns(2)
        
        with col1:
            st.info("### KNN (Regressão)")
            st.metric("Nota Esperada", f"{nota_prevista:.1f}")
        
        with col2:
            st.success("### Árvore (Classificação)")
            resultado = "Alta (>= 7.0)" if classificacao == 1 else "Baixa (< 7.0)"
            st.write(f"Categoria de Nota: **{resultado}**")

except Exception as e:
    st.error(f"Certifique-se de que os modelos foram treinados: {e}")