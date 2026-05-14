# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:46:56 2026

@author: Vanilson Manuel
"""

from rapidfuzz import process


def pesquisar_filmes(
    termo_pesquisa,
    df,
    limite=5,
    score_minimo=60
):
    """
    Pesquisa filmes semelhantes usando RapidFuzz.
    """

    titulos = df["Movie Name"].tolist()

    resultados = process.extract(
        termo_pesquisa,
        titulos,
        limit=limite,
        score_cutoff=score_minimo
    )

    return resultados