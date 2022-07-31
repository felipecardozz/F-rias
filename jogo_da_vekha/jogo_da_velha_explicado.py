# Passos                (DEVEM SER APAGADOS PARA FUNCIONAR)
import random
1. Jogo no terminal como um tabuleiro                 # <-- apagar
2. Forma de reconhecer a escolha do jogador(o input)  # <-- apagar
3. Reconhecer vitória ou empate                       # <-- apagar
4. Trocar o jogador(bola vira x e vice-versa)         # <-- apagar
5. Reconhecer vitória ou empate denovo...             # <-- apagar"

#  1.        O jogo aparece no terminal e assim precisa de 9 quadrados para colocar os Xs e Círculos

janela = ["-", "-", "-",  # espaços dos Xs e Círculos
          "-", "-", "-",
          "-", "-", "-"]
jogador = "X"             # Jogador começa sendo X
vencedor = None           # Não existe vencedor ainda ao começar
# Esse jogo muitas vezes é escrito como gameRunning e usado no game loop que é o "while jogo", lá no final
jogo = True

#  1.1 Espaçamento dos quadrados


# Definindo as possibilidades de escolha nos espaços, ou seja onde coloco o X
def printjanela(janela):
    print(janela[0] + " | " + janela[1] + " | " + janela[2])
    print("---------")
    print(janela[3] + " | " + janela[4] + " | " + janela[5])
    print("---------")
    print(janela[6] + " | " + janela[7] + " | " + janela[8])

#  2.Como saber qual dos espaços o jogador escolheu, sendo que não da pra fzer um X onde já tem um circulo


def jogadorInput(janela):
    inp = int(input("Escolha um espaço de 1-9"))
    if janela[inp-1] == "-":
        janela[inp-1] = jogador
    else:
        print("Amigão aí já está ocupado")

# Reconhecer o vencedor ou um empate, definindo as regras de retas
# Vitória nas 3 horizontais


def linhaHorizontal(janela):
    global vencedor
    if janela[0] == janela[1] == janela[2] and janela[0] != "-":
        vencedor = janela[0]
        return True
    elif janela[3] == janela[4] == janela[5] and janela[3] != "-":
        vencedor = janela[3]
        return True
    elif janela[6] == janela[7] == janela[8] and janela[6] != "-":
        vencedor = janela[6]
        return True


# Somente 3 verticais possíveis para vitória
def linhavertical(janela):
    global vencedor
    if janela[0] == janela[3] == janela[6] and janela[0] != "-":
        vencedor = janela[0]
        return True
    elif janela[1] == janela[4] == janela[7] and janela[1] != "-":
        vencedor = janela[1]
        return True
    elif janela[2] == janela[5] == janela[8] and janela[2] != "-":
        vencedor = janela[3]
        return True

# Somente duas diagonais possíveis


def linhaDiagonal(janela):
    global vencedor
    if janela[0] == janela[4] == janela[8] and janela[0] != "-":
        vencedor = janela[0]
        return True
    elif janela[2] == janela[4] == janela[6] and janela[4] != "-":
        vencedor = janela
        return True

# Ver se ganhou a partir da regra das linhas


def checarVitoria(janela):
    global jogo

# Vitória na horizontal
    if linhaHorizontal(janela):
        printjanela(janela)
        print("O vencedor é " + str(vencedor)+"!")
        jogo = False

# Vitória na vertical
    elif linhavertical(janela):
        printjanela(janela)
        print("O vencedor é " + str(vencedor)+"!")
        jogo = False

# Vitória na diagonal
    elif linhaDiagonal(janela):
        printjanela(janela)
        print(f"O vencedor é {vencedor}!")  # String mas em f String
        jogo = False

# Ver se empatou


def checarEmpate(janela):
    global jogo
    if "-" not in janela:
        printjanela(janela)
        print("Empatou")
        jogo = False


# Troca de X para bola ou círculo
def mudarDeJogador():
    global jogador
    if jogador == "X":
        jogador = "O"
    else:
        jogador = "X"


def computador(janela):
    while jogador == "O":
        posição = random.randint(0, 8)
        if janela[posição] == "-":
            janela[posição] = "O"
            mudarDeJogador()


# Game loop, faz todas as funções rodarem ao apertar o botão
while jogo:
    printjanela(janela)
    jogadorInput(janela)
    checarVitoria(janela)
    checarEmpate(janela)
    mudarDeJogador()
    computador(janela)
    checarVitoria(janela)
