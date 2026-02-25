import streamlit as st
import plotly.express as px
import sys
import os

# Ajuste de path para encontrar o utils e importar os módulos necessários
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.data_processor import carregar_e_limpar_dados
from utils.export_manager import gerar_csv, gerar_pdf

# 1. Configuração da Página com Identidade WSistemas
st.set_page_config(page_title="WSistemas - Dashboard Analítico", page_icon="📊", layout="wide")

# Custom CSS para manter o padrão de design dos seus projetos recentes
st.markdown("""
    <style>
    .stMetric {
        background-color: #161b22;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #77d7ff;
    }
    div.stButton > button:first-child {
        width: 100%;
        border-radius: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown("# 🚀 WSistemas")
st.sidebar.subheader("Painel de Controle")

st.title("📊 Dashboard de Análise de Filmes")
st.caption("Desenvolvido por WSistemas")

try:
    # 2. Carregamento dos Dados
    df, _ = carregar_e_limpar_dados('data/summer_movies.csv')

    # 3. Barra Lateral - Filtros Dinâmicos
    st.sidebar.divider()
    
    generos_selecionados = st.sidebar.multiselect(
        "Filtrar por Gênero", 
        options=df['categoria'].unique(),
        default=df['categoria'].unique()[:3]
    )
    
    nota_minima = st.sidebar.slider("Avaliação Mínima", 0.0, 10.0, 5.0)
    
    anos = sorted(df['year'].unique())
    ano_limite = st.sidebar.select_slider(
        "Período (Anos)",
        options=anos,
        value=(min(anos), max(anos))
    )

    # Aplicação dos Filtros no DataFrame
    df_filtrado = df[
        (df['categoria'].isin(generos_selecionados)) &
        (df['average_rating'] >= nota_minima) &
        (df['year'].between(ano_limite[0], ano_limite[1]))
    ]

    # 4. Seção de Exportação (Nova Funcionalidade)
    st.sidebar.divider()
    st.sidebar.subheader("📥 Exportar Relatórios")
    
    # Exportação CSV
    csv_data = gerar_csv(df_filtrado)
    st.sidebar.download_button(
        label="📄 Baixar Planilha (CSV)",
        data=csv_data,
        file_name='analise_wsistemas.csv',
        mime='text/csv',
    )

    # Exportação PDF
    if st.sidebar.button("🛠️ Gerar Relatório PDF"):
        try:
            # Passamos os filtros em formato de texto para o relatório
            detalhes_filtros = f"Generos: {', '.join(generos_selecionados)} | Nota min: {nota_minima}"
            pdf_bytes = gerar_pdf(df_filtrado, detalhes_filtros)
            
            st.sidebar.download_button(
                label="📥 Baixar Relatório PDF",
                data=bytes(pdf_bytes),
                file_name="relatorio_final_wsistemas.pdf",
                mime="application/pdf"
            )
            st.sidebar.success("PDF pronto para download!")
        except Exception as e:
            st.sidebar.error(f"Erro ao processar PDF: {e}")

    # 5. Visualização das Métricas Principais
    m1, m2, m3 = st.columns(3)
    m1.metric("Filmes Encontrados", len(df_filtrado))
    m2.metric("Média de Notas", f"{df_filtrado['average_rating'].mean():.2f}")
    m3.metric("Total de Votos", f"{df_filtrado['num_votes'].sum():,}")

    # 6. Seleção de Modelos de Gráfico
    st.divider()
    tipo_grafico = st.selectbox(
        "Selecione a Visualização Desejada:",
        ["Dispersão: Votos vs Nota", "Barras: Nota Média por Gênero", 
         "Distribuição: Duração dos Filmes", "Linha: Tendência Temporal"]
    )

    # Renderização Condicional (Plotly)
    if tipo_grafico == "Dispersão: Votos vs Nota":
        fig = px.scatter(df_filtrado, x="num_votes", y="average_rating", 
                         color="categoria", hover_name="primary_title",
                         size="runtime_minutes", log_x=True,
                         template="plotly_dark", color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig, use_container_width=True)

    elif tipo_grafico == "Barras: Nota Média por Gênero":
        df_bar = df_filtrado.groupby('categoria')['average_rating'].mean().reset_index().sort_values('average_rating', ascending=False)
        fig = px.bar(df_bar, x='categoria', y='average_rating', color='average_rating',
                     template="plotly_dark", color_continuous_scale='Blues')
        st.plotly_chart(fig, use_container_width=True)

    elif tipo_grafico == "Distribuição: Duração dos Filmes":
        fig = px.histogram(df_filtrado, x="runtime_minutes", nbins=30,
                           template="plotly_dark", color_discrete_sequence=['#77d7ff'])
        st.plotly_chart(fig, use_container_width=True)

    elif tipo_grafico == "Linha: Tendência Temporal":
        df_line = df_filtrado.groupby('year')['average_rating'].mean().reset_index()
        fig = px.line(df_line, x='year', y='average_rating', 
                      template="plotly_dark", color_discrete_sequence=['#77d7ff'])
        st.plotly_chart(fig, use_container_width=True)

    # Exibição da Tabela de Dados
    with st.expander("🔍 Detalhes dos Dados Filtrados"):
        st.dataframe(df_filtrado, use_container_width=True)

except Exception as e:
    st.error(f"Erro na interface de gráficos: {e}")