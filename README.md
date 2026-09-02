# Delivery Data Analysis

Projeto de análise de dados de pedidos de um serviço de delivery utilizando Python, Pandas e NumPy.

## Objetivo

O projeto tem como objetivo explorar, tratar e analisar dados de pedidos, criando indicadores e extraindo informações relevantes sobre vendas, produtos, categorias e comportamento ao longo do tempo.

## Tecnologias utilizadas

- Python
- Pandas
- NumPy

## Estrutura do projeto

```text
delivery-data-analysis/
├── dados/
│   ├── pedidos.csv
│   └── cardapio.csv
├── main.py
└── README.md
```

## Análises realizadas

O projeto inclui:

- carregamento dos dados com Pandas;
- análise exploratória com `head()`, `tail()`, `info()` e `describe()`;
- identificação e tratamento de valores ausentes;
- criação da coluna `Receita_Item`;
- agrupamento e análise dos produtos;
- identificação dos produtos mais vendidos e com maior receita;
- análise da receita ao longo do tempo;
- cruzamento dos pedidos com os dados do cardápio;
- análise de receita por categoria;
- filtro de Salgados com quantidade maior que 10;
- cálculo de KPIs;
- cálculo de percentis utilizando NumPy.

## Tratamento dos dados

Os valores ausentes da coluna `Quantidade` foram preenchidos com a média da própria coluna.

Os registros sem informação em `Preco_Unitario` foram removidos.

A receita de cada item foi calculada por meio da multiplicação da quantidade pelo preço unitário.

## Principais resultados

- Item com maior quantidade vendida: **Hamburguer**
- Item com maior receita: **Pizza Calabresa**
- Categoria com maior receita: **Salgados — R$ 53.073,30**
- Mês com maior receita: **Fevereiro de 2023 — R$ 6.646,03**
- Receita Total: **R$ 122.652,59**
- Total de Itens Vendidos: **6.833,25**
- Número de Pedidos analisados: **430**
- Ticket Médio: **R$ 285,24**

## Percentis

### Preço unitário

- 25%: R$ 8,92
- 50%: R$ 13,10
- 75%: R$ 27,40

### Quantidade

- 25%: 8
- 50%: 16
- 75%: 24

## Como executar

Instale as dependências:

```bash
pip install pandas numpy
```

Execute o projeto:

```bash
python main.py
```

## Autor

Projeto desenvolvido como exercício prático de análise de dados.