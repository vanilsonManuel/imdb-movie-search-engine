# -*- coding: utf-8 -*-
"""
Projeto Final - Search Engine de Filmes do IMDb
Autor: Vanilson Manuel
"""

import streamlit as st

from src.preprocess import carregar_dados, limpar_dados
from src.search_engine import pesquisar_filmes


def configurar_pagina():
    st.set_page_config(
        page_title="IMDb Movies Search Engine",
        page_icon="🎬",
        layout="wide"
    )


def mostrar_resultados(resultados, df):
    if resultados:
        st.subheader("🎬 Resultados encontrados")

        for titulo, score, indice in resultados:
            filme = df.iloc[indice]

            with st.container():
                st.markdown("---")
                st.markdown(f"### 🎞️ {filme['Movie Name']}")
                st.write(f"📅 **Ano:** {filme['Year of Release']}")
                st.write(f"⭐ **Rating IMDb:** {filme['Movie Rating']}")
                st.write(f"⏱️ **Duração:** {filme['Watch Time']} minutos")
                st.write(f"🧠 **Similaridade:** {score:.1f}%")
                st.write(f"📝 **Descrição:** {filme['Description']}")
    else:
        st.warning("Nenhum filme encontrado. Tenta escrever de outra forma.")


def main():

    configurar_pagina()

    st.title("🎬 IMDb Movies Search Engine")

    st.write(
        "Pesquisa inteligente de filmes usando Python, Pandas, RapidFuzz e Streamlit."
    )

    caminho_csv = "data/top_1000_imdb_movies.csv"

    df = carregar_dados(caminho_csv)

    if df is None:
        st.error("Erro ao carregar dataset.")
        return

    df = limpar_dados(df)

    # =========================
    # SIDEBAR
    # =========================

    st.sidebar.title("🎬 IMDb Search Engine")

    st.sidebar.markdown("---")

    st.sidebar.write("Projeto Final - Master D")

    st.sidebar.write("Desenvolvido por Vanilson Manuel")

    st.sidebar.markdown("---")

    st.sidebar.subheader("📊 Estatísticas")

    st.sidebar.write(f"Total de filmes: {len(df)}")

    st.sidebar.write(
        f"Rating médio: {df['Movie Rating'].mean():.1f}"
    )

    # =========================
    # PREVIEW DOS DADOS
    # =========================

    with st.expander(
        "📊 Ver pré-visualização dos dados tratados"
    ):
        st.dataframe(df.head())

    # =========================
    # PESQUISA
    # =========================

    pesquisa = st.text_input(
        "🔎 Escreve o nome do filme:",
        placeholder="Exemplo: Hary Ptter"
    )

    if pesquisa:

        resultados = pesquisar_filmes(
            pesquisa,
            df
        )

        mostrar_resultados(
            resultados,
            df
        )


if __name__ == "__main__":
    main()
    

 
    
    