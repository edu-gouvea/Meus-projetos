import pandas as pd
'''
    Esse código tem o intuito de fazer uma análise básica sobre os dados
    acerca dos livros bestsellers da Amazon 
'''

# Ler o arquivo com a base de dados dos bestsellers
arquivo = 'bestsellers.csv'
df = pd.read_csv(arquivo)

'''
# Analisar as primeiras 5 linhas para ter noção de como os dados
# estão organizados
print('Primeiras 5 linhas')
print(df.head())

# Últimas 5 linhas
print('\nÚltimas 5 linhas')
print(df.tail())

# Ver todos os nomes das categorias das colunas
print('\nColunas')
print(df.columns)

# Analisar os tipos de dado de cada coluna
print('\nTipos de dados de cada coluna')
print(df.dtypes)

# Uma descrição estatística de todos os dados numéricos
print('\nDescrição estatística')
print(df.describe())

# Verifiar se há dados nulos ou dupliados
print('\nSoma da quantidade de linhas com valores nulos por coluna')
print(df.isnull().sum())
print('\nSoma da quantidade de linhas com valores duplicados totais')
print(df.duplicated().sum())
'''

# essas análises foram colocadas como docstring, mas para ver
# tudo isso basta apagar as aspas simples triplas antes e depois do bloco


'''
    Visto isso, agora é preciso ajeitar algumas coisas, como alterar o nome das colunas para
    serem mais explicativas, e alterar o tipo de 'Price' para float64, pois como se trata de preços,
    estamos falando de números com casas decimais
'''

# Alterando o nome das colunas (inplace faz a base de dados ser alterada no próprio arquivo)
df.rename(columns={'Name': 'Title', 'Year': 'Publication Year', 'User Rating': 'Rating'}, inplace=True)

# Mudar o tipo de 'Price'
df['Price'] = df['Price'].astype(float)


'''
    Agora a parte mais prática, fazer análises mais interessantes sobre esses dados
'''


# Agrupa todas as linhas por gênero e organiza com a média de nota
# por gênero
media_rating_by_genre = df.groupby('Genre')['Rating'].mean()
print('\nMédia de nota por gênero')
print(media_rating_by_genre)

# Agrupa todas as linhas por gênero e organiza com a média de preço
# por gênero
media_price_by_genre = df.groupby('Genre')['Price'].mean()
print('\nMédia de preço por gênero')
print(media_rating_by_genre)

# Ver quais são os top 10 autores que mais estão presentes
quant_authors = df['Author'].value_counts()
print('\nTop 10 autores com mais bestsellers')
print(quant_authors.sort_values(ascending=False).head(10))

# Agrupa todas as linhas por autor e organiza com a média de nota
# por autor. E printa os top 10 autores com a maior média de nota
media_rating_by_author = df.groupby('Author')['Rating'].mean()
print('\nTop 10 autores com maior média de nota')
print(media_rating_by_author.sort_values(ascending=False).head(10))

# Agrupa todas as linhas por autor e organiza com a média de preço
# por autor. E printa os top 10 autores com a maior média de preço
media_price_by_author = df.groupby('Author')['Price'].mean()
print('\nTop 10 autores com maior média de preço')
print(media_price_by_author.sort_values(ascending=False).head(10))

# Como existem muitos autores, para ter uma visão melhor da distribuição
# desses dados, vamos exportar esses agrupamentos para arquivos separados
quant_authors.to_csv('csv_criados/authors_with_more_books.csv')
media_rating_by_author.to_csv('csv_criados/media_rating_by_author.csv')
media_price_by_author.to_csv('csv_criados/media_price_by_author.csv')