import random


janela = ["-", "-", "-",
          "-", "-", "-",
          "-", "-", "-"]
jogador = "X"
vencedor = None
jogo = True


def printjanela(janela):
    print(janela[0] + " | " + janela[1] + " | " + janela[2])
    print("---------")
    print(janela[3] + " | " + janela[4] + " | " + janela[5])
    print("---------")
    print(janela[6] + " | " + janela[7] + " | " + janela[8])


def jogadorInput(janela):
    inp = int(input("Escolha um espaço de 1-9"))
    if janela[inp-1] == "-":
        janela[inp-1] = jogador
    else:
        print("Amigão aí já está ocupado")


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


def linhaDiagonal(janela):
    global vencedor
    if janela[0] == janela[4] == janela[8] and janela[0] != "-":
        vencedor = janela[0]
        return True
    elif janela[2] == janela[4] == janela[6] and janela[4] != "-":
        vencedor = janela
        return True


def checarVitoria(janela):
    global jogo
    if linhaHorizontal(janela):
        printjanela(janela)
        print("O vencedor é " + str(vencedor)+"!")
        jogo = False

    elif linhavertical(janela):
        printjanela(janela)
        print("O vencedor é " + str(vencedor)+"!")
        jogo = False

    elif linhaDiagonal(janela):
        printjanela(janela)
        print(f"O vencedor é {vencedor}!")
        jogo = False


def checarEmpate(janela):
    global jogo
    if "-" not in janela:
        printjanela(janela)
        print("Empatou")
        jogo = False


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


while jogo:
    printjanela(janela)
    jogadorInput(janela)
    checarVitoria(janela)
    checarEmpate(janela)
    mudarDeJogador()
    computador(janela)
    checarVitoria(janela)
