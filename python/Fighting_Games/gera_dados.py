import pandas as pd
from random import choice, randint
from datetime import datetime, timedelta

class Gerador_Dados:

    '''Função para gerar o DataFrame que será utilizado 
        na análise posterior das vendas. Essa empresa fictícia
        é uma vendedora de jogos de luta virtual e está interessada em saber 
        os seus jogos mais vendidos'''
    
    def gera_dados(num_registros = 1000) -> pd.DataFrame: 
        print(f'\nGerando {num_registros} registros de venda...')

        # Dicionário com os jogos e suas especificações
        jogos = {
            'Mortal Kombat X' : {'categoria' : 'violento','empresa' : 'NetherRealm', 'preco' : 99.90},
            'Mortal Kombat 11' : {'categoria' : 'violento', 'empresa' : 'NetherRealm', 'preco' : 199.90},
            'Mortal Kombat 1' : {'categoria' : 'violento', 'empresa' : 'NetherRealm', 'preco' : 249.90},
            'Injustice Gods Among Us' : {'categoria' : 'herois', 'empresa' : 'NetherRealm', 'preco' : 89.90},
            'Injustice 2' : {'categoria' : 'herois', 'empresa' : 'NetherRealm', 'preco' : 163.50},
            'Street Fighter IV' : {'categoria' : 'arcade', 'empresa' : 'Capcom', 'preco' : 69.50},
            'Street Fighter V' : {'categoria' : 'arcade', 'empresa' : 'Capcom', 'preco' : 129.70},
            'Street Fighter VI' : {'categoria' : 'arcade', 'empresa' : 'Capcom', 'preco' : 229.90},
            'Marvel vs Capcom 3' : {'categoria' : 'herois', 'empresa' : 'Capcom', 'preco' : 99.99},
            'Marvel vs Capcom Infinite' : {'categoria' : 'herois', 'empresa' : 'Capcom', 'preco' : 199.99},
            'Tekken 7' : {'categoria' : '3D', 'empresa' : 'Namco', 'preco' : 175.29},
            'Tekken 8' : {'categoria' : '3D', 'empresa' : 'Namco', 'preco' : 225.79},
        }

        # Lista com os nomes dos jogos
        lista_nomes = list(jogos.keys())

        # Lista com a plataforma na qual o jogo foi comprado
        plataforma = ['Xbox', 'Playstation', 'PC']

        # Define a data inicial dos pedidos
        data_inicial = datetime(2026, 1, 1)

        # Lista que armazenará os dados das vendas
        dados_vendas = []

        for i in range(num_registros):
            
            # Nome aleatório de um jogo
            nome_jogo = choice(lista_nomes)

            # Plataforma aleatória
            plataforma_jogo = choice(plataforma)

            # Quantidade de jogos comprados nessa venda (de 1 a 2)
            quantidade = randint(1,2)

            # Define a data do pedido baseado na data inicial
            data_pedido = data_inicial + timedelta(days = int(i/5), hours = randint(0, 23))

            # Define se foi comprada edição especial do jogo ou não
            edicao_especial = choice([True,False])

            # Se for edição especial é aplicado um aumento de 40% no preço do jogo
            if edicao_especial:
                preco_unitario = jogos[nome_jogo]['preco'] * 1.4
            else:
                preco_unitario = jogos[nome_jogo]['preco']

            dados_vendas.append({
                'ID_Pedido' : 1000 + i,
                'Data_Pedido': data_pedido,
                'Nome_Jogo': nome_jogo,
                'Categoria': jogos[nome_jogo]['categoria'],
                'Empresa' : jogos[nome_jogo]['empresa'],
                'Plataforma' : plataforma_jogo,
                'Preco_Unitario': round(preco_unitario, 2),
                'Quantidade': quantidade,
                'ID_Cliente': randint(100, 150),
                'Edicao_especial' : edicao_especial
            })

        print('Geração de dados concluída')

        return pd.DataFrame(dados_vendas)

def main():
    df = Gerador_Dados.gera_dados()
    
    df.to_csv('vendas.csv', index=False)

if __name__ == "__main__":
    main()