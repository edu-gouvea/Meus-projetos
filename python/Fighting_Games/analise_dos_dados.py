import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns

# Configuração visual
sns.set_theme(style='whitegrid', palette='muted')
plt.rcParams['figure.dpi'] = 120

# Carregamento e preparação
df_vendas = pd.read_csv('vendas.csv', parse_dates=['Data_Pedido'])

# Criação da coluna 'Faturamento', correspondente ao produto do preço pela quantidade vendida
df_vendas['Faturamento'] = df_vendas['Preco_Unitario'] * df_vendas['Quantidade']

# Cria a coluna 'Mes' para analisar os meses com maior faturamento
df_vendas['Mes'] = df_vendas['Data_Pedido'].dt.to_period('M')

# Agrupando os jogos por nome e então fazendo a soma das quantidades respectivas ao nome, 
# ordenando de forma decrescente e agrupando apenas o head (5 primeiros)
top_5_jogos_mais_vendidos = df_vendas.groupby('Nome_Jogo')['Quantidade'].sum().sort_values(ascending=False).head()

# Agrupando os jogos por categorias e somando os respectivos faturamentos para visualizar os maiores
# faturamentos por categorias
faturamemto_por_categoria = df_vendas.groupby('Categoria')['Faturamento'].sum().sort_values(ascending=False)

# Agrupando os jogos por empresa criadora e somando os respectivos faturamentos para visualizar os maiores
# faturamentos por empresa
faturamemto_por_empresa = df_vendas.groupby('Empresa')['Faturamento'].sum().sort_values(ascending=False)

# Agrupando os jogos por plataforma e somando os respectivos faturamentos para visualizar os maiores
# faturamentos por plataforma
faturamemto_por_plataforma = df_vendas.groupby('Plataforma')['Faturamento'].sum().sort_values(ascending=False)

# Agrupando os jogos por mês de venda e somando os respectivos faturamentos para visualizar os maiores
# faturamentos por mês de venda
faturamento_por_mes = df_vendas.groupby('Mes')['Faturamento'].sum()

# Faturamento e quantidade de jogos por edição (especial ou não)
faturamento_por_edicao = df_vendas.groupby('Edicao_especial')['Faturamento'].sum()
quantidade_por_edicao = df_vendas.groupby('Edicao_especial')['Quantidade'].sum()

preco_medio = df_vendas.groupby(['Nome_Jogo', 'Plataforma'])['Preco_Unitario'].mean().unstack()

# Proporção de edição especial
proporcao_especial = (
    df_vendas.groupby(['Nome_Jogo', 'Edicao_especial'])['Quantidade']
    .sum()
    .unstack(fill_value=0)
    .assign(pct_especial=lambda x: x[True] / (x[True] + x[False]) * 100)
    .sort_values('pct_especial', ascending=False)
)

# Pivot jogo × plataforma (faturamento)
pivot_jogo_plataforma = df_vendas.pivot_table(
    values='Faturamento',
    index='Nome_Jogo',
    columns='Plataforma',
    aggfunc='sum',
    fill_value=0
)

# Pivot jogo × plataforma (faturamento)
pivot_empresa_plataforma = df_vendas.pivot_table(
    values='Faturamento',
    index='Empresa',
    columns='Plataforma',
    aggfunc='sum',
    fill_value=0
)

# Pivot jogo × plataforma (faturamento)
pivot_categoria_plataforma = df_vendas.pivot_table(
    values='Faturamento',
    index='Categoria',
    columns='Plataforma',
    aggfunc='sum',
    fill_value=0
)

# Visualização das primeiras e últimas 5 linhas do DataFrame
print(df_vendas.head())
print(df_vendas.tail())

fig, axes = plt.subplots(3, 3, figsize=(20, 15))
fig.suptitle('Dashboard de Vendas — Jogos de Luta', fontsize=16, fontweight='bold')

# 1. Top 5 jogos mais vendidos (barras horizontais)
ax = axes[0, 0]
top_5_jogos_mais_vendidos.sort_values().plot(kind='barh', ax=ax, color='steelblue')
ax.set_title('Top 5 Jogos Mais Vendidos')
ax.set_xlabel('Quantidade')

# 2. Faturamento por categoria
ax = axes[0, 1]
faturamemto_por_categoria.plot(kind='bar', ax=ax, color='coral')
ax.set_title('Faturamento por Categoria')
ax.set_ylabel('R$')
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
ax.tick_params(axis='x', rotation=30)

# 3. Faturamento por empresa (pizza)
ax = axes[0, 2]
faturamemto_por_empresa.plot(kind='pie', ax=ax, autopct='%1.1f%%', startangle=90)
ax.set_title('Faturamento por Empresa')
ax.set_ylabel('')

# 4. Faturamento mensal (linha)
ax = axes[1, 0]
faturamento_por_mes.plot(kind='line', marker='o', ax=ax, color='teal')
ax.set_title('Faturamento Mensal')
ax.set_ylabel('R$')
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
ax.tick_params(axis='x', rotation=45)

# 5. Edição especial vs normal — faturamento
ax = axes[1, 1]
faturamento_por_edicao.rename({True: 'Especial', False: 'Normal'}).plot(
    kind='bar', ax=ax, color=['gold', 'slategray']
)
ax.set_title('Faturamento: Edição Especial vs Normal')
ax.set_ylabel('R$')
ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'R${x:,.0f}'))
ax.tick_params(axis='x', rotation=0)

# 6. Edição especial por jogo
ax = axes[1, 2]
proporcao_especial['pct_especial'].sort_values().plot(kind='barh', ax=ax, color='tomato')
ax.set_title('% Vendas de Edição Especial por Jogo')
ax.set_xlabel('% de Edições Especiais')
ax.axvline(50, color='gray', linestyle='--', linewidth=0.8)

# 7. Heatmap jogo × plataforma
ax = axes[2, 0]
sns.heatmap(
    pivot_jogo_plataforma.astype(int), ax=ax,
    cmap='YlOrRd', fmt=',d', annot=True, linewidths=0.5,
    annot_kws={'size': 8}
)
ax.set_title('Faturamento por Jogo x Plataforma')
ax.tick_params(axis='x', rotation=30)
ax.tick_params(axis='y', rotation=0)

# 8. Heatmap empresa × plataforma
ax = axes[2, 1]
sns.heatmap(
    pivot_empresa_plataforma.astype(int), ax=ax,
    cmap='viridis_r',  fmt=',d', annot=True, linewidths=0.5,
    annot_kws={'size': 8}
)
ax.set_title('Faturamento por Empresa x Plataforma')
ax.tick_params(axis='x', rotation=30)
ax.tick_params(axis='y', rotation=0)

# 9.Heatmap categoria × plataforma
ax = axes[2, 2]
sns.heatmap(
    pivot_categoria_plataforma.astype(int), ax=ax,
    cmap='Blues', fmt=',d', annot=True, linewidths=0.5,
    annot_kws={'size': 8}
)
ax.set_title('Faturamento por Categoria x Plataforma')
ax.tick_params(axis='x', rotation=30)
ax.tick_params(axis='y', rotation=0)

plt.tight_layout()
plt.savefig('dashboard_vendas.png', bbox_inches='tight')
plt.show()
print("\nGráfico salvo em dashboard_vendas.png")