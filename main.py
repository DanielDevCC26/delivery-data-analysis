import pandas as pd
import numpy as np


pedidos = pd.read_csv("pedidos.csv")

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