import pandas as pd
from fpdf import FPDF
import io

def gerar_csv(df):
    """Converte o DataFrame filtrado em CSV para download."""
    return df.to_csv(index=False).encode('utf-8')

def gerar_pdf(df, filtros_aplicados):
    """Gera um relatório PDF com a marca WSistemas."""
    pdf = FPDF()
    pdf.add_page()
    
    # Cabeçalho WSistemas
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "WSistemas - Relatório de Análise de Filmes", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"Filtros aplicados: {filtros_aplicados}", ln=True, align='C')
    pdf.ln(10)
    
    # Resumo das Métricas
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Resumo do Dataset Filtrado:", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, f"- Total de Filmes: {len(df)}", ln=True)
    pdf.cell(0, 10, f"- Media de Avaliacao: {df['average_rating'].mean():.2f}", ln=True)
    pdf.ln(5)

    # Tabela Simples (Top 10 Filmes)
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(80, 10, "Titulo do Filme", 1)
    pdf.cell(30, 10, "Ano", 1)
    pdf.cell(30, 10, "Nota", 1)
    pdf.ln()

    pdf.set_font("Arial", size=9)
    for i, row in df.head(15).iterrows():
        # Limpar caracteres especiais para evitar erro no PDF básico
        titulo = str(row['primary_title'])[:40]
        pdf.cell(80, 10, titulo, 1)
        pdf.cell(30, 10, str(row['year']), 1)
        pdf.cell(30, 10, str(row['average_rating']), 1)
        pdf.ln()

    return pdf.output(dest='S') # Retorna como string/bytes