def game():
    turno = 1
    rodada = 1
    while True:

        if vitoria() == 1:
            print("Jogador Vence")
            break
        elif vitoria() == -1:
            print("Maquina Vence")
            break
        elif vitoria() == 0:
            print("Empate")
            break

        if turno == 1:
            print("\nTurno do Jogador") 
            exibir()
            linha = int(input("\nDigite a linha desejada: "))
            coluna = int(input("\nDigite a coluna desejada: "))   

            if board[linha - 1][coluna - 1] == 0:
                board[linha - 1][coluna - 1] = 1
                turno = 0
            else:
                print("Espaço preenchido, tente novamente") 

        else:
            (m,linha,coluna) = max()
            board[linha][coluna] = -1
            turno = 1

    return 0

# Metodo para otimizar as decições da IA
def max():

    # Possivies valores para maxv são:
    # -1 = Perda
    # 0 = Empate
    # 1 = Vitoria

    # Inicialização para o pior dos casos
    maxv = -2

    linha = None
    coluna = None

    resultado = vitoria()

    if resultado == 1:
        return (-1,0,0)
    elif resultado == -1:
        return (1,0,0)
    elif resultado == 0:
        return (0,0,0)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                # Caso se estiver vazio, o jogador faz a jogada e chama a função min
                board[i][j] = -1
                #exibir()
                (m, min_i, min_j) = min()
                # Reparando o valor de maxv se caso necessário
                if m > maxv:
                    maxv = m
                    linha = i
                    coluna = j

                board[i][j] = 0
    return (maxv,linha,coluna)                                 

# Metodo para minimizar a pontuação da IA
def min():

    # Possivies valores para minv são:
    # -1 = Perda
    # 0 = Empate
    # 1 = Vitoria

    # Inicialização para o pior dos casos
    minv = 2
    
    linha = None
    coluna = None

    resultado = vitoria()

    if resultado == 1:
        return (-1,0,0)
    elif resultado == -1:
        return (1,0,0)
    elif resultado == 0:
        return (0,0,0)   
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = 1
                #exibir()
                (m, max_i, max_j) = max()
                if m < minv:
                    minv = m
                    linha = i
                    coluna = j

                board[i][j] = 0

    return (minv,linha,coluna) 


# Metodo para exibir em tela o tabuleiro
def exibir():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(" _ ", end=' ')
            elif board[i][j] == 1:
                print(" X ", end=' ')
            elif board[i][j] == -1:
                print(" O ", end=' ')

        print()

# Metodo para checagem de vitoria     
def vitoria():
    # Checando as Linhas
    for i in range(3):
        soma = board[i][0] + board[i][1] + board[i][2]
        if soma == 3:
            return 1
        elif soma == -3:
            return -1    
    # Checando as Colunas
    for i in range(3):
        soma = board[0][i] + board[1][i] + board[2][i]
        if soma == 3:
            return 1
        elif soma == -3:
            return -1

    # Checando as Diagonais
    diagonal1 = board[0][0] + board[1][1] + board[2][2]
    diagonal2 = board[0][2] + board[1][1] + board[2][0]  
    # Se a maquina ganhou pela diagonal
    if diagonal1 == 3 or diagonal2 == 3:
        return 1
    # Se o jogador ganhou pela diagonal    
    elif diagonal1 == -3 or diagonal2 == -3:
        return -1               
    # Verifica se há espaço
    for i in range(3):
        for o in range(3):
            if (board[i][o] == 0):
                return None

    return 0

board = [[0,0,0],[0,0,0],[0,0,0]]
game()
exibir()    