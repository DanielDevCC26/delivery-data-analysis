import pandas as pd
import numpy as np


pedidos = pd.read_csv("pedidos.csv")

# Análise exploratória
print("\n--- PRIMEIRAS LINHAS ---")
print(pedidos.head())

print("\n--- ÚLTIMAS LINHAS ---")
print(pedidos.tail())

print("\n--- INFORMAÇÕES DO DATASET ---")
pedidos.info()

print("\n--- ESTATÍSTICAS DESCRITIVAS ---")
print(pedidos.describe())

print("\n--- DIMENSÕES DO DATASET ---")
print(f"Registros: {pedidos.shape[0]}")
print(f"Colunas: {pedidos.shape[1]}")

print("\n--- NOMES DAS COLUNAS ---")
print(pedidos.columns.tolist())

print("\n--- TIPOS DE DADOS ---")
print(pedidos.dtypes)


# Criação da coluna de receita
pedidos["Receita_Item"] = pedidos["Quantidade"] * pedidos["Preco_Unitario"]

print("\n--- RECEITA POR ITEM ---")
print(pedidos[["Item", "Quantidade", "Preco_Unitario", "Receita_Item"]].head())


# Tratamento de valores ausentes
print("\n--- VALORES AUSENTES ANTES DO TRATAMENTO ---")
print(pedidos.isnull().sum())

media_quantidade = pedidos["Quantidade"].mean()
pedidos["Quantidade"] = pedidos["Quantidade"].fillna(media_quantidade)

pedidos = pedidos.dropna(subset=["Preco_Unitario"])

pedidos["Receita_Item"] = pedidos["Quantidade"] * pedidos["Preco_Unitario"]

print("\n--- VALORES AUSENTES APÓS O TRATAMENTO ---")
print(pedidos.isnull().sum())


# Agregações por item
resumo_itens = pedidos.groupby("Item").agg(
    Quantidade_Total=("Quantidade", "sum"),
    Receita_Total=("Receita_Item", "sum")
).reset_index()

print("\n--- RESUMO POR ITEM ---")
print(resumo_itens)


top_5_quantidade = resumo_itens.sort_values(
    by="Quantidade_Total",
    ascending=False
).head(5)

print("\n--- TOP 5 ITENS MAIS VENDIDOS ---")
print(top_5_quantidade)


top_5_receita = resumo_itens.sort_values(
    by="Receita_Total",
    ascending=False
).head(5)

print("\n--- TOP 5 ITENS COM MAIOR RECEITA ---")
print(top_5_receita)