import streamlit as st
import pandas as pd
import sys
import os

# Caminho para o processador
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.data_processor import carregar_e_limpar_dados

st.set_page_config(page_title="WSistemas - Movie Analytics", layout="wide", page_icon="🎬")

# --- CUSTOM CSS PARA DESIGN ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.stButton > button:first-child {
        background-color: #77d7ff;
        color: #0e1117;
        border-radius: 10px;
        font-weight: bold;
    }
    .stMetric {
        background-color: #161b22;
        padding: 15px;
        border-radius: 15px;
        border: 1px solid #77d7ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGO E TÍTULO ---
st.sidebar.markdown("# 🚀 WSistemas")
st.sidebar.markdown("---")

st.title("🎬 Movie Analytics Pro")
st.subheader("by WSistemas")

# Restante do seu código de carregamento e métricas...
try:
    df, _ = carregar_e_limpar_dados('data/summer_movies.csv')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Filmes", len(df))
    with col2:
        st.metric("Média de Notas", round(df['average_rating'].mean(), 2))
    with col3:
        st.metric("Gêneros", df['categoria'].nunique())

    st.divider()
    st.dataframe(df.head(15), use_container_width=True)

except Exception as e:
    st.error(f"Erro: {e}")