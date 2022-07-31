import random
import math

# Definindo a função jogar para que se encaixe no loop la no final


def jogar():
    usuario = input(
        "Pedra, papel e tesouraa ... \n")  # /n cria uma nova linha, assim as palavras depois dele e antes das aspas = "" são mostradas em outra linha
    usuario = usuario.lower()

    computador = random.choice(['pedra', 'papel', 'tesoura'])

    if usuario == computador:
        return (0, usuario, computador)

    #
    if vitoria(usuario, computador):
        return (1, usuario, computador)

    return (-1, usuario, computador)

# Estabelecendo as condições de vitória


def vitoria(jogador, oponente):
    # Se o jogador ganhar do oponente ele return True
    if (jogador == 'pedra' and oponente == 'tesoura') or (jogador == 'tesoura' and oponente == 'papel') or (jogador == 'papel' and oponente == 'pedra'):
        return True
    return False


def melhor_de(n): 
    # joga até ganharem a melhor de partidas pré determinadas 
    jogador_vencedor = 0
    computador_vencedor = 0
    vitórias_necessárias = math.ceil(n/2)
    # forma de representar se foi pedra, papel e tesoura
    while jogador_vencedor < vitórias_necessárias and computador_vencedor < vitórias_necessárias:
        resultado, usuario, computador = jogar()

# Se for empate
        if resultado == 0:
            print(
                'Empatou. \n'.format(usuario))

# Se você ganhar ou o computador
        elif resultado == 1:
            jogador_vencedor += 1
            print('Você escolheu {}, e o computador {}. Você venceu!\n'.format(
                usuario, computador))
        else:
            computador_vencedor += 1
            print(
                'Você escolheu{}, e o computador {}. Perdeu, bobão! :(\n'.format(usuario, computador))

# Quando a melhor de {} acaba
    if jogador_vencedor > computador_vencedor:
        # Quando {} mostra o número de partidas - melhor de 3
        print('Você ganhou a melhor de {}'.format(n))
    else:
        print(
            'Manezão, deixou o computador ganhar de tu. Nem tenta mais, meu Deus'.format(n))


if __name__ == '__main__':
    jogar
    melhor_de(3)
