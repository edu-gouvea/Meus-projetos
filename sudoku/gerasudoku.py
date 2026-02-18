from random import shuffle, randint
from copy import deepcopy

# as duas funções a seguir já foram explicadas no resolvedor 
# de sudoku, porém elas vão nos ajudar a, obviamente, resolver o 
# sudoku gerado pelo nosso código, mas também para garantir uma solução 
# única do nosso sudoku 

def eh_valido(board, linha, coluna, palpite):
    for i in range(9):
        if board[linha][i] == palpite:
            return False
        if board[i][coluna] == palpite:
            return False

    box_linha = (linha // 3) * 3
    box_coluna = (coluna // 3) * 3

    for i in range(box_linha, box_linha + 3):
        for j in range(box_coluna, box_coluna + 3):
            if board[i][j] == palpite:
                return False

    return True

def solve_sudoku(board):
    for linha in range(9):
        for coluna in range(9):
            if board[linha][coluna] == ".":
                for palpite in map(str, range(1, 10)):
                    if eh_valido(board, linha, coluna, palpite):
                        board[linha][coluna] = palpite
                        if solve_sudoku(board):
                            return True
                        board[linha][coluna] = "."
                return False
    return True


# resolve contando número de soluções
# mas é apenas um wrapper que copia o board
# e chama '_count' 
def conta_solucoes(board):
    temp = deepcopy(board)
    return _count(temp)


# essa função funciona igual ao resolvedor visto anteriormente,
# no entanto incrementa um count toda vez que encontra uma solução
# completa. quando encontra volta a executar, e dentro do loop, caso 
# count > 1 já retorna, pois já se sabe que existe mais de uma 
# solução, logo não há a unicidade que desejamos
def _count(board):
    count = 0
    for linha in range(9):
        for coluna in range(9):
            if board[linha][coluna] == ".":
                for palpite in map(str, range(1, 10)):
                    if eh_valido(board, linha, coluna, palpite):
                        board[linha][coluna] = palpite
                        count += _count(board)
                        board[linha][coluna] = "."
                        if count > 1:
                            return count
                return count
    return 1  


# essa função vai gerar primeiro o nosso board
# primeiro preenchemos tudo com ".", e uma lista 
# 'numeros' que vai ser usada para preencher o board
# depois chamamos uma função recursiva 'fill' que percorre
# linha a linha e coluna por coluna, e pra todas as posições 
# vazias, vamos primeiro embaralhar os números dentro da nossa lista
# o que vai garantir aleatoriedade, depois se for válido preencher 
# o elemento do board com 'palpite' e chama fill, se fill retornar true,
# propagamos true, caso contrário, desfaz, colocando "." naquela posição
# e testa o próximo palpite, se nenhum dígito couber retorna false 
# quando todas as posições forem preenchidas fill retorna true
def gera_full_board():
    board = [["." for _ in range(9)] for _ in range(9)]
    numeros = list(map(str, range(1, 10)))

    def fill():
        for linha in range(9):
            for coluna in range(9):
                if board[linha][coluna] == ".":
                    shuffle(numeros)
                    for palpite in numeros:
                        if eh_valido(board, linha, coluna, palpite):
                            board[linha][coluna] = palpite
                            if fill():
                                return True
                            board[linha][coluna] = "."
                    return False
        return True

    fill()
    return board


# ess função vai de fato fazer o quebra-cabeça, a partir
# do nosso board todo preenchido, vamos retirar valores 
# mantendo a unicidade do quebra-cabeça, e a quantidade de remoções 
# vai depender da dificuldade que o usuário vai requisitar, com 
# easy sendo 35 remoções, medium sendo 45 e hard sendo 55.
# enquanto 'removals' for maior que 0, vamos selecionar 
# uma linha e uma coluna aleatória (de 0 a 8), se já for "."
# volta pois já foi removido, armazena backup como o número que está
# na posição e remove, agora sendo ".", chamando o 'conta_solucoes'
# caso não for igual a 1, rejeitamos a mudança, aquela posição volta 
# a ser o número que era, caso contrário diminui 1 em removals e segue 
# o loop, ao final retorna o board modificado, agora com vazios
def generate_puzzle(board, dificuldade):
    if dificuldade == "easy":
        removals = 35
    elif dificuldade == "medium":
        removals = 45
    else:
        removals = 55  # (hard)

    while removals > 0:
        linha = randint(0, 8)
        coluna = randint(0, 8)

        if board[linha][coluna] == ".":
            continue

        backup = board[linha][coluna]
        board[linha][coluna] = "."

        if conta_solucoes(board) != 1:
            board[linha][coluna] = backup
        else:
            removals -= 1

    return board


# função que compila tudo, gera o board, e depois forma o puzzle
# removendo números de certas posições
def gerar_sudoku(dificuldade):
    full = gera_full_board()
    puzzle = generate_puzzle(deepcopy(full), dificuldade)
    return puzzle, full

# pergunta a dificuldade desejada e printa tudo
dificuldade = input('Digite a dificuldade: ').strip()
puzzle, solution = gerar_sudoku(dificuldade)
print("Puzzle:")
for linha in puzzle:
    print(" ".join(linha))

print("\nSolução:")
for linha in solution:
    print(" ".join(linha))