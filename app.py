# -*- coding: utf-8 -*-

"""
Projeto Final - Mecanismo de Busca de Filmes IMDb
Autor: Vanilson Manuel
"""

import streamlit as st

from src.preprocess import carregar_dados, limpar_dados
from src.search_engine import pesquisar_filmes


# ==================================================
# CONFIGURAÇÃO DA PÁGINA
# ==================================================

st.set_page_config(
    page_title="IMDb Movie Search Engine",
    page_icon="🎬",
    layout="wide"
)


# ==================================================
# FUNÇÃO PARA MOSTRAR RESULTADOS
# ==================================================

def mostrar_resultados(resultados, df):

    if resultados:

        st.subheader("🎯 Resultados encontrados")

        for titulo, score, indice in resultados:

            filme = df.iloc[indice]

            with st.container():

                st.markdown("---")

                col1, col2 = st.columns([3, 1])

                with col1:

                    st.markdown(f"## 🎬 {filme['Movie Name']}")

                    st.write(f"📅 Ano: {filme['Year of Release']}")
                    st.write(f"⭐ Rating IMDb: {filme['Movie Rating']}")
                    st.write(f"⏱️ Duração: {filme['Watch Time']} min")
                    st.write(f"🎯 Similaridade: {score}%")

                with col2:

                    st.metric(
                        label="IMDb Rating",
                        value=f"{filme['Movie Rating']}"
                    )

                st.write("📝 Descrição:")
                st.info(filme['Description'])

    else:
        st.warning("❌ Nenhum filme encontrado.")


# ==================================================
# FUNÇÃO PRINCIPAL
# ==================================================

def main():

    # -------------------------
    # TÍTULO PRINCIPAL
    # -------------------------

    st.title("🎬 Mecanismo de busca de filmes do IMDb")

    st.markdown(
        """
        Pesquisa inteligente de filmes usando Python,
        Pandas, RapidFuzz e Streamlit.
        """
    )

    # -------------------------
    # CARREGAR DADOS
    # -------------------------

    try:

        df = carregar_dados("data/top_1000_imdb_movies.csv")
        df = limpar_dados(df)

        st.success("✅ Conjunto de dados carregado com sucesso!")

    except Exception as erro:

        st.error(f"Erro ao carregar os dados: {erro}")
        return

    # -------------------------
    # SIDEBAR
    # -------------------------

    st.sidebar.title("🎬 Mecanismo de busca do IMDb")

    st.sidebar.markdown("---")

    st.sidebar.write("Projeto Final - Master D")
    st.sidebar.write("Desenvolvido por Vanilson Manuel")

    st.sidebar.markdown("---")

    st.sidebar.subheader("📊 Estatísticas")

    st.sidebar.write(f"Total de filmes: {len(df)}")

    media_rating = round(df["Movie Rating"].mean(), 1)

    st.sidebar.write(f"Classificação média: {media_rating}")

    st.sidebar.markdown("---")

    # -------------------------
    # FILTROS
    # -------------------------

    st.sidebar.subheader("🎛️ Filtros")

    rating_minimo = st.sidebar.slider(
        "⭐ Rating mínimo",
        0.0,
        10.0,
        7.0
    )

    ano_minimo = st.sidebar.slider(
        "📅 Ano mínimo",
        int(df["Year of Release"].min()),
        int(df["Year of Release"].max()),
        2000
    )

    numero_resultados = st.sidebar.selectbox(
        "📌 Número de resultados",
        [5, 10, 15, 20]
    )

    # -------------------------
    # PRÉ-VISUALIZAÇÃO DOS DADOS
    # -------------------------

    with st.expander("📊 Ver pré-visualização dos dados tratados"):

        st.dataframe(df.head())

    # -------------------------
    # PESQUISA
    # -------------------------

    st.write("🔎 Pesquisa filme:")

    pesquisa = st.text_input(
        "",
        placeholder="Exemplo: Harry Potter"
    )

    # -------------------------
    # EXECUTAR PESQUISA
    # -------------------------

    if pesquisa:

        resultados = pesquisar_filmes(
            pesquisa,
            df,
            limite=numero_resultados
        )

        # Aplicar filtros

        resultados_filtrados = []

        for titulo, score, indice in resultados:

            filme = df.iloc[indice]

            if (
                filme["Movie Rating"] >= rating_minimo
                and filme["Year of Release"] >= ano_minimo
            ):

                resultados_filtrados.append(
                    (titulo, score, indice)
                )

        mostrar_resultados(resultados_filtrados, df)


# ==================================================
# EXECUTAR APP
# ==================================================

if __name__ == "__main__":
    main()

 
    
    