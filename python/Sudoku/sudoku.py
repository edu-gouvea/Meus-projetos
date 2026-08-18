def solve_sudoku(board):
    
    # vamos criar uma função principal que vai armazenar
    # funções internas que resolvem o sudoku, é mais fácil
    # criar uma função principal pois depois é só chamar
    # ela que resolverá tudo

    def eh_valido(linha, coluna, palpite):
        
        # essa função vai nos dizer se, seguindo as regras
        # do sudoku, o 'palpite' pode estar na posição
        # linha x coluna, ou seja vamos verificar se já existe
        # 'palpite' na linha, na coluna e na 'box', ou seja
        # no quadrado em que 'palpite está inserido  

        # verifica linha
        for i in range(9):
            if board[linha][i] == palpite:
                return False
            # se encontrar, já retorna false

        
        # verifica coluna
        for i in range(9):
            if board[i][coluna] == palpite:
                return False
            # mesma coisa, se encontrar, retorna false
        
        # verifica a 'box' 3x3
        box_linha = (linha // 3) * 3
        box_coluna = (coluna // 3) * 3
        # esse pequeno cálculo nos dirá onde que começa a box
        # do nosso palpite, por exemplo, se temos linha 5 e coluna 7
        # 'box_linha' = (5 // 3) * 3 = 3
        # 'box_coluna' = (7 // 3) * 3 = 6
        # ou seja a box começa na linha 3, coluna 6
        for i in range(box_linha, box_linha + 3):
            for j in range(box_coluna, box_coluna + 3):
                if board[i][j] == palpite:
                    return False
                # verifica se existe um número igual a palpite
                # na box, se tiver retorna false
                # note que i inicia em box_linha e vai até 
                # box_linha + 3, pois é onde a box começa e termina
                # e o mesmo acontece com a coluna
        
        return True
        # caso palpite não caia em nenhuma das checagens
        # retorna true

    def backtrack():
        for linha in range(9):
            for coluna in range(9):
                if board[linha][coluna] == ".":  
                # a primeira coisa é procurar um espaço vazio
                # para começar a dar o palpite
                    for palpite in map(str, range(1, 10)):
                        # vai tentar os números de 1 a 9
                        # em formato string
                        if eh_valido(linha, coluna, palpite):
                            board[linha][coluna] = palpite
                            # se for válido, seguindo a nossa função
                            # anterior, preenche com o número de palpite
                            if backtrack():
                                return True
                            # esse é um passo importante, pois fazemos
                            # uma chamada recursiva da própria função
                            # caso resolva tudo, ótimo
                            board[linha][coluna] = "."
                            # caso não, desfaz, ou seja volta a ser vazio
                            # isso é importante pois caso um valor seja preenchido
                            # em palpite e lá na frente esse valor não possa mais
                            # ser usado, pois causaria erro na nossa resolução,
                            # ele volta a ser vazio e o fluxo continua
                    return False  # se nenhum número couber, retorna false
        return True  # sudoku completo (não encontrou nenhum ".")

    backtrack()


def ler_test_case():
    print("Digite o seu sudoku, 9 linhas, valores separados por espaço, use . para espaços vazios:")
    board = []

    for _ in range(9):
        linha = input().strip().split()
        board.append(linha)
    # função simples de leitura do sudoku

    return board

test_case = ler_test_case() # atribui a 'test_case' a leitura feita em 'ler_test_case'
solve_sudoku(test_case) # usa a função principal para resolver
print("Sudoku resolvido:")
for row in test_case:
    print(" ".join(row)) # printa cada linha da resposta
