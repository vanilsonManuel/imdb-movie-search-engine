# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:44:11 2026

@author: pt
"""

import pandas as pd


def carregar_dados(caminho_csv):
    try:
        return pd.read_csv(caminho_csv)
    except FileNotFoundError:
        return None


def limpar_dados(df):
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])

    df = df.dropna(subset=["Movie Name"])

    df["Year of Release"] = (
        df["Year of Release"]
        .astype(str)
        .str.extract(r"(\d{4})")
    )

    df["Year of Release"] = pd.to_numeric(
        df["Year of Release"],
        errors="coerce"
    )

    df["Description"] = df["Description"].fillna("Sem descrição disponível.")
    df["Movie Rating"] = df["Movie Rating"].fillna(0)
    df["Watch Time"] = df["Watch Time"].fillna(0)

    return df