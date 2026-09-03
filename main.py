import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


pedidos = pd.read_csv("dados/pedidos.csv")

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


# Análise temporal
pedidos["Data"] = pd.to_datetime(pedidos["Data"])

pedidos["Mes"] = pedidos["Data"].dt.to_period("M")

receita_mensal = pedidos.groupby("Mes")["Receita_Item"].sum().reset_index()

print("\n--- RECEITA MENSAL ---")
print(receita_mensal)

print("\n--- MAIOR RECEITA MENSAL ---")
print(
    receita_mensal.sort_values(
        by="Receita_Item",
        ascending=False
    ).head(1)
)


# Cruzamento com o cardápio
cardapio = pd.read_csv("dados/cardapio.csv")

print("\n--- CARDÁPIO ---")
print(cardapio.head())

dados_completos = pedidos.merge(
    cardapio,
    on="Item",
    how="left"
)

print("\n--- DADOS APÓS O MERGE ---")
print(
    dados_completos[
        ["Item", "Categoria", "Quantidade", "Receita_Item"]
    ].head()
)


# Receita por categoria
receita_categoria = dados_completos.groupby(
    "Categoria"
)["Receita_Item"].sum().reset_index()

receita_categoria = receita_categoria.sort_values(
    by="Receita_Item",
    ascending=False
)

print("\n--- RECEITA POR CATEGORIA ---")
print(receita_categoria)

# Gráfico - Receita por Categoria
ax = receita_categoria.plot(
    x="Categoria",
    y="Receita_Item",
    kind="bar",
    figsize=(10, 6),
    legend=False
)

plt.title("Receita por Categoria")
plt.xlabel("Categoria")
plt.ylabel("Receita (R$)")
plt.xticks(rotation=45)

# Adiciona o valor de receita acima de cada barra
for container in ax.containers:
    ax.bar_label(
        container,
        fmt="R$ %.2f",
        padding=3
    )

plt.tight_layout()
plt.savefig("graficos/receita_por_categoria.png", dpi=300, bbox_inches="tight")

# Gráfico - Evolução Mensal da Receita
plt.figure(figsize=(12, 6))

plt.plot(
    receita_mensal["Mes"].astype(str),
    receita_mensal["Receita_Item"],
    marker="o"
)

plt.title("Evolução Mensal da Receita")
plt.xlabel("Mês")
plt.ylabel("Receita (R$)")
plt.xticks(
    ticks=range(0, len(receita_mensal), 3),
    labels=receita_mensal["Mes"].astype(str)[::3],
    rotation=45
)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("graficos/evolucao_receita_mensal.png", dpi=300, bbox_inches="tight")

# Top 5 itens por receita
top5_receita = resumo_itens.nlargest(5, "Receita_Total")

# Gráfico - Top 5 Itens por Receita
ax = top5_receita.sort_values("Receita_Total").plot(
    x="Item",
    y="Receita_Total",
    kind="barh",
    figsize=(10, 6),
    legend=False
)

plt.title("Top 5 Itens por Receita")
plt.xlabel("Receita (R$)")
plt.ylabel("Item")

# Adiciona os valores nas barras
for container in ax.containers:
    ax.bar_label(
        container,
        fmt="R$ %.2f",
        padding=3
    )

plt.tight_layout()
plt.savefig("graficos/top_5_itens_receita.png", dpi=300, bbox_inches="tight")
plt.show()

# Categoria com maior receita
categoria_maior_receita = receita_categoria.head(1)

print("\n--- CATEGORIA COM MAIOR RECEITA ---")
print(categoria_maior_receita)


# Filtro de salgados com quantidade maior que 10
salgados_filtrados = dados_completos[
    (dados_completos["Categoria"] == "Salgados")
    & (dados_completos["Quantidade"] > 10)
]

print("\n--- SALGADOS COM QUANTIDADE MAIOR QUE 10 ---")
print(
    salgados_filtrados[
        ["ID_Pedido", "Item", "Quantidade", "Preco_Unitario", "Receita_Item"]
    ]
)


# KPIs
receita_total = dados_completos["Receita_Item"].sum()

total_itens_vendidos = dados_completos["Quantidade"].sum()

numero_pedidos = dados_completos["ID_Pedido"].nunique()

ticket_medio = receita_total / numero_pedidos

print("\n--- KPIs ---")
print(f"Receita Total: R$ {receita_total:.2f}")
print(f"Total de Itens Vendidos: {total_itens_vendidos:.2f}")
print(f"Número de Pedidos: {numero_pedidos}")
print(f"Ticket Médio: R$ {ticket_medio:.2f}")


# Percentis com NumPy
percentis_preco = np.percentile(
    pedidos["Preco_Unitario"],
    [25, 50, 75]
)

percentis_quantidade = np.percentile(
    pedidos["Quantidade"],
    [25, 50, 75]
)

print("\n--- PERCENTIS DO PREÇO UNITÁRIO ---")
print(f"25%: R$ {percentis_preco[0]:.2f}")
print(f"50%: R$ {percentis_preco[1]:.2f}")
print(f"75%: R$ {percentis_preco[2]:.2f}")

print("\n--- PERCENTIS DA QUANTIDADE ---")
print(f"25%: {percentis_quantidade[0]:.2f}")
print(f"50%: {percentis_quantidade[1]:.2f}")
print(f"75%: {percentis_quantidade[2]:.2f}")